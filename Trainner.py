def numero(x):
    def multiplicador(y):
        return x * y
    return multiplicador
    
dobrar = numero(2)
triplicar = numero(3)
quadriplicar = numero(4)

print(dobrar(2))
print(triplicar(3))
print(quadriplicar(4))