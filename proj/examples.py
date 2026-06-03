################# Exercícios (1ª aula) #################


def calcula_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")


def converte_temperatura_fahrenreit(graus_celsius: float):
    temperatura = (graus_celsius * (9 / 5)) + 32
    print(f"A temperatura em fahrenreit é: {temperatura}")


def converte_em_dolares(reais: float):
    dolares = reais / 5.04
    print(f"O valor em dólares é: {dolares}")


################# Exercícios (2ª aula) #################


def classificar_pop(idade: int) -> str:

    if idade <= 12:
        return "Criança"

    if idade > 12 and idade < 18:
        return "Adolescente"

    if idade >= 18 and idade <= 60:
        return "Adulto"

    return "Idoso"


def tipo_triangulo(lado1: float, lado2: float, lado3: float):
    if (lado1 + lado2) > lado3 \
        or (lado3 + lado2) > lado1 \
            or (lado1 + lado3) > lado2:
        
        if lado1 == lado2 == lado3:
            return "Equilátero"
        if (lado1 != lado2 != lado3): 
            return "Escaleno"
        return "Isóceles"

def aprovar_saque(saldo:float, valor_saque:float):
    if valor_saque <= saldo and valor_saque % 10 == 0:
        return True
    return False

def verifica_membro_do_clube(nome:str, idade:int) -> str:
    if nome != "João" and idade < 28:
        return "Você não é membro do clube"
    
    return "Bem vindo ao clube!"
