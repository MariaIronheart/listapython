#criando uma lista de núemros 
numeros = [10,20,30,40,50]

#inicializando a variável que ir´armazenar o maior número
maior_numero = numeros[0]

#usando um loop para percorrer a lista e encontrar o maior núemro
for numero in numeros:
    if numero > maior_numero:
      maior_numero = numero
      
print('O maior número na lista é: ', maior_numero)