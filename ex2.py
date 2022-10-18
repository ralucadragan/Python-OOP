'''
2.
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        print(f'Drptunghiul are culoarea {self.culoare} si urmatoarele dimensiuni: {self.lungime} x {self.latime} cm.')

    def aria_deptunghi(self):
        return(self.lungime * self.latime)

    def perimetru_deptunghi(self):
        return(2 * (self.lungime + self.latime))

    def schimba_culoare(self, new_color):
        self.culoare = new_color


d1 = Dreptunghi(10, 5, 'roz')
d2 = Dreptunghi(7, 3, 'portocaliu')

d1.descriere_dreptunghi()
d2.descriere_dreptunghi()

print(f'Aria dreptunghiului este: {d1.aria_deptunghi()} cmp.')
print(f'Aria dreptunghiului este: {d2.aria_deptunghi()} cmp.')

print(f'Perimetrul dreptunghiului este: {d1.perimetru_deptunghi()} cm.')
print(f'Perimetrul dreptunghiului este: {d2.perimetru_deptunghi()} cm.')

d1.schimba_culoare('maro')
d2.schimba_culoare('albastru')
print(f'Culoarea dreptunghiului s-a schimbat in {d1.culoare}.')
print(f'Culoarea dreptunghiului s-a schimbat in {d2.culoare}.')