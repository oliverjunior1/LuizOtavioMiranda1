CPF = input('Type your CPF with only numbers: ')

i = 10
j = 0
lista = []
sum = 0
while i >= 2:
   CPF_int = int(CPF[j])
   lista.append(int(CPF_int*i))
   j += 1
   i -= 1

for x in lista:
   sum += x

rest = (sum * 10)% 11
if rest > 9:
   rest = 0

print(rest)
if rest == int(CPF[9]):
   print('Valid CPF')
else:
   print('Invalid CPF')
