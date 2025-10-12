# oop/polymorphism_demo.py
"""
Module: polymorphism_demo
Description: Demonstrates polymorphism and method overriding using Shape subclasses.
"""

import math

class Shape:
    """
    Base class representing a generic shape.
    """

    def area(self) -> float:
        """
        Calculate the area of the shape.

        Raises:
            NotImplementedError: If subclass does not override this method.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.
    """

    def __init__(self, length: float, width: float) -> None:
        """
        Initialize a Rectangle instance.

        Args:
            length (float): Length of the rectangle.
            width (float): Width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate and return the rectangle's area."""
        return self.length * self.width


class Circle(Shape):
    """
    Represents a circle shape.

    Attributes:
        radius (float): Radius of the circle.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle instance.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """Calculate and return the circle's area."""
        return math.pi * (self.radius ** 2)
