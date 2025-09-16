class Tasse:
    matiere:str = "céramique"

    def __init__(self,couleur:str,contenance:int,marque:str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return (f"la tasse de matière {self.matiere}, de couleur {self.couleur} et de"
                f" marque {self.marque} a une contenance de {self.contenance} ml")

    def contenu(self,contenu:str):
        self.contenu = contenu

    def del_contenu(self):
        del(self.contenu)

if __name__ == "__main__":
    tasse1 = Tasse("bleue",125,"toto")
    print(tasse1)
    tasse1.contenu("lait")
    print(vars(tasse1))
    print(vars(Tasse))
    tasse1.del_contenu()
    print(vars(tasse1))