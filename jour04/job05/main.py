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

class Cercle(Forme):
    def __init__(self, radius:int):
        Forme.__init__(self, aire)
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def aire(self):
        return f"L'aire du cercle avec un rayon de : {self.get_radius()} est égal à " + str(format(self.get_radius() * 2 * 3.14, ".5f")) + " cm2."
    

cercle = Cercle(10)

print(cercle.aire())