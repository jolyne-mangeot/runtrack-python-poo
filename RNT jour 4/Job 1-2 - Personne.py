class Personne:
    def __init__(self):
        self.age = 14
    
    def modifier_age(self):
        self.age = int(input('Nouvel âge : '))
        self.afficher_age()

    def afficher_age(self):
        print(f"J'ai {self.age} ans !")
    
    def bonjour():
        print('Hellloo')
    
class Eleve(Personne):
    def __init__(self, prenom):
        super().__init__()
        self.prenom = prenom
    
    def aller_en_cours():
        print("Je vais en cours")
    
    def afficher_age(self):
        print(f"J'ai {self.age} ans hihi !")

class Professeur(Personne):
    def __init__(self, matiere):
        super().__init__()
        self.__matiere = matiere
    
    def enseigner():
        print("La classe va commencer")

def main():
    marie = Eleve('Marie')
    marie.aller_en_cours()
    marie.modifier_age()
    jerome = Professeur()
    jerome.modifier_age()
    jerome.enseigner()
    jerome.afficher_age()