'''
6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''

class Masina:
    def __init__(self, model, viteza_maxima):
        self.marca = 'Volvo'
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 70
        self.culori_disponibile = {'gri', 'verde', 'mov', 'visiniu'}
        self.inmatriculata = False

    def descriere(self):
        # descrie() (se vor printa toate atributele, inafara de culori_disponibile)
        print(f'Masina {self.marca}, modelul {self.model}, desi atinge o viteza maxima de {self.viteza_maxima} km/h,'
              f'aceasta este condusa pe autostrada cu viteza de {self.viteza_actuala} km/h si aceasta nici nu este inmatriculata - {self.inmatriculata}.')

    def inmatriculare(self):
        #inmatriculare() - va schimba atributul inmatriculata in True
        self.inmatriculata = True
        print(self.inmatriculata)

    def vopseste(self,culoare):
        # vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare
        # e in optiunea de culori displonibile, altfel afisati o eroare
        #culoare = input('Introduceti culoarea dorita pt masina: ')
        if culoare in self.culori_disponibile:
            self.culori_disponibile = culoare
            print(f'Culoarea aleasa - {self.culori_disponibile} - pentru masina este disponibila.')
        else:
            print(f'Culoarea aleasa nu este disponibila.')


    def accelereaza(self, viteza):
        # se va accelera la o anumita viteza,
        # daca viteza e negativa-eroare,
        # daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
        if viteza < self.viteza_actuala:
            print ('Viteza este mai mica decat viteza actuala ! Accelereaza!!!')
        elif viteza > self.viteza_actuala and viteza < self.viteza_maxima:
            print(f'Masina merge cu {viteza} km/h, dar ea poate ajunge pana la viteza maxima de {self.viteza_maxima} km/h. Accelereaza !!!!')
        else:
            print(f'Masina poate ajunge maxim pana la viteaza de {self.viteza_maxima} km/h. Va rugam incetiniti !!!!!')


    def franeaza(self):
        # masina se va opri si va avea viteza 0
        self.viteza_actuala = 0
        return self.viteza_actuala

m1 = Masina('V70', 300)
m2 = Masina('C30', 350)

m1.descriere()

m2.inmatriculare()

m1.vopseste('gri')
m2.vopseste('maro')

m1.accelereaza(120)
m2.accelereaza(520)
m2.accelereaza(50)

print(f'Viteza masinii este de {m2.franeaza()} si ea se opreste.')