num = input("Give me a number: ")

try:
    number = float(num)
    if number == int(number):
        print("The number is an integer")
    else:
        print("The number is a decimal")
except ValueError:
    print("That's not a valid number")
