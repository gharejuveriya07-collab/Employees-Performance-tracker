import csv
from pathlib import Path
from src.employee import Employee

FILE_PATH = Path(__file__).resolve().parents[1] / "data" / "employees.csv"
FIELDNAMES = ["name", "department", "hours_worked", "tasks_completed", "rating"]

def load_employees():
    employees = []
    with FILE_PATH.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append(Employee(**row))
    return employees

def add_employee(emp):
    with FILE_PATH.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(emp.to_dict())

def export_top_performers(employees, path):
    avg = sum(e.rating for e in employees) / len(employees) if employees else 0
    top = [e for e in employees if e.rating >= avg]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for e in top:
            writer.writerow(e.to_dict())
    return len(top)
