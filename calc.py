# calculator

# ADD
def  add(n1, n2):
    return n1 + n2

# SUBTRACT
def subtract(n1, n2):
    return n1 - n2

# DIVIDE
def divide(n1, n2):
    return n1 / n2

# MULTIPLY
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True  

    while should_continue:
        operations_symbol = input("Pick an opeartion: ")  
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()                




