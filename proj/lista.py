# Exercício 1
frutas = ['maçã', 'banana', 'laranja', 'morango']

def primeira_fruta(frutas: list):
    return frutas[0]

# Exercício 2
animais = ['gato', 'cachorro', 'passarinho', 'coelho']

def ultimo_animal(animais: list):
    return animais[-1]

#Exercício 3:
compras = []

def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')

    return compras

# Exercício 4
notas = [7.5, 8.0, 6.0, 9.5, 10.0]
def quantidade_notas(notas: list):
    return len(notas)

#Exercício 5
cores = ['vermelho', 'verde', 'azul']

def mudar_cor(cores: list):
    indice = cores.index('verde')
    cores[indice] = 'amarelo'
    return cores

#Exercício 6
tarefas = ['estudar', 'limpar quarto', 'lavar louça']
def esvaziar_tarefas(tarefas: list):
    tarefas.clear()
    return tarefas

#Exercício 7
respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']
def contar_sim(respostas: list):
    return respostas.count('Sim')

#Exercício 8
fila = ['Ana', 'Bruno', 'Carlos', 'Diego']
def remover_ultimo(fila: list):
    return fila.pop()

#Exercício 9
canais = ['Globo', 'SBT', 'Record', 'Band']

def posicao_sbt(canais: list):
    return canais.index('SBT')

# Exercício 10
dias = ['Segunda', 'Quarta', 'Quinta']
def ajustar_terca(dias: list):
    dias.insert(1, 'Terça')
    return dias


##################################### Médio ################################

# Exercício 11
numeros = [10, 20, 30, 40, 50, 60]
def tres_primeiros(numeros: list):
    return numeros[:3]

# Exercício 12
convidados = ['Alice', 'Bob', 'Arthur', 'Carol']
def remover_arthur(convidados: list):
    if 'Arthur' in convidados:
        convidados.remove('Arthur')
        return convidados
    
    return "Nome não encontrado."

# Exercício 13
letras = ['A', 'B', 'C', 'D', 'E']
def inverter_lista(letras: list):
    letras.reverse()
    return letras

# Exercício 14
pontos = [45, 12, 89, 5, 23]
def ordenar_pontos(pontos: list):
    pontos.sort()
    return pontos

# Exercício 15
valores = [12, 5, 8, 22, 9, 15]
def soma_extremos(valores: list):
    return valores[0] + valores[-1]

# Exercício 16
ingredientes = ['ovo', 'farinha', 'açúcar', 'leite']
def tem_chocolate(ingredientes:list):
    if 'chocolate' in ingredientes:
        return True
    return False

# Exercício 17
amigos_escola = ['Pedro', 'Lucas']
amigos_bairro = ['Mariana', 'Julia']

def juntar_amigos(amigos_escola: list, amigos_bairro: list):
    amigos_escola.extend(amigos_bairro)
    return amigos_escola

# Exercício 18
anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
def ultimos_tres(anos: list):
    return anos[-3:]

##################################### Difícil ################################

# Exercício 19
brinquedos = ['carrinho', 'boneca', 'bola', 'pião']
def remover_brinquedo_seguro(brinquedos:list, item:str):
    if item in brinquedos:
        brinquedos.remove(item)
        return brinquedos
    return 'Este brinquedo não está na lista!'

# Exercício 20
numeros_para_trocar = [1,2,3,4]
def trocar_extremos(numeros_para_trocar: list):

    numeros_para_trocar[0], numeros_para_trocar[-1] =  numeros_para_trocar[-1], numeros_para_trocar[0]
    
    # ou
    
    # numero_comeco = numeros_para_trocar[0]
    # numeros_para_trocar[0] = numeros_para_trocar[-1]
    # numeros_para_trocar[-1] = numero_comeco

    return numeros_para_trocar
    

if __name__ == '__main__':
    print("Resultado exercício 1: ")
    fruta = primeira_fruta(frutas)
    print(fruta)

    print("\n Resultado exercício 2:")
    animal = ultimo_animal(animais)
    print(animal)

    print("\n Resultado exercício 3:")
    lista_compras = adicionar_compras(compras)
    print(lista_compras)

    print("\n Resultado exercício 4:")
    print(quantidade_notas(notas))

    print("\n Resultado exercício 5:")
    lista_cores = mudar_cor(cores)
    print(lista_cores)

    print("\n Resultado exercício 6:")
    lista_tarefas_vazia = esvaziar_tarefas(tarefas)
    print(lista_tarefas_vazia)

    print("\n Resultado exercício 7:")
    contagem_sim = contar_sim(respostas)
    print(contagem_sim)

    print("\n Resultado exercício 8:")
    pessoa_removida = remover_ultimo(fila)
    print(pessoa_removida)

    print("\n Resultado exercício 9:")
    indice_sbt = posicao_sbt(canais)
    print(indice_sbt)

    print("\n Resultado exercício 10:")
    semana = ajustar_terca(dias)
    print(semana)

    print("\n Resultado exercício 11:")
    tres_numeros = tres_primeiros(numeros)
    print(tres_numeros)

    print("\n Resultado exercício 12:")
    lista_sem_arthur = remover_arthur(convidados)
    print(lista_sem_arthur)

    print("\n Resultado exercício 13:")
    lista_inversa = inverter_lista(letras)
    print(lista_inversa)

    print("\n Resultado exercício 14:")
    lista_ordenada = ordenar_pontos(pontos)
    print(lista_ordenada)

    print("\n Resultado exercício 15:")
    soma_ext = soma_extremos(valores)
    print(soma_ext)
    
    print("\n Resultado exercício 16:")
    chocolate = tem_chocolate(ingredientes)
    print(chocolate)

    print("\n Resultado exercício 17:")
    amigos = juntar_amigos(amigos_escola, amigos_bairro)
    print(amigos)

    print("\n Resultado exercício 18:")
    ultimos_tres_anos = ultimos_tres(anos)
    print(ultimos_tres_anos)

    print("\n Resultado exercício 19:")
    brinquedo_removido = remover_brinquedo_seguro(brinquedos, 'pião')
    print(brinquedo_removido)
    mensagem = remover_brinquedo_seguro(brinquedos, 'lego')
    print(mensagem)

    print("\n Resultado exercício 20:")
    lista_extremos_trocados = trocar_extremos(numeros_para_trocar)
    print(lista_extremos_trocados)

