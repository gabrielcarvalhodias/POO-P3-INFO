salario = int(input('Qual o valor do seu salário?'))

if salario > 600 and salario <= 1200:
    valor1 = salario - salario * 0,20
    print('O valor final, após a retirado do dinheiro para INSS, é', valor1)
