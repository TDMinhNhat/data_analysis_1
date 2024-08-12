class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width): 
        if width < 0:
            self.width = 0
        else:
            self.width = width

    def set_height(self, height):
        if height < 0:
            self.height = 0
        else:
            self.height = height

    def calcArea(self):
        return (self.width * self.height)

    def calcPerimeter(self):
        return (2 * (self.width + self.height))
    
    def display(self):
        print(f"Width: {self.width}, Height: {self.height}, Area: {self.calcArea()}, Perimeter: {self.calcPerimeter()}")

