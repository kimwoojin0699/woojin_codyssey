def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def evaluate_expression(expr):
    try:
        bonus = expr.strip().split()
        if len(bonus) != 3:
            return "Invalid input format."
        
        a = int(bonus[0])
        op = bonus[1]
        b = int(bonus[2])

        if op == "+":
            return add(a, b)
        elif op == "-":
            return subtract(a, b)
        elif op == "*":
            return multiply(a, b)
        elif op == "/":
            return divide(a, b)
        else:
            return "Invalid operator."
    except ValueError:
        return "Invalid input. Please enter integers."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Select mode:")
    print("1.calculator")
    print("2.bonus")
    mode = input("Choose mode (1 or 2): ")

    if mode == "1":
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            op = input("Enter the operator (+, -, *, /): ")

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                result = "Invalid operator."

            print("Result:", result)

        except ValueError:
            print("Invalid input.")

    elif mode == "2":
        expr = input("Enter expression: ")
        result = evaluate_expression(expr)
        print("Result:", result)
    else:
        print("Invalid mode selected.")
