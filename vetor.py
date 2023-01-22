#Classe Vetor: Treinando polimorfismo
import math

class Vetor():
    def __init__(self, x: int = 0, y:int = 0) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, outro_vetor):
        return Vetor(self.x + outro_vetor.x, self.y + outro_vetor.y)
    
    def __sub__(self, outro_vetor):
        return Vetor(self.x - outro_vetor.x, self.y - outro_vetor.y)
    
    def __mul__(self, outro_vetor):
        #Código pode aceitar outro vetor ou escalar
        if isinstance(outro_vetor, Vetor):
            return Vetor((self.x*outro_vetor.x), (self.y*outro_vetor.x))
        elif isinstance(outro_vetor, (int,float)):
            return Vetor((self.x*outro_vetor), (self.y*outro_vetor))
        else:
            raise TypeError('Segundo valor deve ser um vetor ou um escalar.')
        
    def __abs__(self):
        return math.sqrt((self.x**2)+(self.y**2))
    
    def __eq__(self, outro_vetor):
        return (self.x==outro_vetor.x) and (self.y == outro_vetor.y)
    
    def __ne__(self, outro_vetor):
        return not (self.x==outro_vetor.x) and (self.y == outro_vetor.y)

    def __lt__(self, outro_vetor):
        if abs(self) < abs(outro_vetor):
            return True
        else:
            return False
    def __gt__(self):
        if abs(self) > abs(outro_vetor):
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f'Esse vetor tem o valor {str(self.x)}, {str(self.y)}'