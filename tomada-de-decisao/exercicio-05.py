''' 5 - Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas. '''


# Primeiro, irei pedir os comprimentos dos três lados do triângulo à pessoa usuária:
lado1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
lado2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
lado3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))

# Depois verifico o tipo de triângulo
if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')