class Operation:
    def __init__(self):
        self.nombre1 = 2
        self.nombre2 = 3
    
    def addition(self):
        self.nombre3 = self.nombre1 + self.nombre2

def main():
    __main__ = Operation()
    print(__main__)
    print(__main__.nombre1)
    print(__main__.nombre2)
    __main__.addition()
    print(__main__.nombre3)

main()