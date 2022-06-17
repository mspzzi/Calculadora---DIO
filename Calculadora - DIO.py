class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
        
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
        
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())