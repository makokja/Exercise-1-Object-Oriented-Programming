import math
pi = math.pi 

class Circle: 
#init function
    def __init__(self,radius):
        self.radius = radius

#first method 
    def area(self):
        a = pi*self.radius*self.radius
        return a

#second method
    def perimeter(self):
        p = 2*pi*self.radius
        return p

cir = Circle(float(input("Enter Radius: ")))  #create the object and getting the user input
area = cir.area()  #get the area by calling function area
peri = cir.perimeter()  #get the paramiter by calling function perimeter
# print out the result with 2 decimal point
print("Area: ", round(area,2)) 
print("Perimiter: ", round(peri,2))