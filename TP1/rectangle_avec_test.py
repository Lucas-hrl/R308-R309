from point import Point

class Rectangle:
    def __init__(self,pointBasGauche:Point = Point(0,0),longueur:float = 1,hauteur:float = 1):
        if isinstance(pointBasGauche, Point):
            self.__pointBasGauche = pointBasGauche
        else:
            raise TypeError("mauvais type de valeur pour pointBasGauche")
        if hauteur < 0:
            raise ValueError("la hauteur ne peut pas être négative")
        if longueur < 0:
            raise ValueError("la longueur ne peut pas être négative")
        if isinstance(longueur,(int,float)):
            self.__longueur = longueur
        else:
            raise TypeError("mauvais type de valeur pour longueur")
        if isinstance(hauteur,(int,float)):
            self.__hauteur = hauteur
        else:
            raise TypeError("mauvais type de valeur pour hauteur")
    @property
    def pointBasGauche(self) -> Point:
        return self.__pointBasGauche

    @pointBasGauche.setter
    def pointBasGauche(self, pointBasGauche: Point):
        self.__pointBasGauche = pointBasGauche

    @property
    def longueur(self) -> float:
        return self.__longueur

    @longueur.setter
    def longueur(self, longueur: float):
        self.__longueur = longueur

    @property
    def hauteur(self) -> float:
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, hauteur: float):
        self.__hauteur = hauteur

    def __str__(self):
        return (f"Le rectangle a un point bas gauche a {self.__pointBasGauche}, "
                f"une longueur de {self.__longueur} cm et une hauteur de {self.__hauteur} cm")

    def surface(self):
        return self.__hauteur*self.__longueur

    def perimetre(self):
        return self.__hauteur*2 + self.__longueur*2

if __name__ == "__main__":
    try:
        rect1 = Rectangle(longueur=-8)
    except TypeError as e:
        print(e)
    except ValueError as ve:
        print(ve)
    else:
        print(rect1)

    try:
        rect1 = Rectangle("g")
    except TypeError as e:
        print(e)
    except ValueError as ve:
        print(ve)
    else:
        print(rect1)

    rect2 = Rectangle(longueur = 2, hauteur = 6)
    print(rect2)
    print(f"Le périmètre est {rect2.perimetre()} cm")
    print(f"la surface est  : {rect2.surface()}cm**2")
