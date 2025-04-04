def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):
        return num % divisor == 0
    else:
        return False  # Ensure both num and divisor are numeric.

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
print(check_divisibility(10, 2))  # True, because 10 is divisible by 2
print(check_divisibility(7, 3))   # False, because 7 is not divisible by 3
