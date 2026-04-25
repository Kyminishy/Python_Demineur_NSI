import random as rd

#Fonction qui crée la grille
def InitGrille()->list:
    """
    Cette fonction est une procédure qui crée la grille à son état d'inistalisation.
    ----------------------------------------------------------------------------------------------------
    Paramètre :
    X
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    X
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    return [[0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0]]

#Fonction qui place les mines
def PlaceMines(grille:list)->list:
    """
    Cette fonction sert à inserer des mines dans la grille de jeu.
    ----------------------------------------------------------------------------------------------------
    Paramètre :
    grille représente la grille initiale.
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    X
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    nombresmines=6
    while nombresmines>0:
        ligne=rd.randint(1,5)
        colonne=rd.randint(1,5)
        if grille[ligne][colonne]==0:
            grille[ligne][colonne]=9
            nombresmines=nombresmines-1
    return grille
#Fonction retournant la grille avec contours
def ContourGrille(grille:list)->list:
    """
    Cette fonction agrandis la grille.
    ----------------------------------------------------------------------------------------------------
    Paramètre :
    grille représente la grille de jeu.
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    La grille agrandie.
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    contourgrille = []

    contourgrille.append([0]*7)  # Ajoute la première ligne de 7 zéros

    for i in range(1,len(grille)):
        ligne = grille[i][1:] # On prend la ligne sans le numéro de ligne ( [1:] -> pas le premier index)
        contourgrille.append([0] + ligne + [0]) # on ajoute la ligne récupéré + un 0 au debut et à la fin

    contourgrille.append([0]*7)  # Ajoute la dernière ligne de 7 zéros
    return contourgrille
   
#Fonction donnant le nombre de mines voisines
def NombreMines(grille:list, n:int, p:int)->int:
    """
    Cette fonction donne le nombre de mines voisines de la case indiquée.
    ----------------------------------------------------------------------------------------------------
    Paramètre :
    grille représente la grille de jeu.
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    Le nombre de mines voisines de la case indiquée.
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    grillelarge = ContourGrille(grille) # récupere la grille avec uniquement les bombes
   
    n = n -1# se place dans le coin supérieur droit de carré 3x3 autour de la position
    p = p -1
   
    count = 0
   
    for i in range(3): # parcours les 3 lignes du carré 3x3
        for j in range(3): # parcours la ligne du carré 3x3
            if grillelarge[n][p] == 9: # si bombe = + 1 count
                count += 1
            n += 1
        p += 1
        n -= 3
       
    return count

#Fonction permettant de voir la grille
def Affiche(grille:list)->str:
    """
    Cette fonction affiche la grille de jeu.
    ----------------------------------------------------------------------------------------------------
    Paramètre :
    grille représente la grille de jeu à afficher.
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    La grille.
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    for x in range(6):
        temp = ' '.join(str(i) for i in grille[x])
        print(temp)

def grilleJoueur(grille:list, grille_joueur:list, n:int, p:int)->list:
    '''
    '''
    mines = NombreMines(grille, n,p)
    grille_joueur[n][p] = mines
    return grille_joueur


#Programme principal
def DeroulementPartie(grille: list, colonne_n: int, ligne_n: int)-> str:
    """
    Cette fonction permet d'annoncer au joueur son avancement dans la partie.
    ----------------------------------------------------------------------------------------------------
    Paramètres :
    colonne_n représente la colonne visée par le joueur.
    ligne_n représente la ligne visée par le joueur.
    ----------------------------------------------------------------------------------------------------
    Renvoie :
    Si le joueur a touché une mine ou non et/ou si il a gagné.
    ----------------------------------------------------------------------------------------------------
    Tests :
    """
    global compteur #On dit au code d'utiliser la variable compteur deja donnée
    global mort #pareil
    global grillejoueur

    if grille[ligne_n][colonne_n]==0:
        grille[ligne_n][colonne_n]=8
        compteur=compteur+1
        grilleJoueur(grille, grillejoueur, ligne_n, colonne_n)
        Affiche(grillejoueur)
        if compteur==19:
            return "Vous avez découvert toutes les cases vides sans toucher de mine. C'est gagné!"
        return "Vous avez découvert une case vide. Continuez de jouer"
    elif grille[ligne_n][colonne_n]==9:
        mort = True
        return "Vous avez touché une mine. C'est perdu !"



grille = PlaceMines(InitGrille())
compteur = 0
mort = False
grillejoueur:list=[[0,1,2,3,4,5],[1,"X","X","X","X","X"],[2,"X","X","X","X","X"],[3,"X","X","X","X","X"],[4,"X","X","X","X","X"],[5,"X","X","X","X","X"]]


while mort == False and compteur < 19:
    while True:
        try:
            ligne = int(input("Ligne : "))
            if 1 <= ligne <= 5: # le nombre est entre 1 et 5
                break
            else:
                print("Erreur : le nombre doit être compris entre 1 et 5.") # nombre en dehors de l'intervalle
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.") # pas un nombre entier

    while True:
        try:
            colonne = int(input("Colonne : "))
            if 1 <= colonne <= 5: # le nombre est entre 1 et 5
                break
            else:
                print("Erreur : le nombre doit être compris entre 1 et 5.") # nombre en dehors de l'intervalle
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.") # pas un nombre entier

           


    print(DeroulementPartie(grille, colonne, ligne))


if __name__=="__main__":
    import doctest
    doctest.testmod()
