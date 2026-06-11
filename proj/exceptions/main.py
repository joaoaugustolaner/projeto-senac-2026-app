from casa import Casa
from chave import Chave
from minha_excecao import ChaveErradaError

if __name__ == '__main__':

    chave = Chave()
    casa = Casa(1234, chave)

    try:
        casa.abrir_porta(chave)
    except ChaveErradaError:
        print('Trocando o código da chave...')
        chave.troca_codigo(1234)
        print(casa.abrir_porta(chave))
        

        
    
