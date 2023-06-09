from app.models import Pokemon, db
from sqlalchemy.dialects.postgresql import insert


# check if it works when there are multiple tables and has relations between each table


def upsert_do_update(values):
    try:

        for value in values:
            insert_stmt = insert(Pokemon).values(value)
            to_update = {col.name: col for col in insert_stmt.excluded if col.name != "id"}

            upsert_statement = insert_stmt.on_conflict_do_update(
                constraint="pokemon_pkey",
                set_=to_update,
            )

            db.session.execute(upsert_statement)
        db.session.commit()

        return {
            "success": True,
            "message": "records updated.",
        }
    except Exception as e:
        print(f"Error: {e}")
 
