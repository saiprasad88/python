try:

    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError:
    print("divided by error")
except ValueError:
    print("invalid input")