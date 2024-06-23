lista_compras = []
menu = 0
menu2 = 0

while True:
    menu = int(input('What do you want to do: (1)add (2)delete (3)list:'))
    if menu == 1:
        lista_compras.append(input('Type the item list:'))
    elif menu == 2:
        menu2 = int(input('What is the indice, that you will be delete? '))
        if menu2 > len(lista_compras):
             print('Invalid number!')
        else:
            lista_compras.remove(lista_compras[menu2])
    elif menu == 3:
        for i, j in enumerate(lista_compras):
                print(i, j)

         
