'''
5.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

'''
from datetime import  date

class Factura:
    sff = 'sfdsfg'
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.seria = 'TZ'

    def schimba_cantitatea(self, cantitate):
        self.cantitate = self.cantitate + cantitate

    def schimba_pretul(self, pretul):
        self.pret_buc = self.pret_buc + pretul

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura are seria {self.seria} numar {self.numar}')
        today = date.today()
        print(f'Data: {today}')


p1 = Factura(75, 'castane', 100, 1)
p2 = Factura(80, 'piersici', 50, 5)

p1.schimba_cantitatea(10)
print(f'Noua cantitate de {p1.nume_produs} este de {p1.cantitate} buc.')
p2.schimba_cantitatea(5)
print(f'Noua cantitate de {p2.nume_produs} este de {p2.cantitate} buc.')

p1.schimba_pretul(2)
p2.schimba_pretul(1)
print(f'Noul pret la produsul {p1.nume_produs} este de {p1.pret_buc} lei.')
print(f'Noul pret la produsul {p2.nume_produs} este de {p2.pret_buc} lei.')


p1.schimba_nume_produs('cirese')
p2.schimba_nume_produs('caise')
print(f'Noua denumire a produsului este {p1.nume_produs}.')
print(f'Noua denumire a produsului este {p2.nume_produs}.')

print('----------------------------------------')
p1.genereaza_factura()
print('              ')

print('Produs ', '|', ' Cantitate ', '|', 'Pret/Buc ', '|', ' Total ', '|')
print('----------------------------------------------')
print(p1.nume_produs, ' |', '   ', p1.cantitate, '   ', '|', '   ',  p1.pret_buc, '   ', '|', '  ', p1.cantitate*p1.pret_buc, '', '|',)
print(p2.nume_produs, '  |', '   ', p2.cantitate, '    ', '|', '   ',  p2.pret_buc, '   ', '|', '  ', p2.cantitate*p1.pret_buc, '', '|',)


