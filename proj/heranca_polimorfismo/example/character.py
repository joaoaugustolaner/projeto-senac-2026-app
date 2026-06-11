



class Character:

    nome:str
    vida: float
    level:int = 1

    def __init__(self, nome:str, vida: float):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        raise NotImplementedError("Será implementado pela classe filha")
