class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, personnage):
        personnage.vie -= 6
    
    def en_vie(self):
        if self.vie <=0:
            return False
        else:
            return True
    
    def get_vie(self):
        return self.vie
    
    def victoire(self, ennemi):
        if not ennemi.en_vie():
            print('Victoire !!!')
            return True
        if not self.en_vie():
            print('Défaite...')
            return True
        return False
    
class Jeu:
    def choisir_niveau(self):
        self.niveau = int(input("Difficulté : "))
    
    def lancer_jeu(self, nom_joueur):
        joueur = Personnage(nom_joueur, 15*self.niveau)
        ennemi = Personnage('Ennemi', 25*self.niveau)
        self.liste_joueur = (joueur, ennemi)

def game():
    partie = Jeu()
    partie.choisir_niveau()
    partie.lancer_jeu('bibi')
    done = False
    tour = 1
    while not done:
        for personnage in partie.liste_joueur:
            personnage.attaquer(partie.liste_joueur[tour%2])
            print(f"{personnage.nom} attaque ! \n{partie.liste_joueur[tour%2].nom} perd 6 pv,\
                  il lui en reste {partie.liste_joueur[tour%2].get_vie()}.")
            if personnage.victoire(partie.liste_joueur[1]) == True:
                done = True
            tour +=1

game()