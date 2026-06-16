class Usuario:
    pass

class Comum(Usuario):
    pass

class Admin(Usuario):
    pass

def deletar_banco_de_dados(usuario_objeto):
    if not isinstance(usuario_objeto, Admin):
        raise PermissionError('Você deve ser ADMIN para executar essa operação')
    

if __name__ == '__main__':

    comum = Comum()
    admin = Admin()

    deletar_banco_de_dados(comum)
