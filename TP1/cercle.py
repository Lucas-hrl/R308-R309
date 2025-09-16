from point import Point
import math

class Cercle:
    def __init__(self,rayon:float,centre:Point = Point(0,0)):
        self.__centre = centre
        self.__rayon = rayon

    def __str__(self):
        return f"Cercle de rayon {self.__rayon} et de centre {self.__centre}"

    @property
    def centre(self) -> Point:
        return self.__centre

    @centre.setter
    def centre(self, centre: Point):
        self.__centre = centre

    @property
    def rayon(self) -> float:
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon: float):
        self.__rayon = rayon

    def diametre(self)-> float:
        return self.__rayon*2

    def perimetre(self)->float:
        return self.diametre()*math.pi

    def surface(self)->float:
        return math.pi * self.__rayon**2



if __name__ == "__main__":
    cercle1= Cercle(3)
    print(vars(cercle1))
    print(cercle1)
    print(cercle1.diametre())
    print(cercle1.perimetre())
    print(cercle1.surface())