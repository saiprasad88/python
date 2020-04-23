employees_file = open("employees", "r")
print(employees_file.readline()[1])
employees_file.close()