def is_prime(n):
    """Check if number is prime using functional approach."""
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

try:
    num = int(input("Enter a number: "))
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}.")
except ValueError:
    print("Invalid input. Enter a whole number.")
