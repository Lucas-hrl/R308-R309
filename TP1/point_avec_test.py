from typing import Union
class Point:
    def __init__(self,x:float = 0.0,y:float = 0.0):
        if isinstance(x,Union[float,int]):
            self.__x = x
        else:
            raise TypeError("mauvais type de valeur pour x")

        if isinstance(y,Union[float,int]):
            self.__y = y
        else:
            raise TypeError("mauvais type de valeur pour y")

    def __str__(self):
        return f"Le point a pour coordonnées ({self.__x},{self.__y})"

if __name__ == "__main__":
    #x = input("Saisir l'abscisse : ")
    #y = input("Saisir l'ordonnée : ")
    try:
        p = Point(12,4)
    except TypeError as e:
        print(e)
    else:
        print(p)