logs = ["Success","Failed","Failed","Success","Failed","Success"]

success = logs.count("Success")
failed = logs.count("Failed")

print("Total Attempts:",len(logs))
print("Successful Logins:",success)
print("Failed Logins:",failed)

print("\nImportance:")
print("Monitoring failed logins helps detect brute-force attacks and unauthorized access attempts.")