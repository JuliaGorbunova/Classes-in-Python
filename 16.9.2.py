class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height = height
    def display_circle(self):
        return str(f'Rectangle({self.width},{self.height})')

circle_1=Rectangle(6,8)
print(circle_1.display_circle())
