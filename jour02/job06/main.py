class Commande:
    def __init__(self,numero_commande, liste_commande= [], statut_commande= "en cours"):
        self.__numero_commande = numero_commande
        self.__liste_commande = liste_commande
        self.__statut_commande = statut_commande
    
    def get_numero_commande(self):
        return self.__numero_commande
    
    def get_liste_commande(self):
        return self.__liste_commande
    
    def get_statut_commande(self):
        return self.__statut_commande
    
    def set_numero_commande(self, numero_commande):
        self.__numero_commande = numero_commande
    
    def ajouter_plat(self, plat):
        self.__liste_commande.append(plat)
      
    def annuler_commande(self, annuler):
   
        if annuler == self.__numero_commande: 
            self.__statut_commande = "annuler"
            self.__liste_commande.clear()
            return "le statut de la commande a été annulé"



commande = Commande(1)
print(commande.ajouter_plat("lasagne"))

print(commande.get_liste_commande())

print(commande.annuler_commande(1))


