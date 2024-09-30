import unittest

class Produto:
    def __init__(self, nome, preco, quantidade):
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço e quantidade devem ser não negativos.")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade deve ser não negativa.")
        self.quantidade = quantidade

    def atualizar_preco(self, preco):
        if preco < 0:
            raise ValueError("Preço deve ser não negativo.")
        self.preco = preco

    def valor_total(self):
        return self.preco * self.quantidade

class TestProduto(unittest.TestCase):
    def test_criacao_produto_valido(self):
        produto = Produto("Produto A", 10, 5)
        self.assertEqual(produto.nome, "Produto A")
        self.assertEqual(produto.preco, 10)
        self.assertEqual(produto.quantidade, 5)

    def test_criacao_produto_preco_negativo(self):
        with self.assertRaises(ValueError):
            Produto("Produto B", -10, 5)

    def test_criacao_produto_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            Produto("Produto C", 10, -5)

    def test_atualizar_quantidade_valida(self):
        produto = Produto("Produto D", 10, 5)
        produto.atualizar_quantidade(10)
        self.assertEqual(produto.quantidade, 10)

    def test_atualizar_quantidade_negativa(self):
        produto = Produto("Produto E", 10, 5)
        with self.assertRaises(ValueError):
            produto.atualizar_quantidade(-10)

    def test_atualizar_preco_valido(self):
        produto = Produto("Produto F", 10, 5)
        produto.atualizar_preco(20)
        self.assertEqual(produto.preco, 20)

    def test_atualizar_preco_negativo(self):
        produto = Produto("Produto G", 10, 5)
        with self.assertRaises(ValueError):
            produto.atualizar_preco(-20)

    def test_valor_total(self):
        produto = Produto("Produto H", 10, 5)
        self.assertEqual(produto.valor_total(), 50)

if __name__ == '__main__':
    unittest.main()
