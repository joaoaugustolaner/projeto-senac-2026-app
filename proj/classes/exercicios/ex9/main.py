from tamagotchi import BichinhoVirtual

if __name__ == '__main__':

    bicho = BichinhoVirtual('Luci')
    
    bicho.alimentar()
    assert bicho.fome == 35

    bicho.brincar()
    assert bicho.felicidade == 75

    