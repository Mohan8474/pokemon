# Installed Imports
from flask import Blueprint, request, url_for
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
# from flask_jwt_extended import jwt_required

# Custom Imports
from app import app, db, utils
from app.models import Pokemon, PokemonSchema

# from app.auth import login_required


pokemon_api = Blueprint("pokemon_api", __name__, url_prefix="/pokemons")
pokemon_schema = PokemonSchema(many=True)


class PokemonException(Exception):
    def __init__(self, message, code=400):
        self.message = message
        self.code = code


@pokemon_api.errorhandler(PokemonException)
def handle_exception(e):
    app.logger.exception(e)
    return {"success": False, "error": e.message}, e.code


@pokemon_api.errorhandler(SQLAlchemyError)
def handle_sql_exception(e):
    app.logger.exception(e)
    return {"success": False, "error": str(e)}, 400


# <<<<<<<<<<<<<<<<<<<<<<<< API >>>>>>>>>>>>>>>>>>


@pokemon_api.route("/", methods=["GET"])
@pokemon_api.route("/<int:id>", methods=["GET"])
# @jwt_required
def get_pokemon(id=None):
    """
    This API retrieves pokemon
    If the id is metioned it retrieves pokemon based on id else it will retrieve all pokemon .
    query_params:
        limit(int): records per page
        sort(str): column to sort on.
        order(str): desc/asc
        page(int): fetch the requested page.
        search(str): search str in pokemon name
        legendary(bool) : fetch pokemon based on legendary
        type_1(str) : fetch pokemon based on type_1
        type_2(str) : fetch pokemon based on type_2
        generation(int) : fetch pokemon based on generation
        id (int, Optional): id to retrieve pokemon
    """
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", app.config["PAGE_LIMIT"], type=int)
    order = request.args.get("order", "asc")
    sort = request.args.get("sort", "rank")
    search = request.args.get("search")
    legendary = request.args.get("legendary")
    type_1 = request.args.get("type_1")
    type_2 = request.args.get("type_2")
    generation = request.args.get("generation", 1, type=int)
    pokemon = Pokemon.query

    if id:
        pokemon = pokemon.filter(Pokemon.id == id)
        if not pokemon.first():
            raise PokemonException(
                f"Pokemon with id {id} doesn't exist.",
                404,
            )

    if order == "asc":
        pokemon = pokemon.order_by(sort)
    else:
        pokemon = pokemon.order_by(desc(sort))

    if search:
        pokemon = pokemon.filter(Pokemon.name.ilike(f"%{search}%"))

    if legendary:
        pokemon = pokemon.filter(Pokemon.legendary == legendary)

    if type_1:
        pokemon = pokemon.filter(Pokemon.type_1 == type_1)

    if type_2:
        pokemon = pokemon.filter(Pokemon.type_2 == type_2)

    if generation:
        pokemon = pokemon.filter(Pokemon.generation == generation)

    pokemon = pokemon.paginate(page=page, per_page=limit, error_out=False)

    all_pokemon = pokemon_schema.dump(pokemon)
    if len(all_pokemon) == 0:
        raise PokemonException(
            "No pokemon found.",
            404,
        )

    if pokemon.has_next:
        next_url = url_for("pokemon_api.get_pokemon", page=pokemon.next_num)
    else:
        next_url = None

    return {
        "all_pokemon": all_pokemon,
        "total": pokemon.total,
        "order": order,
        "sort": sort,
        "page": pokemon.page,
        "total_pages": pokemon.pages,
        "next_page": next_url,
    }, 200


@pokemon_api.route("/", methods=["POST", "PUT"])
@pokemon_api.route("/<int:id>", methods=["PUT"])
def add_pokemon(id=None):
    """
    Create or update a Pokémon.

    Request method: POST, PUT
    This route accepts both POST and PUT requests. For POST requests, it creates a new Pokémon with the provided data.
    For PUT requests, it updates an existing Pokémon identified by the `id` parameter with the provided data.

    Request method: PUT
    This route updates an existing Pokémon identified by the `id` parameter with the provided data.
    Args:
        id (int): The ID of the Pokémon to be updated.
    """
    pokemon_data = request.get_json()

    if not pokemon_data:
        raise PokemonException("No data found", 404)

    values = []
    update_pokemon = []
    insert_pokemon = []

    for item in pokemon_data:
        if id:
            pokemon = Pokemon.query.filter_by(id=id).first()
            if not pokemon:
                raise PokemonException(
                    f"Pokemon with id {id} doesn't exist.",
                    404,
                )
            new_item = {}
            for column in Pokemon.__table__.c.keys():
                new_item[column] = item.get(column) or getattr(pokemon, column)
            values.append(new_item)

        else:
            new_item = {}

            if "id" in item:
                pokemon = Pokemon.query.get(item["id"])
                if not pokemon:
                    raise PokemonException(
                        f"No pokemon found with the given ID.",
                        404,
                    )
                for column in Pokemon.__table__.c.keys():
                    new_item[column] = item.get(column) or getattr(pokemon, column)
                update_pokemon.append(new_item)

            else:
                for column in Pokemon.__table__.c.keys():
                    if column == "id":
                        continue
                    new_item[column] = item.get(column)
                insert_pokemon.append(new_item)

    if len(insert_pokemon) > 0:
        values.append(insert_pokemon)
    if len(update_pokemon) > 0:
        values.append(update_pokemon)

    upsert = utils.upsert_do_update(values)

    return {"message": upsert}, 201


@pokemon_api.route("/", methods=["DELETE"])
@pokemon_api.route("/<int:id>", methods=["DELETE"])
def delete_pokemon(id=None):
    """
    This API deletes the pokemon.
    Deletes single pokemon if id is passed else deletes all pokemon
    """
    if id:
        pokemon = Pokemon.query.get(id)
        if pokemon is None:
            raise PokemonException("No Data Exists", 404)
        db.session.delete(pokemon)
    else:
        db.session.query(Pokemon).delete()
        db.session.commit()

    db.session.commit()
    return {"message": "Successfully deleted"}, 200
