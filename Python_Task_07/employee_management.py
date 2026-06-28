import csv


class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = float(salary)


employees = []


def add_employee():
    print("\n===== Add Employee =====")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(emp_id, name, department, designation, salary)
    employees.append(employee)

    print("\nEmployee Added Successfully!")


def view_employees():
    if len(employees) == 0:
        print("\nNo Employee Records Found.")
        return

    print("\n" + "-" * 75)
    print(f"{'ID':<10}{'Name':<20}{'Department':<15}{'Designation':<15}{'Salary'}")
    print("-" * 75)

    for emp in employees:
        print(
            f"{emp.emp_id:<10}"
            f"{emp.name:<20}"
            f"{emp.department:<15}"
            f"{emp.designation:<15}"
            f"{emp.salary}"
        )


def search_employee():
    print("\n1. Search by Employee ID")
    print("2. Search by Employee Name")

    choice = input("Enter Choice: ")

    found = False

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        for emp in employees:
            if emp.emp_id == emp_id:
                print("\nEmployee Found")
                print(vars(emp))
                found = True
                break

    elif choice == "2":
        name = input("Enter Employee Name: ").lower()

        for emp in employees:
            if emp.name.lower() == name:
                print("\nEmployee Found")
                print(vars(emp))
                found = True
                break

    if not found:
        print("Employee Not Found")


def update_employee():
    emp_id = input("Enter Employee ID to Update: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            emp.department = input("New Department: ")
            emp.designation = input("New Designation: ")
            emp.salary = float(input("New Salary: "))

            print("Employee Updated Successfully!")
            return

    print("Employee Not Found")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found")


def salary_statistics():
    if len(employees) == 0:
        print("No Employee Records Found.")
        return

    salaries = [emp.salary for emp in employees]

    print("\n===== Salary Statistics =====")
    print("Highest Salary :", max(salaries))
    print("Lowest Salary  :", min(salaries))
    print("Average Salary :", sum(salaries) / len(salaries))
    print("Total Employees:", len(employees))
def export_csv():
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Employee ID", "Name", "Department", "Designation", "Salary"]
        )

        for emp in employees:
            writer.writerow(
                [
                    emp.emp_id,
                    emp.name,
                    emp.department,
                    emp.designation,
                    emp.salary,
                ]
            )

    print("Employee Data Exported Successfully!")


def read_csv():
    try:
        with open("employees.csv", "r") as file:
            print("\n===== Employee Records from CSV =====")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("employees.csv not found.")


def department_count():
    if len(employees) == 0:
        print("No Employee Records Found.")
        return

    departments = {}

    for emp in employees:
        departments[emp.department] = departments.get(emp.department, 0) + 1

    print("\nDepartment-wise Employee Count")

    for dept, count in departments.items():
        print(dept, ":", count)


def sort_salary():
    if len(employees) == 0:
        print("No Employee Records Found.")
        return

    sorted_list = sorted(employees, key=lambda x: x.salary)

    print("\nEmployees Sorted by Salary")

    for emp in sorted_list:
        print(emp.emp_id, emp.name, emp.salary)


while True:

    print("\n========== Employee Management System ==========")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Salary Statistics")
    print("7. Export to CSV")
    print("8. Read CSV")
    print("9. Department-wise Employee Count")
    print("10. Sort Employees by Salary")
    print("11. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        salary_statistics()

    elif choice == "7":
        export_csv()

    elif choice == "8":
        read_csv()

    elif choice == "9":
        department_count()

    elif choice == "10":
        sort_salary()

    elif choice == "11":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")