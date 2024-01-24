x = int(input("enter your number:"))
for i in range (2,x):
    if x % i == 0:
        print("the number is not a prime number")
        break
    else :
        print("number is prime") 
        break   
