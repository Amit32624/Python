class Triangle:

    def __init__(self,base,height):
        self.base=base
        self.height=height


    def area(self):
        return (.5 * self.base * self.height)


    def __add__(self, anothertriangle):
          return Triangle(self.base+anothertriangle.base,self.height+anothertriangle.height)




t1=Triangle(4,4)
print("Triangel's T1 Area ",t1.area())


t2=Triangle(6,6)
print("Triangel's T2 Area ",t2.area())

t3=t1+t2
print("Sum of area of both the triangles is :",t3.area())
