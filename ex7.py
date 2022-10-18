'''
7. Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''

class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        # se va adauga in dict
        self.todo[nume] = descriere
        return self.todo

    def finalizeaza_task(self, nume):
        # se va sterge din dict
        self.todo.pop(nume)
        return self.todo

    def afiseaza_todo_list(self):
        # doare cheile
        return self.todo.keys()

    #def afiseaza_detalii_suplimentare(self, nume, task):
        # in funct de numele taskului, printam detalii suplimentare
        # daca taskul nu e in todolist, intrebam utilizatorul daca vrea sa il adauge.
        # daca acesta raspunde nu - la revedere
        # daca raspunde da - il cerem detalii task si salvam nume + detalii in dict



todo = TodoList()

todo.adauga_task('Raluca', 'canta')
todo.adauga_task('Stefania', 'danseaza')
print(f"Taskuri initiale: {todo.adauga_task('Stefan', 'doarme')}.")

print(f"Au mai ramasa de facut urmatoarele taskuri: {todo.finalizeaza_task('Stefan')}.")

print(todo.afiseaza_todo_list())


