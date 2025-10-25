================================Employee Performance Tracker================================


A Python console project to manage and analyze the performance of employees in an IT company.


Features:
-Store, add, and view employee details (name, department, hours worked, tasks completed, rating)
-Analyze overall averages and find the top performer
-Auto-select "Employee of the Month" based on performance and tasks
-Visualize productivity with quick charts (tasks completed vs rating)
-Export top performer data to a new CSV file


Project Structure:
employee_performance_tracker/
│
├── data/
│   └── employees.csv
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── employee.py
│   ├── storage.py
│   ├── analysis.py
│   ├── visualize.py
│
└── README.md


Setup:
-Install Python 3.7+
-Install requirements:
pip install pandas matplotlib
-Run the Project:
python -m src.main


Menu Options:
1: View all employees
2: Add new employee
3: Analyze performance and top performer
4: Show productivity chart
5: Show employee of the month
6: Export employee of the month to CSV
7: Exit


Example Data(employees.csv):
name,department,hours_worked,tasks_completed,rating
Amit,IT,46,15,5
Riya,HR,44,14,5
...


Bonus Features:
-Employee of the Month
-Easy data export for reports
-Clear productivity bar and line charts


Requirements:
-Python 3.7+
-pandas, matplotlib


