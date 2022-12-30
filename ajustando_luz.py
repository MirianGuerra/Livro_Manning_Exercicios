"""Ajustando a Luz"""

class AjustandoLuz():
    def __init__(self, status: bool, intensidade:int):
        self.intensidade = intensidade
        self.status = status
        
    def ligar(self):
        if self.status == True:
            print("Lampada já esta acesa")
        self.status = True
        
    def desligar(self):
        if self.status==False:
            print("Lapada está apagada") 
        self.status = False
        
    def aumentar_intensidade(self):
        if self.intensidade == 10:
            print("A lampada já está no máximo") 
        else:
            self.intensidade = self.intensidade +1
        
    def diminuir_intensidade(self):
        if self.intensidade == 0:
            print("A lampada já está no mínimo") 
        else:
            self.intensidade = self.intensidade -1
        
    def mostrar(self):
        print(f'Status: {self.status}')
        print(f'Intensidade: {self.intensidade}')
        
lampada1 = AjustandoLuz(True, 4)
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.aumentar_intensidade()
lampada1.mostrar()