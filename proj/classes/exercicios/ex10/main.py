from carrinho import CarrinhoDeCompras

if __name__ == '__main__':

    carrinho_de_compras = CarrinhoDeCompras()
    
    carrinho_de_compras.adicionar_item('leite', 3.00)
    carrinho_de_compras.adicionar_item('farinha', 2.69)

    assert int(carrinho_de_compras.calcular_total()) == 5

    