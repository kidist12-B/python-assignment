def calculate(num1, operator, num2):
    """
    Performs basic arithmetic operations.
    Supports: +, -, *, /
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        # If the operator isn't recognized, raise an error
        raise ValueError("Unsupported operator.")

print("--- Simple CLI Calculator ---")
print("Type 'exit' at any time to close.")

while True:
    user_input = input("\nEnter expression (e.g., 10 + 5): ").strip()
    
    if user_input.lower() == 'exit':
        print("Closing calculator...")
        break

    try:
        # Split input into three parts: number, operator, number
        parts = user_input.split()
        if len(parts) != 3:
            print("Error: Format must be <num1> <op> <num2>")
            continue

        n1 = float(parts[0])
        op = parts[1]
        n2 = float(parts[2])

        # Call the calculation function
        result = calculate(n1, op, n2)
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError as e:
        print(f"Error: {e if 'Unsupported' in str(e) else 'Please enter valid numbers.'}")
