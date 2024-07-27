''' 4 - Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21

PS* Resolvi utilizar os dados atualizados de cada moeda'''

# Primeiro irei criar a função que calcula quanto pode ser comprado de cada moeda estrangeira
def calcular_moedas(dinheiro):
    taxas = {
        "Dólar Americano": 5.66,
        "Peso Argentino": 0.06,
        "Dólar Australiano": 3.69,
        "Dólar Canadense": 4.09,
        "Franco Suíço": 6.45,
        "Euro": 6.14,
        "Libra Esterlina": 7.29
    }
    
    # Agora irei calcular e imprimir a quantidade de cada moeda que pode ser comprada
    for moeda, taxa in taxas.items():
        quantidade = dinheiro / taxa
        print(f"Com R${dinheiro:.2f}, você pode comprar {quantidade:.2f} {moeda}(s).")

dinheiro = float(input("Digite quanto dinheiro você possui na carteira: R$"))

# Aqui irei chamar a função
calcular_moedas(dinheiro)