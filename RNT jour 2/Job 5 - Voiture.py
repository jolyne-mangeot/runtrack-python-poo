class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = 0
        self.en_marche = False
    
    def set_marque(self):
        self.__marque = input("Marque : ")
    def get_marque(self):
        return self.__marque

    def set_modele(self):
        self.__modele = input("Modèle : ")
    def get_modele(self):
        return self.__modele

    def set_annee(self):
        self.__annee = input("Année : ")
    def get_annee(self):
        return self.__annee

    def set_kilometrage(self):
        self.__kilometrage = input("Kilométrage : ")
    def get_kilometrage(self):
        return self.__kilometrage

    def demarrer(self):
        if self.__reservoir > 5:
            self.en_marche = True
    
    def arreter(self):
        self.en_marche = False