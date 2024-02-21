def factorial(n):
    if n == 0:  # Base case: When n equals 0
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call to create nested folders

# Example usage:
print(factorial(5))  # Output: 120

def fibonacci(n):
    if n <= 1:  # Base case: When n is less than or equal to 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call to add up documents

# Example usage:
print(fibonacci(6))  # Output: 8