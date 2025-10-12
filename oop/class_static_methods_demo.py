"""
Module: class_static_methods_demo
Description: Illustrates the difference between class and static methods using a Calculator class.
"""

class Calculator:
    """A simple calculator demonstrating class and static methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers and show the class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


if __name__ == "__main__":
    # Example usage (manual test)
    print("The sum is:", Calculator.add(10, 5))
    print("The product is:", Calculator.multiply(10, 5))
