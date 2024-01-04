class Ville:
    def __init__(self, ville: str, habitants: int):
        self.__ville = ville
        self.__habitants = habitants

    @property
    def ville(self):
        return self.__ville
    
    @ville.setter
    def ville(self, ville):
        self.__ville = ville
    
    @property
    def habitants(self):
        return self.__habitants
    
    @habitants.setter
    def habitants(self, habitants):
        self.__habitants = habitants

    def afficher_nb_habitants(self):
        return f"Le nombre d'habitants de la ville de {self.ville} est de {self.habitants} habitants."

paris = Ville("Paris", 1000000)
print(paris.afficher_nb_habitants())

marseille = Ville("Marseille", 861635)
print(marseille.afficher_nb_habitants())
print()

class Personne:
    def __init__(self, nom: str, age: int, ville: str):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @property
    def ville(self):
        return self.__ville

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @age.setter
    def age(self, age):
        self.__age = age

    @ville.setter
    def ville(self, ville):
        self.__ville = ville

    def ajouterPopulation(self, ville_obj):
        if ville_obj.ville == "Paris":
            ville_obj.habitants += 1
        elif ville_obj.ville == "Marseille":
            ville_obj.habitants += 1

personne1 = Personne("John", 45, "Paris")
personne2 = Personne("Mytille", 4, "Marseille")
chloe = Personne("Chloe", 25, "Paris")
personne1.ajouterPopulation(paris)
personne2.ajouterPopulation(marseille)
chloe.ajouterPopulation(paris)


print(paris.afficher_nb_habitants())
print(marseille.afficher_nb_habitants())
