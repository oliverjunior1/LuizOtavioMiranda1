while True:
    number1 =int(input('Enter the first number: '))
    operador =input('Enter the operator: ')
    number2 =int(input('Enter the second number: '))
    if operador == '*':
        calculo = number1 * number2
        name_operator= 'multiplication'
    elif operador== '/':
        calculo = number1 / number2
        name_operator= 'division'
    elif operador == '+':
        calculo = number1 + number2
        name_operator = 'sum'
    elif operador == '-':
        calculo = number1 - number2
        name_operator = 'subtration'
    else:
        print('Invalid Character!' )
        break

    print(f'The {name_operator} from the numbers {number1} and {number2} is {calculo}.')