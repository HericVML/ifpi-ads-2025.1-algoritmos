# Entrada
saque = int(input('Digite a quantia que deseja sacar: '))

# Processamento
cinquenta = saque // 50
dez = (saque % 50) // 10
cinco = ((saque % 50) % 10) // 5
um = ((saque % 50) % 10) % 5

# Saída
resultado = f'Você receberá {cinquenta} nota(s) de R$50.00, {dez} nota(s) de R$10.00, {cinco} nota(s) de R$5.00 e {um} nota(s) de R$1,00'
print(resultado)