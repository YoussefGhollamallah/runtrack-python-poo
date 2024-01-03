class Voiture:
    def __init__(self, marque, modele,annee, kilometrage, move=False, reservoir: int=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__move = move
        self.__reservoir = reservoir
    
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_move(self):
        return self.__move
    
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def verifier_plein(self):
        return self.__reservoir
    
    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__move = True
            self.__reservoir -= 5
    
    def arreter(self):
        self.__move = False

    def affichageInfo(self):
        return f"{self.__marque} {self.__modele} {self.__annee} {self.__kilometrage} {self.__move} {self.__reservoir}"

voiture1 = Voiture("Renault", "21", 1995, 192563)

print(voiture1.affichageInfo())

voiture1.demarrer()

print(voiture1.affichageInfo())

voiture1.arreter()

print(voiture1.affichageInfo())