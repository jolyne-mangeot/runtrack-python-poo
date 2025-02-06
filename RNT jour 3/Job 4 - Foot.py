class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.carton_rouge = 0
    
    def marquer_but(self):
        self.buts_marques +=1
    
    def passe_decisive(self):
        self.passes_decisives +=1
    
    def recevoir_carton_jaune(self):
        self.cartons_jaunes +=1

    def recevoir_carton_rouge(self):
        self.carton_rouge +=1
    
    def get_infos(self):
        return f"Nom : {self.nom}, Numéro : {self.numero}, Position : {self.position}\
            \nButs : {self.buts_marques}, Passes : {self.passes_decisives}\
            \nCartons, Jaunes : {self.cartons_jaunes}, Rouge : {self.carton_rouge}"

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouter_joueur(self, *joueur):
        for ajout in joueur:
            self.joueurs.append(ajout)
    
    def get_infos(self):
        for joueur in self.joueurs:
            print(joueur.get_infos())
    
    def maj_infos(self, joueur, info):
        match info:
            case 'carton jaune':
                self.joueurs[self.joueurs.index(joueur)].recevoir_carton_jaune()
            case 'carton rouge':
                self.joueurs[self.joueurs.index(joueur)].recevoir_carton_rouge()
            case 'marquer but':
                self.joueurs[self.joueurs.index(joueur)].marquer_but()
            case 'passe decisive':
                self.joueurs[self.joueurs.index(joueur)].passe_decisive()

def game():
    harry = Joueur('Harry', '01', 'Gardien')
    jojo = Joueur('Jojo', '04', 'Attaquant')
    gerard = Joueur('Gérard', '06', 'Défenseur')
    gogogo = Equipe('GoGoGo')
    gogogo.ajouter_joueur(harry, jojo, gerard)
    gogogo.get_infos()
    gogogo.maj_infos(harry, 'marquer but')
    gogogo.maj_infos(jojo, 'carton rouge')
    gogogo.maj_infos(gerard, 'marquer but')
    gogogo.maj_infos(gerard, 'passe decisive')
    gogogo.get_infos()

game()