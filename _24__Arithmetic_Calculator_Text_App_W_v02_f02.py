# calculator:

print("Welcome to a calculator text based app.")

# add:
def add(n1, n2):
    return n1 + n2

# subtract:
def subtract(n1, n2):
    return n1 - n2

# multiply:
def multiply(n1, n2):
    return n1 * n2

# divide:
def divide(n1, n2):
    return n1 / n2

# dictionary of operations:
operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}

# function to perform calculation:
def calculator():
    num1 = float(input("What is the first number you'd like to use?: "))

    for symbol in operations:
        print(symbol)

    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{int(num1)} {operation_symbol} {int(num2)} = {int(answer)}")

        if input("Do you want to do another calculation with the last answer? (Y or N): ").lower() == "y":
            num1 = answer
        else:
            continue_calculation = False
            if input("Start a new calculation? (Y or N): ").lower() == "y":
                calculator()

calculator()
