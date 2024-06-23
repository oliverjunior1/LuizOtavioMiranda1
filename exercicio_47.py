user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espacos')
    else:
        print(f'Seu nome não contém espaços.')

else:
    print('Desculpe, você dixou campos vazios.')

