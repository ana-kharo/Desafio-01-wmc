''' 5 - Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''


# Primeiro eu solicito o salário bruto à pessoa usuária:
salario_bruto = float(input('Favor, digite o valor do seu salário bruto: '))

# Aqui declaro o valor do imposto inicializando com valor 0.0
imposto = 0.0

# Agora, calculo o imposto de renda de acordo com as faixas:
if salario_bruto <= 1903.98:
    imposto = 0.0
elif salario_bruto <= 2826.65:
    imposto = salario_bruto * 0.075
elif salario_bruto <= 3751.05:
    imposto = salario_bruto * 0.15
elif salario_bruto <= 4664.68:
    imposto = salario_bruto * 0.225
else:
    imposto = salario_bruto * 0.275

# Depois calculo o salário líquido
salario_liquido = salario_bruto - imposto

# Ao final, imprimo o saláraio liquído e o imposto descontado:
print(f' O salário bruto é de R${salario_bruto}.')
print(f' O desconto de imposto de renda será de R${imposto}.')
print(f' Deixando como salário líquido, R${salario_liquido}.')