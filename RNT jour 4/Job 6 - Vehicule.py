class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def demarrer():
        print("attention je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informations_vehicule(self):
        print(
            f"Marque : {self.marque},",
            f"Modèle : {self.modele},",
            f"Année de production : {self.annee},",
            f"Prix : {self.prix},",
            f"Nombre de portes : {self.portes}",
            sep="\n"
        )
    
    def demarrer(self):
        print("attention je démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informations_vehicule(self):
        print(
            f"Marque : {self.marque},",
            f"Modèle : {self.modele},",
            f"Année de production : {self.annee},",
            f"Prix : {self.prix},",
            f"Nombre de roues : {self.roues}",
            sep="\n"
        )
    
    def demarrer(self):
        print("Chaud devant")

def main():
    clio = Voiture('peugeot', 'clio', '2000', 6000)
    clio.informations_vehicule()
    deux_roues = Moto("Yamaha", "moto", "2016", "2000")
    deux_roues.informations_vehicule()
    deux_roues.demarrer()
    clio.demarrer()

main()