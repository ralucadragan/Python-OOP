'''
4.
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.sold = self.sold + suma

    def creditare_cont(self, suma):
        self.sold = self.sold - suma


titular1 = Cont('RO39INGB0000111122223333', 'Dragan Raluca', 3000)
titular2 = Cont('RO09INGB9999888877776666', 'Berenyi Stefania', 7000)


titular1.afisare_sold()
titular2.afisare_sold()

a = 3000
titular1.debitare_cont(a)
print(f'Titularul {titular1.titular_cont} a incarcat contul cu suma de {a} lei si are in acest moment in cont suma de {titular1.sold} lei.')
b = 7000
titular2.debitare_cont(b)
print(f'Titularul {titular2.titular_cont} a incarcat contul cu suma de {b} lei si are in acest moment in cont suma de {titular2.sold} lei.')

c = 1000
titular1.creditare_cont(c)
print(f'Titularul {titular1.titular_cont} a scos din cont suma de {c} lei si are in acest moment in cont suma de {titular1.sold} lei.')
d = 4000
titular2.creditare_cont(d)
print(f'Titularul {titular2.titular_cont} a scos din cont suma de {d} lei si are in acest moment in cont suma de {titular2.sold} lei.')




