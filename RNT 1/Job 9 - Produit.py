class Produit:
    def __init__(self, nom, tva, prixht):
        self.nom = nom
        self.tva = tva
        self.prixht = prixht
    
    def calculer_prix_ttc(self):
        self.prixttc = self.prixht * (1 + self.tva/100)
        return round(self.prixttc, 2)
    
    def afficher(self):
        return f"Produit : {self.nom}\nPrix HT : {self.prixht}\nTVA : {self.tva}\nPrix TTC : {self.calculer_prix_ttc()}"

def main():
    riz = Produit('riz', 20, 2.99)
    print(riz.afficher())
    riz.tva = 30
    riz.nom = 'pâtes'
    print(riz.afficher())

main()