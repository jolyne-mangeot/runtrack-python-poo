class Forme:
    def aire(self):
        self.__aire = 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
        self._perimetre = self.perimetre()
    
    def perimetre(self):
        perimetre = self._largeur * self._longueur
        return perimetre
    
    def set_largeur(self):
        self._largeur = int(input("Largeur : "))
    def get_largeur(self):
        return self._largeur

    def set_longueur(self):
        self._longueur = int(input("Longueur : "))
    def get_longueur(self):
        return self._longueur

class Parallepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self._hauteur = hauteur
        self.aire()

    def aire(self):
        self._aire = self._longueur * self._largeur * self._hauteur
    
    def get_dimension(self):
        print(
            f"L : {self._largeur}, l : {self._longueur}",
            f"h : {self._hauteur}, A : {self._aire}",
            sep="\n"
        )

class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__()
        self.__rayon = rayon
        self.__diametre = self.__rayon*2
        self.aire()
    
    def get_diametre(self):
        return self.__diametre
    
    def aire(self):
        self.__aire = 3.14 * (self.__rayon**2)
        return self.__aire

def main():
    rect = Rectangle(20,15)
    print(rect.get_largeur())
    pave = Parallepipede(rect.get_largeur(), rect.get_longueur(), 10)
    pave.get_dimension()
    rond = Cercle(15)
    print(rond.get_diametre())
    print(rond.aire())

main()