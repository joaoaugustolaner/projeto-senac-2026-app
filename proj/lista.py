#!/bin/usr/env python3

## Comentário:
##
## Esse arquivo mostra métodos comuns em listas em python
## e uma breve descrição do que eles fazem.
## Os exemplos serão feitos usando uma cesta de frutas, como exemplo.

cesta_de_frutas = ['banana', 'caqui', 'maçã', 'bergamota', 'abacaxi', 'laranja']

## 1
## Para adicionar um elemento usamos o método `append`.
## É importanate salientar que o tipo do dado deve ser o mesmo
cesta_de_frutas.append('lima')

## 2
## Para remover todos os elementos de uma lista, usamos o método `clear`
cesta_de_frutas.clear()

## 3
## Para percorrer uma lista podemos usar um bloco `for`
## Esse código percorre toda a lista e printa qual é a fruta
for fruta in cesta_de_frutas:
    print(fruta)

## 4
## Para remover um tipo de fruta usaremos uma técnica que percorre a lista e procura por uma fruta,
## se existir, então remove;

for fruta in cesta_de_frutas:
    if fruta == 'banana':
        cesta_de_frutas.remove(fruta)

## 5        
## Para separar a lista em diferentes tamanhos podemos, por exemplo, usar índices a nosso favor
## junto de uma estrutura `while` ou ainda em uma estrutura `for`. Deixarei ambos exemplos abaixo:

# for
nova_cesta = []
for fruta in cesta_de_frutas:
    if cesta_de_frutas.index(fruta) % 2 == 0:
        nova_cesta.append(fruta)
        cesta_de_frutas.remove(fruta)

# while
nova_cesta = []
index = 0 
while (index < len(cesta_de_frutas)):
    if index % 2 == 0:
        nova_cesta.append(cesta_de_frutas[index])
        cesta_de_frutas.remove(cesta_de_frutas[index])

## 6
## Para mover um tipo de fruta da cesta, para outra cesta,
## podemos usar um código parecido com o código do ex. 4

nova_cesta = []
for fruta in cesta_de_frutas:
    if fruta == 'maçã':
        nova_cesta.append(fruta)
        cesta_de_frutas.remove(fruta)

## 7
## Para remover uma fruta do final da lista  podemos usar o método `pop`
## ou remover o elemento com último índice que acessamos com o índice [-1]
cesta_de_frutas.pop()
cesta_de_frutas.remove(cesta_de_frutas[-1])

## 8
## Para remover do ínicio
