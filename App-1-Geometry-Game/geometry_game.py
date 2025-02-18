from random import randint
import turtle


class Point:
    """Class representing a point in space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    """Class representing a rectangle in space"""
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    """Class representing an object capable of drawing a rectangle"""
    def draw(self, canvas):
        # Start at a different coordinate than 0, 0
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        # Draw the rectangle
        canvas.pendown()
        canvas.forward(self.point1.x - self.point2.x)
        canvas.left(90)
        canvas.forward(self.point1.y - self.point2.y)
        canvas.left(90)
        canvas.forward(self.point1.x - self.point2.x)
        canvas.left(90)
        canvas.forward(self.point1.y - self.point2.y)


class GuiPoint(Point):
    """Class representing an object capable of drawing a point"""
    def draw(self, canvas, size: int = 5, color: str = "red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                         Point(randint(10, 400), randint(10, 400)))
canvas = turtle.Turtle()

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
rectangle.draw(canvas)
user_point.draw(canvas)

turtle.done()
