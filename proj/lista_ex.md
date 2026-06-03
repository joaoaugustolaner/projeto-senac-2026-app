# Lista de Exercícios: Listas e Métodos em Python
---

### 1. Acessando o primeiro elemento (Fácil)
**Contexto:**
Dada a lista de frutas: `frutas = ['maçã', 'banana', 'laranja', 'morango']`

**Enunciado:**
Crie uma função chamada `primeira_fruta(frutas)` que receba essa lista e retorne apenas o primeiro elemento dela.

---

### 2. Acessando o último elemento (Fácil)
**Contexto:**
Dada a lista de animais: `animais = ['gato', 'cachorro', 'passarinho', 'coelho']`

**Enunciado:**
Crie uma função chamada `ultimo_animal(animais)` que receba a lista e retorne o último animal usando um índice negativo.

---

### 3. Adicionando itens com append() (Fácil)
**Contexto:**
Você tem uma lista de compras inicialmente vazia: `compras = []`

**Enunciado:**
Crie uma função chamada `adicionar_compras(compras)` que adicione os elementos `'arroz'`, `'feijão'` e `'batata'` à lista usando o método `.append()`. A função deve retornar a lista atualizada.

---

### 4. Tamanho da lista (Fácil)
**Contexto:**
Dada a lista de notas de um aluno: `notas = [7.5, 8.0, 6.0, 9.5, 10.0]`

**Enunciado:**
Crie uma função chamada `quantidade_notas(notas)` que use a função `len()` para descobrir quantas notas existem na lista e retorne esse valor.

---

### 5. Substituindo elementos (Fácil)
**Contexto:**
Dada a lista de cores: `cores = ['vermelho', 'verde', 'azul']`

**Enunciado:**
Crie uma função chamada `mudar_cor(cores)` que altere a cor `'verde'` para `'amarelo'` alterando o elemento diretamente pelo seu índice. Retorne a lista modificada.

---

### 6. Limpando a lista com clear() (Fácil)
**Contexto:**
Dada a lista de tarefas antigas: `tarefas = ['estudar', 'limpar quarto', 'lavar louça']`

**Enunciado:**
Crie uma função chamada `esvaziar_tarefas(tarefas)` que use o método `.clear()` para apagar todos os itens da lista e retorne a lista vazia.

---

### 7. Contando ocorrências com count() (Fácil)
**Contexto:**
Dada a lista de respostas de um quiz: `respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']`

**Enunciado:**
Crie uma função chamada `contar_sim(respostas)` que utilize o método `.count()` para contar quantas vezes a palavra `'Sim'` aparece na lista e retorne essa contagem.

---

### 8. Removendo o último elemento com pop() (Fácil)
**Contexto:**
Dada a lista de participantes de uma fila: `fila = ['Ana', 'Bruno', 'Carlos', 'Diego']`

**Enunciado:**
Crie uma função chamada `remover_ultimo(fila)` que remova o último elemento da lista usando o método `.pop()`. A função deve retornar o nome da pessoa removida.

---

### 9. Descobrindo a posição com index() (Fácil)
**Contexto:**
Dada a lista de canais de TV: `canais = ['Globo', 'SBT', 'Record', 'Band']`

**Enunciado:**
Crie uma função chamada `posicao_sbt(canais)` que use o método `.index()` para encontrar em qual índice (posição) a palavra `'SBT'` está localizada e retorne esse índice.

---

### 10. Inserindo em uma posição específica com insert() (Fácil)
**Contexto:**
Dada a lista de dias da semana: `dias = ['Segunda', 'Quarta', 'Quinta']`

**Enunciado:**
Crie uma função chamada `ajustar_terca(dias)` que insira o elemento `'Terça'` exatamente no índice 1 (entre Segunda e Quarta) usando o método `.insert()`. Retorne a lista modificada.

---

### 11. Fatiando a lista (Slicing básico) (Médio)
**Contexto:**
Dada a lista de números: `numeros = [10, 20, 30, 40, 50, 60]`

