class Forme:
    def __init__(self, air: int = 0):
        self.__air = air

    def set_air(self, air: int):
        self.__air = air

    def aire(self):
        return self.__air 
    
aire = Forme()

print(aire.aire())
class Rectangle(Forme):
    def __init__(self, largeur:int, hauteur:int):
        Forme.__init__(self, aire)
        self.__largeur = largeur
        self.__hauteur = hauteur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def aire(self):
        return f"L'aire du rectangle avec une l'hauteur de : {self.get_hauteur()} et une largeur de {self.get_largeur()} est égal à " + str(self.get_largeur() * self.get_hauteur())

  

rectangle = Rectangle(10, 20)

print(rectangle.aire())