# import os
# import sys
import json

from app import app
from app.models import db, Pokemon
import urllib.request, json

url = "https://coralvanda.github.io/pokemon_data.json"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

app.app_context().push()


def create_object_in_db_at_startup():
    for pokemon in data:
        pokemon = Pokemon(
            rank=pokemon["#"],
            name=pokemon["Name"],
            type_1=pokemon["Type 1"],
            type_2=pokemon["Type 2"],
            total=pokemon["Total"],
            hp=pokemon["HP"],
            attack=pokemon["Attack"],
            defense=pokemon["Defense"],
            sp_atk=pokemon["Sp. Atk"],
            sp_def=pokemon["Sp. Def"],
            speed=pokemon["Speed"],
            generation=pokemon["Generation"],
            legendary=pokemon["Legendary"],
        )
        db.session.add(pokemon)
    db.session.commit()


create_object_in_db_at_startup()
