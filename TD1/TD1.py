def plusgrand_nbr ( a : float , b : float ) -> float :
    """
    fonction qui retourne le plus grand nombre entre 2 réels
    """
    if a > b:
        return a
    else :
        return b

def sup_seuil ( a : float , b : float =10.0) -> str : #possible de retourner un bool avec true or false
    if a > b:
        return ("supérieur au seuil")
    else:
        return ("inférieur au seuil")

def plusgrand_liste (liste : list) -> int:
    max=0
    for i in range (len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def plusgrand_liste_2 ( *args) -> float:
    max:float=args[0]
    for val in args:
        if val > max:
            max = val
    return max

def nbr_liste_inf_seuil(liste : list, seuil : float = 3.0) -> int:
    nbr_val=0
    for i in liste:
        if i < seuil:
            nbr_val += 1
    return nbr_val

def nbr_liste_inf_seuil_corr(*args, seuil : float = 3.0) -> int:
    nbr_val:int=0
    for val in args:
        if val < seuil:
            nbr_val += 1
    return nbr_val

def donne_dico (dictionnaire:dict,chaine_carac:str) ->list:
    lst:list =[]
    for keys,values in dictionnaire.items():
        lst.append((chaine_carac,keys,values))
    return lst

print(plusgrand_nbr(1.5,4.6))
print(sup_seuil(1.2))
print (plusgrand_liste([1,8,4,2,5,9]))
print (plusgrand_liste_2(1,8,4,2,5,9))
print(nbr_liste_inf_seuil([1,8,4,2,5,9,1.2,2.99]))
print(nbr_liste_inf_seuil_corr(1,8,4,2,5,9,1.2,2.99,3, seuil = 4))
print((donne_dico({1:"test",2:"coucou"},"les valeurs sont")))


