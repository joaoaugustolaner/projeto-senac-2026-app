class Pessoa:

    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome


if __name__ == '__main__':
    
    

    while(True):

        print("1 - Criar pessoa: ")
        print("2 - Mostrar pessoa: ")
        print("3 - Sair! ")

        escolha = int(input("\n Escolha uma opção: "))

        if escolha == 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input(f"Digite a idade de {nome}: "))

            pessoa = Pessoa(nome, idade)

        if escolha == 2:
            print(f"O nome da pessoa é: {pessoa.nome} e a idade é {pessoa.idade}")

        if escolha == 3:
            break

