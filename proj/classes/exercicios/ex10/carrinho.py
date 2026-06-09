class CarrinhoDeCompras:

    def __init__(self):
        self.items = []
        self.precos = []


    def adicionar_item(self, nome_produto:str, preco_produto:float):
        self.items.append(nome_produto)
        self.precos.append(preco_produto)

    def calcular_total(self):
        soma = 0
        for preco in self.precos:
           soma += preco
        return soma
    
        # ou return sum(self.precos)