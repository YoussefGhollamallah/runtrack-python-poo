class Livre:
    def __init__(self, titre, auteur,pages:int):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_pages(self, pages):
        self.__pages = pages
        if self.__pages < 0 :
            raise ValueError("Le nombre de pages ne peut être négatif")
        if self.__pages is not int(self.__pages):
            raise ValueError("Le nombre de pages ne peut être à nombre à virgule")

livre1 = Livre("Harry Potter : à l'école des sorciers", "J.K Rowling", 368)


print(livre1.get_pages())

print(livre1.get_titre())

print(livre1.get_auteur())