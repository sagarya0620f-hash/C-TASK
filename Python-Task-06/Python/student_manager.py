import os

FILE = "students.txt"
scores = []

def add_student():
    name = input("Student Name: ")
    sid = input("Student ID: ")
    branch = input("Branch: ")
    email = input("Email: ")

    with open(FILE, "a") as f:
        f.write(f"{sid},{name},{branch},{email}\n")

    print("Student Added Successfully!\n")


def view_students():
    if not os.path.exists(FILE):
        print("No Records Found.\n")
        return

    with open(FILE, "r") as f:
        data = f.readlines()

    if not data:
        print("No Records Found.\n")
        return

    print("\n----- Student Records -----")
    for line in data:
        sid, name, branch, email = line.strip().split(",")
        print(f"ID: {sid}")
        print(f"Name: {name}")
        print(f"Branch: {branch}")
        print(f"Email: {email}")
        print("-------------------------")
    print()


def search_student():
    key = input("Enter Student ID or Name: ")

    if not os.path.exists(FILE):
        print("No Records Found.\n")
        return

    found = False
    with open(FILE, "r") as f:
        for line in f:
            sid, name, branch, email = line.strip().split(",")
            if key == sid or key.lower() == name.lower():
                print("\nRecord Found")
                print(f"ID: {sid}")
                print(f"Name: {name}")
                print(f"Branch: {branch}")
                print(f"Email: {email}\n")
                found = True

    if not found:
        print("Record Not Found.\n")


def delete_student():
    if not os.path.exists(FILE):
        print("No Records Found.\n")
        return

    sid = input("Enter Student ID to Delete: ")

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        deleted = False
        for line in lines:
            if line.startswith(sid + ","):
                deleted = True
                continue
            f.write(line)

    if deleted:
        print("Student Deleted Successfully.\n")
    else:
        print("Record Not Found.\n")


def security_assessment():
    score = 0

    if input("Is MFA Enabled? (y/n): ").lower() == "y":
        score += 25

    if int(input("Password Length: ")) >= 8:
        score += 25

    if input("System Updated? (y/n): ").lower() == "y":
        score += 25

    if input("Antivirus Installed? (y/n): ").lower() == "y":
        score += 25

    scores.append(score)

    print(f"\nSecurity Score: {score}/100")

    if score >= 90:
        print("Status: Excellent\n")
    elif score >= 70:
        print("Status: Good\n")
    elif score >= 50:
        print("Status: Moderate\n")
    else:
        print("Status: Poor\n")


def generate_report():
    total = 0

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            total = len(f.readlines())

    avg = sum(scores) / len(scores) if scores else 0
    poor = sum(1 for s in scores if s < 50)

    print("\n====== REPORT ======")
    print("Total Students:", total)
    print("Security Scores:", scores)
    print("Average Security Score:", round(avg, 2))
    print("Students with Poor Security Ratings:", poor)
    print("====================\n")


while True:
    print("===================================")
    print(" Student Cyber Security Manager")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Security Assessment")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        security_assessment()
    elif choice == "6":
        generate_report()
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice\n")