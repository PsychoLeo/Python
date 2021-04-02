# -24, -14, -9, -8, -6, -5, -3, -2, 0, 1, 6, 16
# n+4|3*n**2+7*n

class Diviseurs:

    def __init__(self, values, condition):
        self.values = values
        self.input_condition = condition
        self.diviseur, self.nombre = self.input_condition.split('|')

    def __str__(self):
        for i in self.values :
            div = eval(self.diviseur.replace('n', str(i)))
            if div != 0 :
                nombre = eval(self.nombre.replace('n', str(i)))
                condition = (nombre % div == 0)
                print(f"n: {i:<7} {self.nombre}: {nombre: <7} {self.diviseur}: {div: <7} {self.input_condition}: {condition}")
        return None

if __name__ == '__main__' :
    values = eval(input('Enter the n values (separated by commas) : '))
    condition = input('Enter your condition (ex: 2*n+1|3*n+4) : ')
    d = Diviseurs(values, condition)
    print(d)