def affiche(chaine:str)->str:
    return f"Texte à afficher : {chaine}"

class Velo:
    vitesse_courante = 1
    def __init__(self,marque:str="toto",taille_pneu:float=2.5,couleur:str="bleu",nbr_vitesse:int=10):
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couler = couleur
        self.nbr_vitesse = nbr_vitesse

    def gear_up(self):
        if self.vitesse_courante<self.nbr_vitesse:
            self.vitesse_courante += 1
            return self.vitesse_courante
        else:
            return "la vitesse est déja max"
    def gear_down(self):
        if self.vitesse_courante > 1:
            self.vitesse_courante-=1
            return self.vitesse_courante
        else:
            return "impossible de descendre en dessous de 1"

if __name__ == "__main__":
    str1 = "coucou"
    print(affiche(str1))
    velo1 = Velo()
    print(velo1.gear_up())
    velo2=Velo()
    print(velo2.vitesse_courante)
    print(velo1.gear_down())