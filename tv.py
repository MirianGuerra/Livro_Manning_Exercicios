"""TV
Power state (on or off)
Mute state (is it muted?)
List of channels available
Current channel setting
Current volume setting
Range of volume levels available
And the actions that the TV must provide include:
Turn the power on and off
Raise and lower the volume
Change the channel up and down
Mute and unmute the sound
Get information about the current settings
Go to a specified channel"""

class Tv():
    def __init__(self):
        self.estaLigado = False
        self.estaMudo = False
        self.listaCanais = [2,4,7,9,11,13]
        self.indexCanal = 0
        self.nCanais = len(self.listaCanais)
        self.volumeMaximo = 10
        self.volumeMinimo = 0
        self.volume = 5
        
    def ligar(self):
        self.estaLigado = not self.estaLigado
    
    def aumentarVolume(self):
        if not self.estaLigado:
            return
        if self.estaMudo:
            self.estaMudo = False
        if self.volume<self.volumeMaximo:
            self.volume = self.volume + 1
            
    def diminuirVolume(self):
        if not self.estaLigado:
            return
        if self.estaMudo:
            self.estaMudo = False
        if self.volume<self.volumeMaximo:
            self.volume = self.volume - 1
            
    def subirCanal(self):
        if not self.estaLigado:
            return
        if self.indexCanal>self.nCanais:
            self.indexCanal = 0
        self.indexCanal = self.indexCanal + 1
        
    def descerCanal(self):
        if not self.estaLigado:
            return
        if self.indexCanal<0:
            self.indexCanal = self.nCanais
        self.indexCanal = self.indexCanal - 1
        
    def mutar(self):
        if not self.estaLigado:
            return
        self.estaMudo=not self.estaMudo
        
    def definirCanal(self, novo_canal:str):
        if novo_canal in self.listaCanais:
            self.indexCanal=self.listaCanais.index(novo_canal)
            
    def mostrar_info(self):
        print(f'A TV está ligada? {self.estaLigado}')
        print(f'A TV está mutada? {self.estaMudo}')
        print(f'Qual é o canal? {self.listaCanais[self.indexCanal]}')
        print(f'Qual é o volume? {self.listaCanais[self.volume]}')


tv_bruno = Tv()
tv_bruno.ligar()
tv_bruno.subirCanal()
tv_bruno.aumentarVolume()
tv_bruno.mutar()
#tv_bruno.diminuirVolume()
tv_bruno.descerCanal()
tv_bruno.mostrar_info()

        
            