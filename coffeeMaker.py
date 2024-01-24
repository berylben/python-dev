MENU = {
    "expppresso": {
        "ingridients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingridients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingridients": {
            "water": 250,
            "milk": 100,
            "cofee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee":100,
}

def is_resourse_sufficient(order_ingridient):
    """returns True when order can be made, false if ingridients are insufficient"""
    is_enough = True
    for item in order_ingridient:
        if order_ingridient[item ] >=     resources[item]:
            print(f"Sorry, there is not enough{item}")
            is_enough = False
    return is_enough

def process_coins():
    """returns total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quaters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How mant pennies: ")) * 0.01
    return total 

def is_transaction_successful(money_received, drink_cost):
    """returns true if payement is accepted , returns true if payement is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change}in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money, money refunded")
        return False
    
def make_coffee(drink_name, order_ingridient):
     """deduct required ingridients from resources"""
     for item in order_ingridient:
         resources[item] -= order_ingridient[item]
     print(f"here is your {drink_name}")  
     


     

is_on = True

while True:
    choice = input("What whould you like?(expresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
           drink = MENU[choice]
           if is_resourse_sufficient(drink["ingridents"]):
               payement = process_coins()
               if is_transaction_successful(payement, drink["cost"]):
                   make_coffee(choice, drink["ingridents"])
                   
