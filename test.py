import json
from pathlib import Path

DB_PATH = Path("data/students.json")

def load_file():
    # Reading JSON file
    with open(DB_PATH, "r") as file:
        data = json.load(file)
    return data

# file = load_file()
# print(file)

def write_file(datas):
        # Write dictionary to a JSON file
    db = load_file()
    db.append(datas)    
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=4)   # indent makes it pretty-printed
    print("Update Succesful !")    


sample_d =   {
    "id": 111,
    "name": "RAni ",
    "age": 21,
    "city": "Pune",
    "skills": ["sql", "python"],
    "scores": {"math": 86, "english": 89, "science": 91},
    "active": True,
    "joined": "2024-05-10"
  }


def delete_student(id):
    pass

READ_DATA = load_file()

for student in READ_DATA:
    print("    _        _     ",student['name'])
    for skil in student['skills']:
        print(skil)