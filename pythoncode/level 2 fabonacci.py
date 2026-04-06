def fibonacci(n):
    """Generate Fibonacci sequence using generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

try:
    count = int(input("Enter number of terms: "))
    print(f"Fibonacci sequence: {list(fibonacci(count))}")
except ValueError:
    print("Invalid input. Enter a positive integer.")
