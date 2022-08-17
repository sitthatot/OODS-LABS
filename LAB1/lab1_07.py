import math
class Spherical:

    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        volume = (4/3) * math.pi * pow(self.radius,3)
        return volume

    def findArea(self):
        area = 4 * math.pi * pow(self.radius,2)
        return area

    def __str__(self):
        return "Radius =%d Volumn = %s Area = %s"%(self.radius, str(R1.findVolume()),str(R1.findArea()))


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
