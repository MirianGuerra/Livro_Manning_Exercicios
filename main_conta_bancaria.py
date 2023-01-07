from conta_bancaria import *

dic_conta = {}
proximo_numero_conta_dic = 0

conta = Conta('Mirian')
mirian_nro_conta = proximo_numero_conta_dic
dic_conta[mirian_nro_conta]=conta
print(f'O número da conta da Mirian é {mirian_nro_conta}')
proximo_numero_conta_dic +=1

conta=Conta('Bruno', 200, '123')
bruno_nro_conta = proximo_numero_conta_dic
dic_conta[bruno_nro_conta]=conta
print(f'O número da conta do Bruno é {bruno_nro_conta}')
proximo_numero_conta_dic +=1

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
    print()

    acao = input('Digite a letra correspondente ao que quer fazer: ')
    acao = acao.lower()
    print(acao)
    
    if acao == 'b':
        print(' *** SALDO *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        conta =dic_conta[numero_conta]
        saldo = conta.mostrar_saldo(senha)
        #saldo = (dic_conta[numero_conta].saldo(senha))
        #print(saldo)
        if saldo is not None:
            print(f'Seu saldo é {saldo}')
        else:
            print('Usuário não encontrado')
            
    elif acao == 'd':
        print(' *** DEPÓSITO *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        valor = int(input('Digite o valor que deseja depositar: '))
        dic_conta[numero_conta].deposito(valor, senha)
        
    elif acao == 'o':
        print(' *** ABRIR CONTA *** ')
        nome = input("Digite seu nome completo: ")
        valor = input('Entre com o valor de entrada, caso não tenha aperte ENTER: ')
        senha = input('Digite uma senha: ')
        conta = Conta(nome, valor, senha)
        nro_conta = proximo_numero_conta_dic
        print(f'O numero da sua conta é: {nro_conta}')
        proximo_numero_conta_dic += 1
        dic_conta[nro_conta] = conta
        dic_conta[nro_conta].mostrar()

    elif acao == 's':
        print(' *** SAQUE *** ')
        numero_conta, senha = pegando_nro_conta_e_senha()
        valor = int(input('Digite o valor que deseja sacar: '))
        conta = dic_conta[numero_conta]
        conta.saque(valor, senha)
        
    elif acao == 'm':
        print(' *** MOSTRAR CONTAS *** ')
        for nro_conta in dic_conta.keys():
            print(f'Número da Conta {nro_conta}')
            dic_conta[nro_conta].mostrar()
            print('')

    elif acao == 'q':
        break
       

