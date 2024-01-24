# ask the user for a number
number = int(input("Enter your number: "))

if number % 2 == 0:
    print("Your number is even")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")        

else:
    print("This is an odd number")    