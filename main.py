"""
JSON CRUD Starter
-----------------
Use the provided students.json as your data store.
Implement the CRUD helpers below. Keep functions small and testable.

Tips / Best Practices:
- Always use `with open(...)` (context managers).
- Prefer pathlib.Path for paths.
- Validate data before writing (e.g., unique `id`).
- Write atomically: write to a temp file, then replace the original.
- Keep pure functions where possible.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json
import tempfile
import os

DB_PATH = "data/students.json"

# ---------- I/O Utilities ----------
def load_db():
    """Load the JSON list from disk. Return [] if file missing or empty."""
    # TODO: implement
    # Reading JSON file
    with open(DB_PATH, "r") as file:
        data = json.load(file)
    return data    

def atomic_write_json(data: Any, path: Path = DB_PATH) -> None:
    """Write JSON atomically: write to temp file, then replace."""
    # TODO: implement
    raise NotImplementedError

def save_db(records: List[Dict[str, Any]], path: Path = DB_PATH) -> None:
    """Persist the full list of records to disk using atomic write."""
    # TODO: implement
    raise NotImplementedError

# ---------- CRUD ----------
def list_all() -> List[Dict[str, Any]]:
    """Return all student records."""
    # TODO: implement
    raise NotImplementedError

def get_by_id(student_id: int):
    """Return a single student by id or None if not found."""
    # TODO: implement
    students =load_db()
    for student in students:
        if student['id'] == student_id:
            return student
    raise NotImplementedError

def create_student(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Insert a new student.
    Requirements:
      - `id` must be unique (raise ValueError if duplicate)
      - Required keys: id, name, age, city, skills, scores, active, joined
    """
    # TODO: implement
    raise NotImplementedError

def update_student(student_id: int, updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update fields for a student by id.
    Example updates:
      - {"city": "Bhopal"}
      - {"scores": {"math": 90}}  (merge dicts, don't overwrite other score fields)
      - {"skills": ["python", "sql", "git"]}
    Raise KeyError if student not found.
    """
    # TODO: implement
    raise NotImplementedError

def delete_student(student_id: int) -> Dict[str, Any]:
    """Delete a student by id. Return the deleted record. Raise KeyError if not found."""
    # TODO: implement
    raise NotImplementedError

# ---------- Queries & Utilities ----------
def find_by_city(city: str) -> List[Dict[str, Any]]:
    """Return all students from a city (case-insensitive match)."""
    # TODO: implement
    raise NotImplementedError

def top_scorers(subject: str, n: int = 3) -> List[Tuple[str, int]]:
    """
    Return top N (name, score) tuples for a given subject: 'math' | 'english' | 'science'.
    Ignore students where the subject is missing.
    """
    # TODO: implement
    raise NotImplementedError

def average_score(subject: str) -> float:
    """Compute average score for a subject across all active students. Round to 2 decimals."""
    # TODO: implement
    raise NotImplementedError

def add_skill(student_id: int, skill: str) -> Dict[str, Any]:
    """Add a skill to a student's skills list (avoid duplicates)."""
    # TODO: implement
    raise NotImplementedError

# ---------- Demo ----------
if __name__ == "__main__":
    print("Total records:", len(load_db()))
    print("Student 101:", get_by_id(101))
