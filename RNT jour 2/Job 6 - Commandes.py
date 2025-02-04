plats_liste = {
    "gnocchis" : 12.99,
    "spaghettis" : 8.99
}

class Commande:
    def __init__(self, numero_commande, *plats_commandes):
        self.__commande = {
            "numero commande" : numero_commande,
            "status commande" : "en cours",
            "prix commande" : 0
        }
        for plat_commande in plats_commandes:
            if plat_commande in list(plats_liste.keys()):
                plat = {
                    "prix" : plats_liste[plat_commande],
                    "status plat" : "en cours"
                }
                self.__commande.update({plat_commande : plat})
                self.__commande["prix commande"] += plats_liste[plat_commande]
                print(self.__commande)
    
    def annuler_commande(self):
        self.__commande["status commande"] = "annulee"
    
    def ajout_plat(self, *plats_ajoutes):
        for plat_commande in plats_ajoutes:
            if plat_commande in list(plats_liste.keys()):
                plat = {
                    "prix" : plats_liste[plat_commande],
                    "status plat" : "en cours"
                }
                self.__commande.update({plat_commande : plat})
                self.__commande["prix commande"] += plats_liste[plat_commande]
                print(self.__commande)
    
    def get_commande(self):
        print(self.__commande)
    
    def get_addition(self):
        prixht = self.__commande["prix commande"]
        self.calcul_tva()
        reste_a_payer = self.__commande["prix tva"]
        return prixht, reste_a_payer
    
    def calcul_tva(self):
        self.__commande["prix tva"] = round(self.__commande["prix commande"] * 1.2, 2)

def main():
    achat = Commande(135, "gnocchis", "spaghettis")
    achat.ajout_plat("spaghettis")
    achat.annuler_commande()
    achat.get_commande()
    print(achat.get_addition())


main()