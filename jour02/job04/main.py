class Student:
    def __init__(self, nom, prenom, matricule, credit= 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__matricule = matricule
        self.__credit = credit
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_matricule(self):
        return self.__matricule
    
    def get_credit(self):
        return self.__credit
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_matricule(self, matricule):
        self.__matricule = matricule
    
    def add_credit(self, credit):
        if self.__credit < 0 :
            raise ValueError("Le nombre de credit ne peut être négatif")
    
        self.__credit += credit


    def affichageInfo(self):
        return f"Le nombre de credits de {self.__prenom} {self.__nom} est de {self.__credit} points"

    def studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80 and self.__credit < 90:
            return "Très Bien"
        elif self.__credit >= 70 and self.__credit < 80:
            return "Bien"
        elif self.__credit >= 60 and self.__credit < 70:
            return "Passable"
        elif self.__credit >= 0 and self.__credit < 60:
            return "Insufissant"
        
    def studendInfo(self):
        return f"Nom : {self.__nom} \nPrénom : {self.__prenom} \nid : {self.__matricule} \nNiveau : { self.studentEval()}"

firststudent = Student("John", "Doe", 145)


firststudent.add_credit(10)
firststudent.add_credit(10)
firststudent.add_credit(10)
print()
print(firststudent.affichageInfo())
print()
firststudent.add_credit(45)
print(firststudent.studendInfo())