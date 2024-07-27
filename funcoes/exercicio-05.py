''' 5 - Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''


# Primeiro, irei criar a função que conta as vogais:
def contar_vogais (frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    # Agora irei percorrer cada letra da frase:
    for letra in frase:
        if letra in vogais:
            contador += 1

    # Aqui retornarei o total de vogais
    return contador

# Agora solicito à pessoa usuária, a frase:
frase_pessoa_usuaria = input('Favor, digite uma frase: ')

# Chamo a função para contar as vogais:
total_vogais = contar_vogais(frase_pessoa_usuaria)

# Exibo o total das vogais:
print(f'A frase que você digitou contém {total_vogais} vogal(is)')