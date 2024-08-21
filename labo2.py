class Bicletas:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo 
        
trekMadone = Bicletas("trek", "trekMadone")
trek23 = Bicletas("trek", "trek23")

print(type(trekMadone))
print(type(trek23))

print(trekMadone.marca, trekMadone.modelo )
print(trek23.marca, trek23.modelo)
