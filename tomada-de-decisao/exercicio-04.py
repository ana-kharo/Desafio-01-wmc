''' 4 -  Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado. '''

# Primeiro eu inicio o loop ou a condição 'enquanto'setando como true:
while True:
    # Depois eu solicito a nota à pessoa usuária:
    nota = float(input('Favor, digite uma nota entre (0 e 10): '))
    
    # Daí verifico se a nota está dentro do intervalo proposto:
    if 0 <= nota <= 10:
        if nota >= 7:
            print('Você foi aprovada(o) :D ')
        else:
            print('Você foi reprovada(o) :( ')
        break
else:
    print('Nota inválida! Favor, tentar novamente!') 