from fracao import Fracao
from Funcionarios import *

fracao1 = Fracao(5,3)
fracao2 = Fracao(3,2)
fracao3 = Fracao(7,4)

print(fracao1)

print(fracao1+fracao2)
print(fracao1-fracao2)
print(fracao1*fracao3)
print(fracao1 == fracao3)
print(fracao2>fracao3)

mirian = Funcionario('Mirian', 'analista', 1500)
bruno = Gerente('Bruno', 'Gerente Geral', 3000)

print(mirian.get_funcao())
print(bruno.get_nome())
print(mirian.get_nome())
print(bruno.pagamento_anual(bonus=True))
print(mirian.pagamento_anual())
