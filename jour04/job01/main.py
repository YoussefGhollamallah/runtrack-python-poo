class Personne:
    def __init__(self, age: int = 14):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def afficherAge(self):
        return self.__age
    
    def bonjour(self):
        return "Hello"
    
    def modifierAge(self, age):
        self.__age = age


class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    
    def allerEnCours(self):
        return "Je vais en cours."
    
    def afficherAge(self):
        return f"J'ai " + str(super().afficherAge()) + " ans."
    

class Professeur(Personne):
    def __init__(self, matiereEnseigner: str):
        Personne.__init__(self)
        self.__matiereEnseigner = matiereEnseigner

    def get_matiereEnseigner(self):
        return self.__matiereEnseigner
    
    def set_matiereEnseigner(self, matiereEnseigner: str):
        self.__matiereEnseigner = matiereEnseigner

    def enseigner(self):
        return f"Le cours va commencer"


personne = Personne()
eleve1 = Eleve()
print(eleve1.afficherAge())  