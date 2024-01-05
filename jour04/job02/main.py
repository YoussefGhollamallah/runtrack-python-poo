class Personne:
    def __init__(self, age: int = 14):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def afficherAge(self):
        return f"j'ai " + str(self.__age) + " ans."
    
    def bonjour(self):
        return "Hello"
    
    def modifierAge(self, age):
        self.__age = age


class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    
    def allerEnCours(self):
        return "Je vais en cours"
    

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
print(eleve1.bonjour())
print(eleve1.allerEnCours())
eleve1.modifierAge(15)
print(eleve1.afficherAge())

ayman = Professeur("Professeur de français")
ayman.modifierAge(40)
print(ayman.afficherAge())
print(ayman.bonjour())
print(ayman.enseigner())