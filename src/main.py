import argparse
from src.storage import load_employees, add_employee, export_top_performers
from src.employee import Employee
from src.analysis import average_rating, top_performer_by_rating, employee_of_month
from src.visualize import plot_performance

def interactive_menu():
    employees = load_employees()
    print(f"Loaded {len(employees)} employees.\n")

    while True:
        print("1. Show employees")
        print("2. Add employee")
        print("3. Analyze performance")
        print("4. Visualize performance")
        print("5. Employee of the Month")
        print("6. Export top performers")
        print("0. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            for e in employees: print(e)
        elif choice == "2":
            n = input("Name: "); d = input("Dept: ")
            h = float(input("Hours: ")); t = int(input("Tasks: ")); r = float(input("Rating: "))
            emp = Employee(n, d, h, t, r); add_employee(emp); employees.append(emp)
            print("✅ Added.")
        elif choice == "3":
            print(f"Avg Rating: {average_rating(employees):.2f}")
            print("Top Performer:", top_performer_by_rating(employees))
        elif choice == "4":
            plot_performance(employees)
        elif choice == "5":
            print("🏆 Employee of the Month:", employee_of_month(employees))
        elif choice == "6":
            export_top_performers(employees, "data/top_performers.csv")
            print("✅ Exported to data/top_performers.csv")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def cli_mode(args):
    employees = load_employees()
    if args.show:
        for e in employees: print(e)
    if args.add:
        n, d, h, t, r = args.add
        emp = Employee(n, d, float(h), int(t), float(r))
        add_employee(emp); print("✅ Added:", emp)
    if args.analyze:
        print(f"Avg Rating: {average_rating(employees):.2f}")
        print("Top:", top_performer_by_rating(employees))
    if args.visualize:
        plot_performance(employees)
    if args.month:
        print("🏆 Employee of the Month:", employee_of_month(employees))
    if args.export:
        export_top_performers(employees, args.export)
        print(f"✅ Exported to {args.export}")

def main():
    parser = argparse.ArgumentParser(description="Employee Performance Analyzer")
    parser.add_argument("--show", action="store_true", help="Show employees")
    parser.add_argument("--add", nargs=5, metavar=("NAME","DEPT","HOURS","TASKS","RATING"))
    parser.add_argument("--analyze", action="store_true", help="Show analysis")
    parser.add_argument("--visualize", action="store_true", help="Show chart")
    parser.add_argument("--month", action="store_true", help="Employee of the Month")
    parser.add_argument("--export", metavar="PATH", help="Export top performers")
    args = parser.parse_args()

    if not any(vars(args).values()):
        interactive_menu()
    else:
        cli_mode(args)

if __name__ == "__main__":
    main()
