from abc import ABC, abstractmethod

# Interface for shapes (Abstract Class)
class Shape(ABC):
    """
    This abstract class defines the interface for shapes.
    It specifies the methods that all shapes must implement
    to calculate their area and perimeter.
    """

    @abstractmethod
    def calculate_area(self):
        """
        This method calculates the area of the shape.
        Derived classes must implement this method specific to their shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """
        This method calculates the perimeter of the shape.
        Derived classes must implement this method specific to their shape.
        """
        pass

# Concrete class representing a Rectangle
class Rectangle(Shape):
    """
    This class represents a rectangle and inherits from the Shape interface.
    It implements the calculate_area and calculate_perimeter methods specific to rectangles.
    """

    def __init__(self, length, width):
        """
        This constructor initializes the rectangle with its length and width.
        """
        self.length = length
        self.width = width

    def calculate_area(self):
        """
        This method calculates the area of the rectangle using its length and width.
        """
        return self.length * self.width

    def calculate_perimeter(self):
        """
        This method calculates the perimeter of the rectangle by adding twice the length and width.
        """
        return 2 * (self.length + self.width)

# Example usage
rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Area of rectangle: {area}")
print(f"Perimeter of rectangle: {perimeter}")
