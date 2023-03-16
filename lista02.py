#criando uma lista
minha_lista = [1,2,3,4,5]
#usando um loop for para percorrer a lista e imprimir cada elemento
for i in range(len(minha_lista)):
    print('O elemento', i+1, ' da lista é: ', minha_lista[i])

#criando uma lista de numeros
numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero, ' - com for')
    
#usando um loop while para percorrer a lista e imprimir cada elemento
i = 0
while i < len(numeros):
    print(numeros[i], ' com while')
    i += 1 #esse comando adiciona valor ao i que inicialmente é 0