import math
class Fracao():
    def __init__(self, numerador: int, denominador: int):
        self.denominador = denominador
        self.numerador = numerador
      
    
    def get_valor(self):
        return self.valor
    
    def __add__(self, outra_fracao):
        mult_den = (self.denominador*outra_fracao.denominador)
        num1 = (mult_den/self.denominador)*self.numerador
        num2 = (mult_den/outra_fracao.denominador)*outra_fracao.numerador
        numerador_soma = int(num1+num2)
        return (Fracao(numerador_soma,mult_den))

    def __sub__(self, outra_fracao):
        mult_den = (self.denominador*outra_fracao.denominador)
        num1 = (mult_den/self.denominador)*self.numerador
        num2 = (mult_den/outra_fracao.denominador)*outra_fracao.numerador
        numerador_subtracao = int(num1-num2)
        return (Fracao(numerador_subtracao, mult_den))

    def __mul__(self, outra_fracao):
        return (Fracao((self.numerador*outra_fracao.numerador), (self.denominador*outra_fracao.denominador)))
        

    def __eq__(self, outra_fracao):
        if self.numerador == outra_fracao.numerador and self.denominador==outra_fracao.numerador:
            return True
        else:
            return False

    def __ne__(self, outra_fracao):
        return not (self.numerador == outra_fracao.numerador) and (self.denominador == outra_fracao.denominador)

    def __lt__(self, outra_fracao):
        if (self.numerador/self.denominador) < (outra_fracao.numerador/outra_fracao.denominador):
            return True
        else:
            return False

    def __gt__(self, outra_fracao):
        if (self.numerador/self.denominador) > (outra_fracao.numerador/outra_fracao.denominador):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Esse Fração tem o valor {str(self.numerador)}/{str(self.denominador)}'
