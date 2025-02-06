import random
class Carte:
    def __init__(self, score, valeur, couleur):
        self.score = int(score)
        self.valeur = str(valeur)
        self.couleur = couleur
        self.nom = self.valeur + " de " + self.couleur
    
    def get_symbole(self):
        self.couleurs = ('trefle','pique','carreau','coeur')
    
    def get_figure(self):
        self.figures = ('valet', 'dame', 'roi')
    
    def get_valeur(self):
        self.valeurs = ['as','deux','trois','quatre','cinq','six','sept','huit','neuf','dix']

class Jeu(Carte):
    def __init__(self):
        self.main_joueur = []
        self.valeur_joueur = 0
        self.main_croupier = []
        self.valeur_croupier = 0
        self.get_symbole()
        self.get_figure()
        self.get_valeur()
    
    def creer_paquet(self, as_11):
        paquet = []
        if as_11:
            self.valeurs.append(self.valeurs.pop(0))
        for symbole in self.couleurs:
            if as_11:
                score = 2
            else:
                score = 1
            for valeur in self.valeurs:
                carte = Carte(score, valeur, symbole)
                paquet.append(carte)
                score += 1
            for figure in self.figures:
                carte = Carte(10, figure, symbole)
                paquet.append(carte)
        return paquet
    
    def get_main(self):
        print(f"\033[H\033[2JMain du joueur : {self.valeur_joueur}",)
        for carte in self.main_joueur:
            print(carte.nom)
        print(f"\nMain du croupier : {self.valeur_croupier}",)
        for carte in self.main_croupier:
            print(carte.nom)

    def debut_partie(self, as_11):
        self.paquet = self.creer_paquet(as_11)
        for pioche in range (0,2):
            self.valeur_joueur = self.piocher(self.main_joueur, self.valeur_joueur)
            self.valeur_croupier = self.piocher(self.main_croupier, self.valeur_croupier)

    def piocher(self, main, joueur):
        carte = random.randint(0,len(self.paquet)-1)
        main.append(self.paquet[carte])
        joueur += self.paquet[carte].score
        self.paquet.pop(carte)
        return joueur
    
    def message_fin(self, victoire_defaite):
        if victoire_defaite == 'victoire':
            print("Le joueur gagne ! défaite pour le croupier...")
        elif victoire_defaite == 'defaite':
            print("Le croupier l'emporte !")

def main():
    partie = Jeu()
    while True:
        choix_joueur = str(input("\033[H\033[2J\n As ou Onze : ")).lower()
        match choix_joueur:
            case 'as':
                as_11 = False
                break
            case 'onze'|'o':
                as_11 = True
                break
            case _:
                continue
    partie.debut_partie(as_11)
    over = False
    tour_croupier = False
    while not over:
        partie.get_main()
        if partie.valeur_joueur < 21:
            choix_joueur = str(input("\n(R)ecevoir ou (P)asser\n ")).lower()
        else:
            choix_joueur = "p"
        if choix_joueur not in ('r','p'):
            continue
        else:
            match choix_joueur:
                case "p" | "passer":
                    tour_croupier = True
                case "r" | "recevoir":
                    partie.valeur_joueur = partie.piocher(partie.main_joueur, partie.valeur_joueur)
                    continue
                case _:
                    continue
        if tour_croupier:
            while partie.valeur_croupier <= 17:
                partie.valeur_croupier = partie.piocher(partie.main_croupier, partie.valeur_croupier)
        if partie.valeur_joueur > 21 or partie.valeur_croupier > 21 or partie.valeur_croupier > partie.valeur_joueur:
            joueur_perdu = 'defaite'
        else:
            joueur_perdu = 'victoire'
        partie.get_main()
        partie.message_fin(joueur_perdu)
        over = True
        break

main()