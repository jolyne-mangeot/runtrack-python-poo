

class Ship:
    def __init__(self, name, parts):
        self.name = name
        self.__parts_dict__ = {}
        for part in list(parts.keys()):
            element = Part(part, parts[part]['materiel'], parts[part]['couleur'])
            self.__parts_dict__[part] = element
    
    def get_parts(self):
        return self.__parts_dict__

    def change_part(self, name, new_material):
        self.get_parts()[name].change_material(new_material)

    def print_info(self):
        print_infos = ''
        for part in list(self.__parts_dict__.keys()):
            print_infos += str(self.__parts_dict__[part]) + '\n'
        return print_infos
    
    def __str__(self):
        return self.print_info()

class Part(Ship):
    def __init__(self, name, material, color):
        self.name = name
        self.material = material
        self.color = color
    
    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f"Le bateau est fait de {self.name} construit en {self.material}"

boat_parts = {
    'mat' : {'materiel' : 'bois',
             'couleur' : 'noir'},
    'pont' : {'materiel' : 'bois',
              'couleur' : 'brun'},
    'coque' : {'materiel' : 'metal',
               'couleur' : 'gris'}
}
boat = Ship('Bobateau', boat_parts)

print(boat)

boat.change_part('mat', 'metal')

print(boat)