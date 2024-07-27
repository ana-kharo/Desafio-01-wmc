''' 7 - Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura). '''

# Primeiro irei solicitar a pessoa usuária seu peso e sua altura: 
peso = float(input('Favor, digitar o seu peso em Kg: '))
altura = float(input('E agora a sua altura em metros: '))

# Aqui irei realizar o calculo do imc
imc = peso / (altura * altura)

# Por fim exibir o resultado
print(f'O resultado do seu imc é: {imc:.2f} ')