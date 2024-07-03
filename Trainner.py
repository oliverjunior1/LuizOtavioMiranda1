# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]
# novo_produto = [
#     {**produto, 'preco': round(produto['preco']*1.1,2)}
#     for produto in produtos
# ]
# print(novo_produto)

class Car:
    def __init__(self, acelerar, velocidade):
        self.acelerar = acelerar
        self.velocidade = velocidade
fusca = Car('acelering', 80)
ferrari = Car('acelering', 200)

print(f'The fusca is {fusca.acelerar} at {fusca.velocidade}km/h.')
print(f'The Ferrari is {ferrari.acelerar} at {ferrari.velocidade}km/h.')


