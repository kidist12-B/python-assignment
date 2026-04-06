import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

print("CLI Calculator | Type 'exit' to quit")

while True:
    try:
        expr = input("Enter <num1> <op> <num2> > ").strip()
        if expr.lower() == "exit":
            break
        
        n1, op, n2 = expr.split()
        result = OPS[op](float(n1), float(n2))
        print(f"Result: {result}\n")
    except (ValueError, KeyError, ZeroDivisionError):
        print("Error: Invalid input. Use format: <number> <op> <number>\n")
