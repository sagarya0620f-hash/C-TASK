password = "admin123"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access Granted")
        break

    attempts += 1
    print("Incorrect Password")

if attempts == 3:
    print("Account Locked")