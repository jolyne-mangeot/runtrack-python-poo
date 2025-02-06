class Comptebancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        if self.__solde < 0:
            self.agios()
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Numéro : {self.__numero_compte}, Nom : {self.__nom}, Solde : {self.__solde}")
    
    def afficher_solde(self):
        print(f"Solde : {self.__solde}")
    
    def versement(self, versement):
        self.__solde += versement
    
    def virement(self, particulier, montant):
        if montant > self.__solde and self.__decouvert == False or montant < 0:
            print("non")
        else:
            self.__solde -= montant
            if self.__solde < 0:
                self.agios()
            particulier.versement(montant)
    
    def agios(self):
        self.__solde *= 1.2
    
    def retrait(self, retrait):
        if self.__solde - retrait < 0 and self.__decouvert == False:
            print(f"Solde insuffisant")
        else: 
            self.__solde -= retrait
            if self.__solde < 0:
                self.agios()
            print(self.__solde)

def main():
    john = Comptebancaire(489, 'Doe', 'John', -48, True)
    john.afficher_solde()
    myrtille = Comptebancaire(456, 'Fruit', 'Myrtille', 489, False)
    myrtille.virement(john, 456)
    john.afficher_solde()

main()