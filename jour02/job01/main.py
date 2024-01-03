class Rectangle:
    def __init__(self,longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def get_longeur(self):
        return "La longeur du rectangle : ",self.__longeur
    
    def get_largeur(self):
        return "La largeur du rectangle est : ",self.__largeur
    
    def set_longeur(self, longeur):
        self.__longeur = longeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


rectangle = Rectangle(10, 5)

print(rectangle.get_longeur())

print(rectangle.get_largeur())

rectangle.set_longeur(20)

print(rectangle.get_longeur())