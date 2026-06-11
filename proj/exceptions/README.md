# Lista de Exercícios: Erros e Exceções em Python

Esta lista foi projetada para consolidar os conhecimentos acumulados de lógica, coleções e orientação a objetos, integrando-os com técnicas robustas de tratamento de erros (`try/except`) e criação de exceções customizadas.

---

## 🟢 Nível: Super Fácil (Para entender o conceito)

### 1. Protegendo a Divisão por Zero
* **Assinatura:** `def dividir_numeros(a, b):`
* **Lógica:** A função deve tentar realizar a divisão do número `a` por `b`. Caso o usuário tente passar o valor zero no segundo parâmetro, capture o erro de divisão por zero nativo do Python (`ZeroDivisionError`) e retorne a mensagem textual: *"Erro: Não é possível dividir por zero."*

### 2. Conversão Segura de Tipos
* **Assinatura:** `def converter_para_inteiro(texto):`
* **Lógica:** O código deve tentar converter a string recebida em um número inteiro e retornar esse número. Se a string contiver letras ou caracteres inválidos para a conversão, capture o erro de valor (`ValueError`) e retorne textualmente: *"Conversão inválida."*

### 3. Minha Primeira Exceção Customizada
* **Assinatura:** `class ErroDeEntradaInvalida(Exception):`
* **Lógica:** Crie uma classe de erro customizada que herda da classe base de exceções do Python. Não adicione nenhuma lógica interna nela, utilize apenas a palavra-chave de omissão (`pass`).

### 4. Disparando Erros Manuais
* **Assinatura:** `def verificar_sinal(numero):`
* **Lógica:** Receba um número. Se o número for menor do que zero, use a palavra-chave adequada (`raise`) para disparar a exceção nativa `ValueError` contendo o texto explicativo: *"O número não pode ser negativo."*

---

## 🔵 Nível: Fácil (Para se familiarizar)

### 5. Acessando Índices de Listas com Segurança
* **Assinatura:** `def obter_elemento(lista, indice):`
* **Lógica:** A função deve tentar acessar e retornar o valor localizado no índice informado. Se o índice não existir dentro da lista, capture a exceção de índice fora do limite (`IndexError`) e retorne a mensagem: *"Posição inexistente."*

### 6. Condicionais Combinadas com Exceções
* **Assinatura:** `def validar_usuario(nome):`
* **Lógica:** Se o nome recebido for uma string vazia ou contiver menos de 3 caracteres, force o disparo de um `ValueError`. Caso contrário, retorne textualmente: *"Usuário válido."*

### 7. Capturando Múltiplos Erros Individuais
* **Assinatura:** `def processar_dados(lista, indice):`
* **Lógica:** O código deve tentar pegar o elemento da lista naquele índice e dividi-lo por 2. Monte uma estrutura que capture especificamente o erro de índice (`IndexError`) em um bloco, e o erro de tipo/valor caso o elemento não seja um número em outro bloco de `except` separado.

### 8. Lógica de Erro em Construtores de Classes
* **Assinatura:** Classe `Produto` com `def __init__(self, nome, preco):`
* **Lógica:** Crie o construtor da classe recebendo o nome e o preço do produto. Se o preço informado for menor ou igual a zero, o construtor deve disparar imediatamente um `ValueError`, impedindo que o objeto chegue a ser instanciado na memória.

### 9. Usando o Bloco Finally
* **Assinatura:** `def simular_banco_de_dados(comando):`
* **Lógica:** A função deve tentar rodar um print com o comando SQL simulado. Caso ocorra qualquer erro genérico no processo, capture-o. Independentemente de dar erro ou funcionar com sucesso, use a estrutura `finally` para exibir sempre no final a mensagem: *"Conexão encerrada."*

### 10. Exceção Customizada de Idade
* **Assinatura:** `class IdadeInvalidaError(Exception):` e `def cadastrar_eleitor(idade):`
* **Lógica:** Crie a classe de erro customizada. Na função, se a idade passada por parâmetro for menor que 16, dispare o seu erro `IdadeInvalidaError`.

---

## 🟠 Nível: Médio (Misturando Conceitos)

### 11. O Som Polimórfico Protegido
* **Assinatura:** Classe mãe `Instrumento` com `def tocar(self):` e classe filha `Guitarra(Instrumento)`.
* **Lógica:** Crie uma exceção customizada chamada `AnatomiaError`. Na classe mãe, o método `tocar` deve disparar esse erro avisando que classes abstratas não tocam som. Na subclasse `Guitarra`, sobrescreva o método para retornar o texto do instrumento funcionando. Teste chamar o método de ambos protegendo com `try/except`.

