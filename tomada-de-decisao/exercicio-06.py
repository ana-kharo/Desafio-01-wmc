''' 6 - Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro. '''

# Primeiro irei solicitar login e a senha à pessoa usuária:
login = input('Favor, digite seu login: ')
senha = input('Agora, digite sua senha: ')

# Depois,verifico se o login e a senha estão corretos
if login == 'admin' and senha == 'admin123':
    print('Ok, acesso permitido.')
else:
    print('Erro: login ou senha incorretos.')