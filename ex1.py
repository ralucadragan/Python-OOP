'''
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Cercul are raza de {self.raza} cm si culoarea {self.culoare}.')

    def aria_cerc(self):
        aria = 3.14 * self.raza * self.raza
        return(aria)

    def diametru_cerc(self):
        return(2 * self.raza)

    def circumferinta_cerc(self):
        circumferinta = 2 * 3.14 * self.raza
        return(circumferinta)

c1 = Cerc(4, 'roz')
c2 = Cerc(7, 'mov')

c1.descriere_cerc()
c2.descriere_cerc()

print(f'Aria ceruclui este: {c1.aria_cerc()} cmp.')
print(f'Aria ceruclui este: {c2.aria_cerc()} cmp.')

print(f'Diametrul ceruclui este: {c1.diametru_cerc()} cm.')
print(f'Diametrul ceruclui este: {c2.diametru_cerc()} cm.')

print(f'Circumferinta ceruclui este: {c1.circumferinta_cerc()} cm.')
print(f'Circumferinta ceruclui este: {c2.circumferinta_cerc()} cm.')