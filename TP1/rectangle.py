from point import Point

class Rectangle:
    def __init__(self,pointBasGauche:Point = Point(0,0),longueur:float = 1,hauteur:float = 1):
        self.__pointBasGauche = pointBasGauche
        self.__longueur = longueur
        self.__hauteur = hauteur

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


if __name__ == "__main__":
    rect1 = Rectangle()
    print(rect1)