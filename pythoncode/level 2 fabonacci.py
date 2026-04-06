def generate_fibonacci(n: int):
    """
    A generator function that yields the first n terms 
    of the Fibonacci sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    try:
        count = int(input("How many Fibonacci terms would you like to generate? "))
        
        if count <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            # Converting generator to list for display
            sequence = list(generate_fibonacci(count))
            # Joining list into a string for cleaner output
            print(f"Fibonacci sequence ({count} terms): {', '.join(map(str, sequence))}")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")
