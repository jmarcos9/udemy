class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, per):
        self.preco = self.preco - (self.preco * (per / 100))


p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 100)
p2.desconto(20)
print(p2.preco)