### 12. Buscando Chaves por Índice de Texto
* **Assinatura:** `def buscar_letra_na_lista(lista_de_strings, indice_lista, indice_palavra):`
* **Lógica:** Acesse a lista no primeiro índice informado e, a partir da palavra encontrada, busque a letra correspondente ao segundo índice. Trate as duas falhas possíveis (`IndexError` da lista ou da string) usando um único bloco de captura genérico, mas exiba a mensagem nativa do erro (`str(erro)`) na tela.

### 13. Cadastro de Alunos com Notas Seguras
* **Assinatura:** `def adicionar_nota_aluno(lista_notas, nova_nota):`
* **Lógica:** A função deve verificar através de condicionais se a nota está entre 0.0 e 10.0. Se não estiver, lança um `ValueError`. Se o tipo do dado passado não for compatível com operações matemáticas, capture a exceção `TypeError` e exiba um aviso de tipo incorreto.

### 14. Elevador e Limite de Carga
* **Assinatura:** Classe `Elevador` com `def entrar_pessoa(self, peso_pessoa):`
* **Lógica:** O elevador inicia com o atributo `peso_total = 0`. Ao chamar o método, verifique se a soma do peso atual com o da nova pessoa ultrapassa 400. Se passar, dispare uma exceção customizada chamada `ElevadorSobrecargadoError` e não altere o peso real do objeto.

### 15. Calculadora Científica Experimental
* **Assinatura:** `def calcular_raiz_quadrada(numero):`
* **Lógica:** Caso o número recebido seja negativo, use condicionais para disparar uma exceção própria chamada `NumeroNegativoError`. Caso passem um caractere de texto que quebre o cálculo, capture o erro de tipo tradicional do Python.

---

## 🔴 Nível: Difícil (Cenários Reais)

### 16. O Banco e a Exceção de Saldo Insuficiente
* **Assinatura:** `class SaldoInsuficienteError(Exception):` e classe `ContaBancaria` com `def sacar(self, valor):`
* **Lógica:** A classe de erro customizada deve aceitar um parâmetro no construtor para guardar quanto saldo faltou. Na classe da conta, o método de saque deve testar se há dinheiro suficiente. Se faltar dinheiro, calcule a diferença e dispare o seu erro customizado passando essa diferença.

### 17. Validando Herança de Atributos Críticos
* **Assinatura:** Classes `Usuario`, `Admin(Usuario)`, `Comum(Usuario)` e a função `deletar_banco_de_dados(usuario_objeto):`
* **Lógica:** A função recebe o objeto de um usuário. Utilizando a função nativa `isinstance()`, teste se o objeto pertence à classe `Admin`. Caso pertença a classe `Comum` ou outra, force o disparo de um erro de permissão nativo do Python (`PermissionError`) com um texto de alerta.

### 18. Sistema de Login com Tentativas Limitadas
* **Assinatura:** Classe `Autenticador` com `def fazer_login(self, senha_digitada):`
* **Lógica:** A classe possui os atributos internos `senha_correta = "1234"` e `tentativas = 0`. A cada erro de senha no método, adicione 1 ao contador e dispare um `ValueError`. Se o contador atingir 3 tentativas, qualquer execução futura do método deve disparar diretamente uma exceção customizada chamada `ContaBloqueadaError`.

---

## 🔥 Nível: Desafio Lendário (Especialistas)

### 19. Simulador de Inventário de RPG com Polimorfismo Restrito
* **Assinatura:** Classes `Item`, `Espada(Item)`, `Pocao(Item)`, `PedraComum(Item)` e a classe `Inventario` com `def guardar_item(self, objeto_item):`
* **Lógica:** A classe `Inventario` possui uma lista interna. O método de guardar deve receber qualquer objeto derivado de `Item` e adicioná-lo à lista. No entanto, se o objeto recebido for especificamente da classe `PedraComum`, o método deve rejeitar a inclusão disparando uma exceção própria chamada `ItemInutilException`. Adicionalmente, se o tamanho da lista do inventário já for maior que 3, ele deve disparar um `InventarioCheioException`.

### 20. Processador de Transações Financeiras em Lote
* **Assinatura:** `def processar_lote_saques(conta_objeto, lista_de_valores):`
* **Lógica:** Esta função recebe um objeto de `ContaBancaria` (da questão 16) e uma lista contendo múltiplos valores numéricos de saques misturados propositalmente com algumas strings inválidas. A função deve percorrer a lista inteira tentando efetuar os saques. Se encontrar uma string, deve capturar o erro de tipo, exibir um aviso no terminal e continuar o laço para o próximo item. Contudo, se a conta disparar o erro customizado `SaldoInsuficienteError`, a função deve interromper imediatamente o lote inteiro (`break`) e salvar em uma lista separada todos os saques que deixaram de ser executados por falta de fundos.
