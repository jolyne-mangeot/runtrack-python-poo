class Cercle:
    def __init__(self, rayon):
        self.rayon = float(rayon)

    def changer_rayon(self):
        self.rayon = float(input("Rayon : "))

    def afficher_infos(self):
        print(
            f"Rayon du cercle : {self.rayon}",
            f"Diamètre du cercle : {self.calcul_diametre()}",
            f"Circonférence du cercle : {self.calcul_circonference()}",
            f"Aire du cercle : {self.calcul_aire()}",
            sep="\n"
        )

    def calcul_circonference(self):
        self.circonference = float(self.calcul_diametre() * 3.1415926536)
        return self.circonference

    def calcul_aire(self):
        self.aire = float((self.rayon**2) * 3.1415926536)
        return self.aire

    def calcul_diametre(self):
        self.diametre = float(self.rayon * 2)
        return self.diametre

def main():
    circle = Cercle(6)
    circle.afficher_infos()
    print(circle.calcul_aire())
    circle.changer_rayon()
    circle.afficher_infos()

main()