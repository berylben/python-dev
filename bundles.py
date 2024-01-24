data = int(input("Enter data you want to purchase: "))

credo = data / 10

CredoBalance = int(input("Enter airtime balance: "))

if CredoBalance >= credo:
    print("You have successfuly purchased your mbs.")
else:
    print("Insufficient balance.")