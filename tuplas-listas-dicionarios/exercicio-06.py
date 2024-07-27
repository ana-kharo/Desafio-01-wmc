''' 6 - Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.'''

# Primeiro solicito à pessoa usuária que digite seu nome:
nome = input('Favor, digite seu nome: ')

# Em seguida, converto o nome para letras maiúsculas e inverto a ordem
nome_reverso = nome.upper()[::-1]

# Por fim, imprimo o nome de trás para frente
print('Nome de trás para frente:', nome_reverso)