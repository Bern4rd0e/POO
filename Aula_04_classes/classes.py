class Triangulo: # Tipo de variável
    def __init__(self):
        self.b = 0 
        self.h = 0

    def teste(self):
        return "Olá"

    def calc_area(self): # Método
        return self.b * self.h / 2

x = Triangulo()
print(x)
print(x.teste())
print(x.b, x.h)
print(x.calc_area())
x.b = 10
x.h = 20

y = Triangulo()
print(y)
print(y.teste())
print(y.b, y.h)
print(y.calc_area())