employees_file = open("employees.txt", "r")
print(employees_file.readlines()[3])
employees_file.close()