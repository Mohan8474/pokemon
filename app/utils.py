from app.models import Pokemon, db
from sqlalchemy.dialects.postgresql import insert


def task_to_dict(pokemon):
    return {column: getattr(pokemon, column) for column in Pokemon.__table__.c.keys()}


# check if it works when there are multiple tables and has relations between each table


def upsert_do_update(data):
    
    insert_stmt = insert(Pokemon).values(data)
    update_columns = {
        col.name: col
        for col in insert_stmt.excluded
        if col.name != "id"
    }

    upsert_statement = insert_stmt.on_conflict_do_update(
        constraint=Pokemon.__table__.primary_key,
        set_=update_columns,
    )

    db.session.execute(upsert_statement)
    db.session.commit()