website = input("Enter Website Name: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

with open("vault.txt", "a") as file:
    file.write(f"Website: {website}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n")
    file.write("-" * 30 + "\n")

print("\nRecord Saved Successfully\n")

with open("vault.txt", "r") as file:
    print(file.read())