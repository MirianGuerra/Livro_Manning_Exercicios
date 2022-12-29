"""Conta Bancaria"""

class Conta():
    def __init__(self, nome: str, saldo, senha:str) -> None:
        self.nome = nome
        self.saldo = saldo
        self.senha = senha
        
    def deposito(self, valor, senha):
        if self.senha != senha:
            print('Senha errada!')
            return None
        
        if valor<0:
            print('Não pode depositar um valor negativo.')
            return None
        
        self.saldo = self.saldo + valor
        print('Valor depositado com sucesso!')
        return self.saldo
    
    def saque(self, valor, senha):
        if self.senha != senha:
            print('Senha errada!')
            return None
        
        if valor>self.saldo:
            print('Não há saldo suficiente')
            return None
        
        self.saldo = self.saldo - valor
        print('Saque realizado com sucesso!')
        return self.saldo
    
    def saldo(self, senha):
        if self.senha != senha:
            print('Senha errada!')
            return None
        
        print(f'O saldo disponível é de R${self.saldo}')
        return self.saldo
    
    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Senha: {self.senha}')
        

mirian = Conta('Mirian', 20, '1234')
mirian.mostrar()
mirian.saque(30, '1234')

        