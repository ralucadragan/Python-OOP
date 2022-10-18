'''
3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume} si are un salar in valaore de {self.salariu} eur.')

    def nume_complet_angajat(self):
        return (self.nume +' ' + self.prenume)

    def salariu_lunar_angajat(self):
        return(self.salariu)

    def salariu_anual(self):
        return(self.salariu *12)

    def marire_salariu_angajat(self, procent,):
        self.salariu = int((procent * self.salariu) / 100) + self.salariu



a1 = Angajat('Dragan', 'Raluca', 3000)
a2 = Angajat('Berenyi', 'Stefania', 7000)

a1.descriere_angajat()
a2.descriere_angajat()

print(f'Numele complet al angajatului este {a1.nume_complet_angajat()}.')
print(f'Numele complet al angajatului este {a2.nume_complet_angajat()}.')

print(f'Salariul lunar al angajatului { a1.nume_complet_angajat()} este de {a1.salariu_lunar_angajat()} eur.')
print(f'Salariul lunar al angajatului { a2.nume_complet_angajat()} este de {a2.salariu_lunar_angajat()} eur.')

print(f'Salariu anual al angajatului {a1.nume_complet_angajat()}  este de {a1.salariu_anual()} eur.')
print(f'Salariu anual al angajatului {a2.nume_complet_angajat()}  este de {a2.salariu_anual()} eur.')

procent1 = 70
a1.marire_salariu_angajat(procent1)
print(f'Angajatul a primit o marime de salar, reprezentand {procent1}% din valoarea salarului actual. '
      f'Noul salariu va fi in valoare de {a1.salariu} eur.')
procent2 = 30
a2.marire_salariu_angajat(procent2)
print(f'Angajatul a primit o marime de salar, reprezentand {procent2}% din valoarea salarului actual. '
      f'Noul salariu va fi in valoare de {a2.salariu} eur.')
