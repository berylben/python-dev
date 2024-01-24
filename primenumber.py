# TODO: take integer input from the user
x = int(input("enter number:"))

isPrime = True

# TODO : loop through to x - 1
for i in range(2, x):
    #TODO : check whether x is divisible by any number from 2 -> x -1
    
    if x % i == 0:
    
        isPrime = False
        break


if isPrime == True:
    print("it is a prime number")
else:
    print("It is not a prime number")
