class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def display_circle(self):
        return str(f'Circle({self.x},{self.y},{self.r})')

circle_1=Circle(3,4,5)
print(circle_1.display_circle())



