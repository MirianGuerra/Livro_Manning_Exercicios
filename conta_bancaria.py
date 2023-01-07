"""Conta Bancaria"""

class Conta():
    def __init__(self, nome: str, saldo=0.0, senha:str = '0000') -> None:
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
    
    def mostrar_saldo(self, senha):
        if self.senha != senha:
            print('Senha errada!')
            return None
        return self.saldo
    
    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Senha: {self.senha}')
        
conta = Conta('Mirian', 10, 'c')
print(conta.mostrar_saldo('c'))