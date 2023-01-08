from conta_bancaria import *
from banco import *

banco = Banco()

nro_conta_mirian = banco.criar_conta('Mirian', )
print(f'O numero da conta é {nro_conta_mirian}')

nro_conta_bruno=banco.criar_conta('Bruno', 200, '123')
print(f'O numero da conta é {nro_conta_bruno}')

def pegando_nro_conta_e_senha():
    numero_conta = int(input('Entre com seu número de conta: '))
    senha = input('Entre com a senha: ')
    return numero_conta, senha


while True:
    print()
    print('Pressione b para mostrar o saldo.')
    print('Pressione d para deposito.')
    print('Pressione o para abrir uma nova conta.')
    print('Pressione s para saque.')
    print('Pressione m para mostrar todas as contas.')
    print('Pressione q para sair.')
    print('Pressione f para fechar sua conta.')
    print()

    acao = input('Digite a letra correspondente ao que quer fazer: ')
    acao = acao.lower()
    print(acao)
    
    if acao == 'b':
        banco.mostrar_saldo()
            
    elif acao == 'd':
        banco.depositar()
        
    elif acao == 'o':
        banco.abrir_conta()

    elif acao == 's':
        banco.sacar()
        
    elif acao == 'm':
        banco.mostrar_contas()

    elif acao == 'f':
        banco.fechar_conta()

    elif acao == 'q':
        break
    
    else:
        print('Essa não é uma ação válida, tente novamente.')
       

