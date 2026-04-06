import operator

# Map operator symbols to their corresponding functions
OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calculate(n1, op, n2):
    """Performs arithmetic using the OPS dictionary; raises error for invalid ops."""
    if op not in OPS: raise ValueError(f"Unsupported operator: {op}")
    return OPS[op](n1, n2)

print("--- Simple CLI Calculator (Type 'exit' to quit) ---")
while True:
    val = input("\nEnter (e.g. 10 + 5): ").strip()
    if val.lower() == 'exit': break
    try:
        # Split and unpack the input string
        n1_str, op, n2_str = val.split()
        res = calculate(float(n1_str), op, float(n2_str))
        print(f"Result: {res}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except (ValueError, IndexError):
        print("Error: Use format <num> <op> <num> with valid numbers.")
