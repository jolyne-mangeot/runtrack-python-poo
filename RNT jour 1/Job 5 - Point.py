class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficher_points(self):
        print(f"x : {self.x}, y : {self.y}")
    
    def afficher_x(self):
        print(f"x : {self.x}")

    def afficher_y(self):
        print(f"y : {self.y}")
    
    def changer_x(self):
        self.x = input('x :')

    def changer_y(self):
        self.y = input('y :')

def main():
    coordonnées = Point(45,5)
    coordonnées.afficher_points()
    coordonnées.changer_x()
    coordonnées.afficher_y()