**Enunciado:**
Crie uma função chamada `tres_primeiros(numeros)` que use o operador de fatiamento (`[:]`) para retornar apenas os três primeiros números da lista.

---

### 12. Removendo um elemento específico com remove() (Médio)
**Contexto:**
Dada a lista de convidados: `convidados = ['Alice', 'Bob', 'Arthur', 'Carol']`

**Enunciado:**
Crie uma função chamada `remover_arthur(convidados)` que remova o nome `'Arthur'` da lista usando o método `.remove()`. Retorne a lista atualizada.

---

### 13. Inverting a ordem com reverse() (Médio)
**Contexto:**
Dada a lista de letras: `letras = ['A', 'B', 'C', 'D', 'E']`

**Enunciado:**
Crie uma função chamada `inverter_lista(letras)` que utilize o método `.reverse()` para inverter a ordem dos elementos da lista e a retorne modificada.

---

### 14. Ordenando números com sort() (Médio)
**Contexto:**
Dada a lista de pontuações desordenadas: `pontos = [45, 12, 89, 5, 23]`

**Enunciado:**
Crie uma função chamada `ordenar_pontos(pontos)` que ordene essa lista de forma crescente (do menor para o maior) usando o método `.sort()` e retorne a lista ordenada.

---

### 15. Somando extremos da lista (Médio)
**Contexto:**
Dada uma lista com números inteiros: `valores = [12, 5, 8, 22, 9, 15]`

**Enunciado:**
Crie uma função chamada `soma_extremos(valores)` que pegue o primeiro e o último elemento da lista, some os dois e retorne o resultado dessa soma.

---

### 16. Verificando existência (Médio)
**Contexto:**
Dada a lista de ingredientes da receita: `ingredientes = ['ovo', 'farinha', 'açúcar', 'leite']`

**Enunciado:**
Crie uma função chamada `tem_chocolate(ingredientes)` que verifique se o ingrediente `'chocolate'` está dentro da lista. Se estiver, retorne `True`; se não, retorne `False`.

---

### 17. Juntando duas listas com extend() (Médio)
**Contexto:**
Você tem duas listas de amigos: `amigos_escola = ['Pedro', 'Lucas']` e `amigos_bairro = ['Mariana', 'Julia']`

**Enunciado:**
Crie uma função chamada `juntar_amigos(amigos_escola, amigos_bairro)` que use o método `.extend()` para colocar todos os amigos do bairro dentro da lista de amigos da escola. Retorne a lista de amigos da escola atualizada.

---

### 18. Fatiamento final (Slicing final) (Médio)
**Contexto:**
Dada a lista de anos: `anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]`

**Enunciado:**
Crie uma função chamada `ultimos_tres(anos)` que use fatiamento (`[:]`) com índices negativos para retornar apenas os 3 últimos anos da lista.

---

### 19. Remoção Segura com Condicional (Difícil)
**Contexto:**
Dada uma lista de brinquedos: `brinquedos = ['carrinho', 'boneca', 'bola', 'pião']`

**Enunciado:**
Crie uma função chamada `remover_brinquedo_seguro(brinquedos, item)` que recebe a lista e o nome de um brinquedo para remover. Se o brinquedo estiver na lista, remova-o usando `.remove()` e retorne a lista modificada. Se não estiver, não mude nada e retorne a string `'Este brinquedo não está na lista!'`.

---

### 20. Substituição Dinâmica de Extremos (Difícil)
**Contexto:**
Dada uma lista qualquer de números ou strings contendo pelo menos 2 elementos.

**Enunciado:**
Crie uma função chamada `trocar_extremos(lista)` que inverta de lugar o primeiro e o último elemento dessa lista entre si. Por exemplo, se a lista for `[1, 2, 3, 4]`, ela deve se transformar em `[4, 2, 3, 1]`. Você deve alterar a própria lista usando atribuição por índices e retornar a lista modificada.

---
