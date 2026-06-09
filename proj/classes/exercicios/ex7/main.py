from carro import Carro

if __name__ == '__main__':

    carro = Carro('uno', 2011)
    assert carro.viajar(-2) == "A distância não pode ser negativa."

    carro.viajar(10)
    assert carro.odometro == 10

    carro.viajar(2)
    assert carro.odometro == 12