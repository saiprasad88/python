try:
    value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError:
    print("divided by error")
except ValueError:
    print("invalid input")