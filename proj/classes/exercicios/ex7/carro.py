class Carro:
    modelo:str
    ano:int
    odometro: float = 0

    def __init__(self, modelo:str, ano:int):
        self.modelo = modelo
        self.ano = ano
    
    def viajar(self, distancia: float):
        if distancia < 0:
            return "A distância não pode ser negativa."

        self.odometro += distancia