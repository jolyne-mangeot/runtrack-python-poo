class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ''
    
    def vieillir(self):
        print(self.age)
        self.age +=1
        print(self.age)
    
    def nommer(self):
        self.prenom = input('prénom : ')
        print(f"L'animal se nomme {self.prenom}")

def main():
    loup = Animal()
    loup.vieillir()
    loup.nommer()

main()