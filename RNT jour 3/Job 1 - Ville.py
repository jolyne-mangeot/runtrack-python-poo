class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
    
    def ajouterpopulation(self):
        self.__nombre_habitants +=1
    
    def get_infos(self):
        return f"nom : {self.__nom}, nombre d'habs. : {self.__nombre_habitants}"
    
    def get_nom(self):
        return f"{self.__nom}"

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterpopulation(self):
        self.__ville.ajouterpopulation()
    
    def get_infos(self):
        return f"nom : {self.__nom}, âge : {self.__age}, lieu : {self.__ville.get_nom()}"

def main():
    paris = Ville('Paris', 1000000)
    marseille = Ville('Marseille', 861635)
    john = Personne('John', 45, paris)
    myrtille = Personne('Myrtille', 4, paris)
    chloe = Personne('Chloé', 18, marseille)

    print(paris.get_infos())
    print(john.get_infos())
    john.ajouterpopulation()
    print(myrtille.get_infos())
    print(paris.get_infos())

main()