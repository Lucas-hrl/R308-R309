from point import Point

class Rectangle:
    def __init__(self,pointBasGauche:Point = Point(0,0),longueur:float = 1,hauteur:float = 1):
        self.__pointBasGauche = pointBasGauche
        self.__longueur = longueur
        self.__hauteur = hauteur