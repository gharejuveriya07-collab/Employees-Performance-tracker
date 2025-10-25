from statistics import mean

def average_rating(employees):
    return mean(e.rating for e in employees) if employees else 0

def top_performer_by_rating(employees):
    return max(employees, key=lambda e: e.rating) if employees else None

def employee_of_month(employees):
    if not employees:
        return None
    max_tasks = max(e.tasks_completed for e in employees)
    return max(employees, key=lambda e: (e.rating * 0.7) + (e.tasks_completed / max_tasks) * 0.3)
