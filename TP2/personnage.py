class Personnage:
    def __init__(self,pseudo:str,niveau:int = 1,nbr_points_vie:int = 1,initiative:int = 1):
        if isinstance(pseudo,str):
            self.__pseudo = pseudo
        else:
            raise TypeError("mauvais type de valeur pour le pseudo")

        if isinstance(niveau,int):
            self.__niveau = niveau
        else:
            raise TypeError("mauvais type de valeur pour le niveau")

        if isinstance(nbr_points_vie,int):
            self.__nbr_points_vie = nbr_points_vie
        else:
            raise TypeError("mauvais type de valeur pour le nombre de points de vie")

        if isinstance(initiative,int):
            self.__initiative = initiative
        else:
            raise TypeError("mauvais type de valeur pour l'initiative'")

