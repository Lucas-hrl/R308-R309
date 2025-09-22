from personnage import Personnage

class Mage(Personnage):
    def __init__(self,pseudo:str,niveau:int = 1):
        pv = niveau * 5 + 10
        initiative = niveau *6 + 4
        mana = niveau * 5
        super().__init__(pseudo,niveau,pv,initiative)
        self.__mana = mana

    @property
    def mana(self) -> int:
        return self.__mana

    @mana.setter
    def mana(self, mana: int):
        self.__mana = mana

    def __str__(self):
        description_base = super().__str__()
        return f"{description_base} ainsi que {self.__mana} de mana"




if __name__ == "__main__":
    mage1 = Mage("Gandalf")
    print(vars(mage1))
    print(mage1)