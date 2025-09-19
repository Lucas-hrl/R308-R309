from point import Point
import math
from typing import Union

class Cercle:
    def __init__(self,rayon:float,centre:Point = Point(0,0)):
        if isinstance(centre,Point):
            self.__centre = centre
        else:
            raise TypeError("mauvais type de valeur pour centre")
        if isinstance(rayon, (float, int)):
            self.__rayon = rayon
        else:
            raise TypeError("mauvais type de valeur pour le rayon")
        if rayon < 0:
            raise ValueError("le rayon ne peut pas être négatif")


    def __str__(self):
        return f"Cercle de rayon {self.__rayon} et de centre {self.__centre}"

    @property
    def centre(self) -> Point:
        return self.__centre

    @centre.setter
    def centre(self, centre: Point):
        if not isinstance(centre, Point):
            raise TypeError("Le centre doit être un objet Point")
        self.__centre = centre

    @property
    def rayon(self) -> float:
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon: float):
        if not isinstance(rayon, (int, float)):
            raise TypeError("Le rayon doit être un nombre (int ou float)")
        if rayon < 0:
            raise ValueError("Le rayon ne peut pas être négatif")
        self.__rayon = rayon

    def diametre(self)-> float:
        return self.__rayon*2

    def perimetre(self)->float:
        return self.diametre()*math.pi

    def surface(self)->float:
        return math.pi * self.__rayon**2



if __name__ == "__main__":
    try:
        cercle1 = Cercle(-5)
    except TypeError as e:
        print(e)
    except ValueError as ve:
        print(ve)
    else:
        print(cercle1)



    #print(vars(cercle1))
    #print(cercle1.diametre())
    #print(cercle1.perimetre())
    #print(cercle1.surface())