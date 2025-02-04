class Student:
    def __init__(self, nom, prenom, id, credits):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = credits
        self.__level = self.__student_eval()

    def get_format_name(self):
        nom = self.__nom
        prenom = self.__prenom
        return f"{prenom} {nom}"

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        self.__init__(self.__nom, self.__prenom, self.__id, self.__credits)
    
    def get_credits(self):
        credits = self.__credits
        return credits
    
    def __student_eval(self):
        if self.__credits >=90:
            return "Excellent"
        elif self.__credits >=80:
            return "Très bien"
        elif self.__credits >=70:
            return "Bien"
        elif self.__credits >=60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def get_infos(self):
        nom = self.__nom
        prenom = self.__prenom
        id = self.__id
        credits = self.__credits
        level = self.__level
        print(
            f"Etudiant : {nom} {prenom}",
            f"Numéro : {id}",
            f"Crédits : {credits} Niveau : {level}",
            sep="\n"
        )

def main():
    john = Student("Doe", "John", 145, 0)
    john.add_credits(35)
    john.add_credits(20)
    john.add_credits(15)
    print(f"Le nom de crédits de {john.get_format_name()} est de {john.get_credits()} points.")
    john.get_infos()

main()