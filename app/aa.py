data = [
        {
            "attack": 100,
            "defense": 123,
            "generation": 1,
            "hp": 80,
            "id": 4827,
            "name": "Raju",
            "rank": 89,
            "sp_atk": 122,
            "sp_def": 120,
            "speed": 80,
            "total": 625,
            "type_1": "Grass",
            "type_2": "Poison"
        },
        {
            "defense": 83,
            "generation": 1,
            "hp": 80,
            "id": 4829,
            "name": "Raju Ramu",
            "rank": 89,
            "sp_atk": 122,
            "sp_def": 120,
            "speed": 80,
            "total": 625,
            "type_1": "Grass",
            "type_2": "Poison"
        },
        {
            "defense": 83,
            "generation": 1,
            "hp": 80,
            "id": 4826,
            "name": "MohanMohan",
            "rank": 987,
            "sp_atk": 100,
            "sp_def": 100,
            "speed": 80,
            "total": 525,
            "type_1": "Grass",
            "type_2": "Poison"
        },
        {
            "attack": 82,
            "defense": 83,
            "generation": 1,
            "hp": 80,
            "id": 4828,
            "name": "Mohan Reddy",
            "rank": 987,
            "sp_atk": 100,
            "sp_def": 100,
            "speed": 80,
            "total": 525,
            "type_1": "Grass",
            "type_2": "Poison"
        }
    ]
values = []
for item in data:
    new_item = {}
    for column in Pokemon.__table__.c.keys():
        new_item[column] = item.get(column) or getattr(Pokemon.__table__.c, column)
    values.append(new_item)

values = [
    {
        item[column] = item.get(column) or getattr(Pokemon.__table__.c, column)
        for column in Pokemon.__table__.c.keys()
    }
    for item in data
    ]




data = {}
data['task'] = 'mohan'
data['due_date'] = 'april'
data['complete'] = 'kind'