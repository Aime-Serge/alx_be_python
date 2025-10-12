# oop/class_static_methods_demo.py
"""
Module: class_static_methods_demo
Description: Illustrates the difference between class and static methods using a Calculator class.
"""

class Calculator:
    """
    A simple calculator demonstrating class and static methods.

    Class Attributes:
        calculation_type (str): A description of the type of calculation.
    """

    calculation_type: str = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: Sum of the two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Multiply two numbers and display the class-level attribute.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: Product of the two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
