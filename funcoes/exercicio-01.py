# 1 - Faça um programa, com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos.

# Primeiro eu irei cirar a função de cálculo:
def soma_tres_numeros(a, b, c):
    return a + b + c

# Agora irei solicitar os três números à pessoa usuária
num1 = float(input("Favor, digite o primeiro número: "))
num2 = float(input("Agora digite o segundo número: "))
num3 = float(input("E por fim, o terceiro número: "))

# Agora irei calcular a soma dos três números usando a função:
resultado = soma_tres_numeros(num1, num2, num3)

# POr fim, imprimir o resultado da soma:
print("A soma dos três números é:", resultado)
