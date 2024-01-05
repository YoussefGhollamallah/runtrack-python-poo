class CompteBancaire:
    def __init__(self, nom: str, prenom: str, numberbank: int, solde: float, decouvert : bool):
        self.__nom = nom
        self.__prenom = prenom
        self.__numberbank = numberbank
        self.__solde = solde
        self.__decouvert = decouvert
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom
    
    @property
    def numberbank(self):
        return self.__numberbank
    
    @numberbank.setter
    def numberbank(self, numberbank):
        self.__numberbank = numberbank
    
    @property
    def solde(self):
        return self.__solde
    
    @solde.setter
    def solde(self, solde):
        self.__solde = solde
    
    @property
    def decouvert(self):
        return self.__decouvert

    def afficher(self):
        return f"Le compte {self.numberbank} appartient à {self.nom} {self.prenom} "
    def afficherSolde(self):
        return f"Le solde du compte {self.numberbank} de {self.nom} {self.prenom} est de {self.solde} euros."

    def versement(self, montant):
        self.__solde += montant
        
    
    def retrait(self, montant):
        if self.__decouvert == True:
            self.__solde -= montant
        else:
            if self.__solde < montant:
                return f"Le solde du compte {self.numberbank} est insuffisant pour un retrait de {montant} euros, il vous reste de {self.__solde} euros."
            else:
                self.__solde -= montant
    
    def agios(self):
        if self.__solde < 0:
            self.__solde -= 20
    
    def effectuerVirement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            return f"Virement de {montant} euros effectué avec succès vers le compte {compte_destinataire.numberbank}. Le solde du compte {self.numberbank} est maintenant de {self.solde} euros."
        else:
            return f"Le solde du compte {self.numberbank} est insuffisant pour effectuer un virement de {montant} euros."

ayman = CompteBancaire("Hachem","Ayman","1234567890", 500, True)
youssef = CompteBancaire("Youssef","Youssef", "1234567891", 1000, False)

print(ayman.afficher())

print(ayman.afficherSolde())
ayman.versement(1000)

print(ayman.afficherSolde())

print(ayman.retrait(2000))

print(ayman.afficherSolde())
print(youssef.afficherSolde())
print(youssef.effectuerVirement(ayman, 500))

print(ayman.afficherSolde())
    