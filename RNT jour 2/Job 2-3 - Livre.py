class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
    
    def set_pages(self):
        input_pages = input("Nombre de pages : ")
        try:
            test = int(input_pages)
            if test <=0:
                raise Exception()
            self.__pages = test
        except Exception:
            print("Insérez un nombre de page entier et positif")
    
    def vérification(self):
        if self.__disponible:
            return True
        else:
            return False
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print("Ce livre n'est pas disponible")
    
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
        else:
            print("Ce livre n'a pas été emprunté")

def main():
    book = Livre()
    book.set_pages()
    book.emprunter()
    book.rendre()
    book.rendre()