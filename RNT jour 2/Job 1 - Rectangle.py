class Rectangle:
    def __init__(self):
        self.__longueur = 0
        self.__largeur = 0
    
    def get_longueur(self):
        print(self.__longueur)
    
    def set_largeur(self):
        self.__largeur = input("Larger : ")
        print(self.__largeur)

def main():
    rect = Rectangle
    rect.get_longueur()
    rect.set_largeur()

main()