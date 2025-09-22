from personnage import Personnage

"""
    La classe Guerrier hérite de Personnage.
    Ses points de vie et son initiative sont calculés automatiquement
    en fonction de son niveau.
    """
class Guerrier(Personnage):
    def __init__(self,pseudo:str,niveau:int = 1):
        pv = niveau * 8 + 4
        initiative = niveau * 4 + 6
        super().__init__(pseudo,niveau,pv,initiative)





if __name__ == "__main__":
    guerrier1 = Guerrier("ivan")
    print(guerrier1)