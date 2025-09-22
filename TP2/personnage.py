class Personnage:
    def __init__(self,pseudo:str,niveau:int = 1,pv:int = 1,initiative:int = 1):
        if niveau != 1:
            initiative = niveau

        if isinstance(pseudo,str):
            self.__pseudo = pseudo
        else:
            raise TypeError("mauvais type de valeur pour le pseudo")

        if isinstance(niveau,int):
            self.__niveau = niveau
        else:
            raise TypeError("mauvais type de valeur pour le niveau")

        if isinstance(pv,int):
            self.__pv = pv
        else:
            raise TypeError("mauvais type de valeur pour le nombre de points de vie")

        if isinstance(initiative,int):
            self.__initiative = initiative
        else:
            raise TypeError("mauvais type de valeur pour l'initiative'")

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo: str):
        self.__pseudo = pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau: int):
        self.__niveau = niveau

    @property
    def pv(self) -> int:
        return self.__pv

    @pv.setter
    def pv(self, pv: int):
        self.__pv = pv

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative: int):
        self.__initiative = initiative

    def __str__(self):
        return f"Le personnage {self.__pseudo} est niveau {self.__niveau}, il a {self.__pv} points de vie et a une initiative de {self.__initiative}"


    def attaque(self,perso_adv):
        premier:bool = False
        if self.__initiative > perso_adv.initiative:
            premier = True
        elif self.__initiative == perso_adv.initiative:
            meme = True

        if meme:
            if self.__pv or perso_adv.pv >0:
                perso_adv.pv -= self.__niveau
                self.__pv -= perso_adv.niveau

        for i in range (2):
            if self.__pv or perso_adv.pv > 0:
                if premier:
                    perso_adv.pv -= self.__niveau
                    premier = False
                else:
                    self.__pv -= perso_adv.niveau
                    premier = True

        return (f"le perso {self.__pseudo} possede maintenant {self.__pv} points de vie, "
                f"le perso {perso_adv.pseudo} possede {perso_adv.pv} points de vie")

    def degats(self)->int:
        return self.__niveau




if __name__ == "__main__":
    try:
        perso1 = Personnage("toto")
    except TypeError as e:
        print(e)
    else:
        print(perso1)

    print(perso1.attaque(Personnage("titi")))