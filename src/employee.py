class Employee:
    def __init__(self, name, department, hours_worked, tasks_completed, rating):
        self.name = name
        self.department = department
        self.hours_worked = float(hours_worked)
        self.tasks_completed = int(tasks_completed)
        self.rating = float(rating)

    def __str__(self):
        return f"{self.name} | {self.department} | Hours: {self.hours_worked} | Tasks: {self.tasks_completed} | Rating: {self.rating}"

    def to_dict(self):
        return {
            "name": self.name,
            "department": self.department,
            "hours_worked": self.hours_worked,
            "tasks_completed": self.tasks_completed,
            "rating": self.rating
        }
