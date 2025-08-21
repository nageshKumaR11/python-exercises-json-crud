import json
from pathlib import Path

DB_PATH = Path("data/students.json")

def load_file():
    # Reading JSON file
    with open(DB_PATH, "r") as file:
        data = json.load(file)
    return data

DB_FILE = load_file()


def delete_student(id):
    new_file = []
    for student in DB_FILE:
        if student['id'] != id:
            new_file.append(student)
        # Step 3: Write back the updated list
    with open(DB_PATH, "w") as f:
        json.dump(new_file, f, indent=4)
    print("Deletion succesful ")

delete_student(111)

            





























# sample_d =   {
#     "id": 111,
#     "name": "RAni ",
#     "age": 21,
#     "city": "Pune",
#     "skills": ["sql", "python"],
#     "scores": {"math": 86, "english": 89, "science": 91},
#     "active": True,
#     "joined": "2024-05-10"
#   }
