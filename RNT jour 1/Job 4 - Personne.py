class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def se_presenter(self):
        print(f"Je m'appelle {self.prenom} {self.nom}.")

def main():
    john = Personne('John', 'Doe')
    john.se_presenter()
    jean = Personne('Jean', 'Dupont')
    jean.se_presenter()

main()