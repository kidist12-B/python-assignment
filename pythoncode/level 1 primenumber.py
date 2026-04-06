import math

def is_prime(n: int) -> bool:
    """Check if a number is prime using a functional approach."""
    if n <= 1:
        return False
    # We only need to check up to the square root of n
    limit = int(math.sqrt(n)) + 1
    return all(n % i != 0 for i in range(2, limit))

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check: "))
        result = "prime" if is_prime(num) else "not prime"
        print(f"{num} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
