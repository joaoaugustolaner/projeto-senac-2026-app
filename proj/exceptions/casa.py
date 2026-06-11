from chave import Chave
from minha_excecao import ChaveErradaError

class Casa:

    def __init__(self, porta: int, chave: Chave):
        self.porta = int
        self.chave = chave

    def abrir_porta(self, chave: Chave):

        if chave.codigo != 1234:
            raise ChaveErradaError(f'Código da chave incorreto, o código informado foi: {chave.codigo}')
        return 'Ṕorta aberta com sucesso'
        

    def troca_chave(self, chave: Chave):
        self.chave.codigo = chave.codigo
        return True
