class car:
    def __init__(self, marca, modelo):
        self.brand = marca
        self.model = modelo

    def move (self):
        print("Drive!")

class boat:
    def __init__(self, marca, modelo):
        self.brand = marca
        self.model = modelo
    
    def move (self):
        print("Sail!")

class plane:
    def __init__(self, marca, modelo):
        self.brand = marca
        self.model = modelo
    
    def move (self):
        print("Fly!")

carro = car("Ford", "Mustang")
barco = boat("Ibiza", "Touring 20")
avião = plane("Boeing", "747")

for x in (carro, barco, avião):
    x.move()

