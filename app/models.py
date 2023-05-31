from app import app, db
from dataclasses import dataclass


@dataclass
class Pokemon(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    rank: int = db.Column(db.Integer)
    name: str = db.Column(db.Text)
    type_1: str = db.Column(db.Text)
    type_2: str = db.Column(db.Text)
    total: int = db.Column(db.Integer)
    hp: int = db.Column(db.Integer)
    attack: int = db.Column(db.Integer)
    defense: int = db.Column(db.Integer)
    sp_atk: int = db.Column(db.Integer)
    sp_def: int = db.Column(db.Integer)
    speed: int = db.Column(db.Integer)
    generation: int = db.Column(db.Integer)
    legendary: bool = db.Column(db.Boolean, default = False)

    def get_editable_fields(self):
        return (
            "rank",
            "name",
            "type_1",
            "type_2",
            "generation",
            "legendary"
        )
