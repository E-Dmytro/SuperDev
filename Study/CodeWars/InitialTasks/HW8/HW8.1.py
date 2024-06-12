class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides= [float(input(f"Enter side {str(i+1)}:"))
                     for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class findAreaRect(Polygon):
    def __init__(self):
                super().__init__(2) # Polygon.__init__(self,2)

    def findAreaRect(self):
        a, b = self.sides
        area= a * b
        print(f"The area of the rectangle is {round(area,0)}")

r=findAreaRect()
r.inputSides()
r.dispSides()
r.findAreaRect()




#Triangle (example)

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)
#
#     def findArea(self):
#         a,b,c = self.sides
#         #calculate the semi-perimeter
#         s=(a+b+c)/2
#         area = (s*(s-a)*(s-b)*(s-c))**0.5
#         print(f"The area of the triangle is {area}")