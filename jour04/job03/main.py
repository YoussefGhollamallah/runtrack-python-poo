class Rectangle:
    def __init__(self, longueur: int, largeur: int):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return f"Le perimètre du rectangle est :" + str(self.__longueur * 2 + self.__largeur * 2) + "."
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur:int,hauteur:int):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.get_hauteur() * self.get_largeur() * self.get_longueur()
    


rectangle = Rectangle(10, 20)

print(rectangle.perimetre())

print(rectangle.surface())

parapip = Parallelepipede(10, 20, 30)

print(parapip.volume())