class BichinhoVirtual:

    nome:str

    def __init__(self, nome:str):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50

    def alimentar(self):
        if self.fome - 15 >= 0:
            self.fome -= 15
        else:
            self.fome = 0
        
        if self.felicidade + 5 > 100:
            self.felicidade = 100
        else:
            self.felicidade += 5
        
        

    def brincar(self):
        if self.felicidade + 20 > 100:
            self.felicidade = 100
        else:
            self.felicidade += 20

        self.fome += 10

