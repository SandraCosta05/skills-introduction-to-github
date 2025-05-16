# Function to generate random numbers between 1 and 100
import random

def generate_random_numbers(n):
    """
    Generate a list of n random numbers between 1 and 100.
    
    Args:
    n (int): The number of random numbers to generate.
    
    Returns:
    list: A list of n random numbers between 1 and 100.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The input must be a positive integer.")
    return [random.randint(1, 100) for _ in range(n)]

if __name__ == "__main__":
    n = 10  # Specify the number of random numbers you want to generate
    try:
        random_numbers = generate_random_numbers(n)
        print(random_numbers)
    except ValueError as e:
        print(f"Error: {e}")


