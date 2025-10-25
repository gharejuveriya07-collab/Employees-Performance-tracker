import matplotlib.pyplot as plt

def plot_performance(employees):
    if not employees:
        print("No employees to show.")
        return
    names = [e.name for e in employees]
    tasks = [e.tasks_completed for e in employees]
    ratings = [e.rating for e in employees]

    plt.bar(names, tasks, label="Tasks Completed")
    plt.plot(names, ratings, marker="o", color="r", label="Rating")
    plt.title("Employee Performance")
    plt.xlabel("Employee")
    plt.ylabel("Tasks / Rating")
    plt.legend()
    plt.tight_layout()
    plt.show()
