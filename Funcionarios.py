class Funcionario():
    def __init__(self,nome: str, funcao:str, salario:float):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        
    def get_nome(self):
        return self.nome
    
    def get_funcao(self):
        return self.funcao
    
    def pagamento_anual(self):
        return (self.salario*13)
    
    
class Gerente(Funcionario):
    def __init__(self, nome, funcao, salario, lista_reports=None):
        self.salario = float(salario)
        if lista_reports is None:
            lista_reports=[]
        self.lista_reports = lista_reports
        #super().__init__(nome, funcao)
        Funcionario.__init__(self,nome,funcao,salario)
        
    def pagamento_anual(self, bonus = False):
        pagamento = self.salario*13
        if bonus:
            pagamento = pagamento+(0.10*pagamento)
            print(f'{self.nome} recebeu um bonus pelo ótimo trabalho!')
        return pagamento
    
    def get_reports(self):
        return self.lista_reports
        