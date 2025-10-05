# robust_division_calculator.py

def safe_divide(numerator, denominator) -> str:
    """
    Attempt to divide numerator by denominator.
    Returns a user-friendly string indicating the result or an error message.
    """
    try:
        n = float(numerator)
        d = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."
    try:
        result = n / d
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of the division is {result}"
