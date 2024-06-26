def mult(*args):
    result = 1
    for i in args:
        result *= i
    return result

def par_impar(x):
    result = ''
    if x % 2 == 0:
        result ='par'
    else:
        result = 'ímpar'
    return result

variavel = mult(7,5,9,25)
print(variavel)
print(par_impar(variavel))
