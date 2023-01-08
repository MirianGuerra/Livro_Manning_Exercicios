from conta_bancaria import *


def pegando_nro_conta_e_senha():
    numero_conta = int(input('Entre com seu número de conta: '))
    senha = input('Entre com a senha: ')
    return numero_conta, senha


class Banco():
    def __init__(self) -> None:
        self.dic_contas = {}
        self.proximo_nro_conta = 0
        
    def criar_conta(self, nome: str, valor_inicial: float =0.0, senha: str = '0000'):
        conta = Conta(nome, valor_inicial, senha)
        nro_conta = self.proximo_nro_conta
        self.dic_contas[nro_conta]=conta
        self.proximo_nro_conta +=1
        return nro_conta
    
    def abrir_conta(self):
        print(' *** ABRIR CONTA *** ')
        nome = input("Digite seu nome completo: ")
        valor_inicial = float(input('Entre com o valor de entrada, caso não tenha aperte ENTER: '))
        senha = input('Digite uma senha: ')
        nro_conta = self.criar_conta(nome, valor_inicial, senha)
        print(f'O numero da sua conta é: {nro_conta}')
        
    def fechar_conta(self):
        print(' *** FECHAR CONTA *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        if senha != self.dic_contas[numero_conta].senha:
            print('Senha incorreta!')
            return 0
        
        conta = self.dic_contas[numero_conta]
        saldo = conta.mostrar_saldo(senha)
        if saldo is not None:
            print(f'Voce tem R${saldo} na sua conta, que será retornado para voce.')
        del self.dic_contas[numero_conta]
        print('Sua conta está encerrada!')
        
    def mostrar_saldo(self):
        print(' *** SALDO *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        conta = self.dic_contas[numero_conta]
        saldo = conta.mostrar_saldo(senha)
        if saldo is not None:
            print(f'Seu saldo é {saldo}')
        else:
            print('Usuário não encontrado')

    def depositar(self):
        print(' *** DEPÓSITO *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        valor = float(input('Digite o valor que deseja depositar: '))
        conta = self.dic_contas[numero_conta]
        conta.deposito(valor, senha)
        saldo = conta.mostrar_saldo(senha)
        if saldo is not None:
            print(f'Seu saldo é {saldo}')
        else:
            print('Usuário não encontrado')

    def mostrar_contas(self):
        print(' *** MOSTRAR CONTAS *** ')
        for nro_conta in self.dic_contas.keys():
            print(f'Número da Conta {nro_conta}')
            self.dic_contas[nro_conta].mostrar()
            print('')
            
    def sacar(self):
        print(' *** SAQUE *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        valor = int(input('Digite o valor que deseja sacar: '))
        conta = self.dic_contas[numero_conta]
        conta.saque(valor, senha)
