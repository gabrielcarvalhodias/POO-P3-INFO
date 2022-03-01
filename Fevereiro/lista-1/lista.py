#----QUESTÃO 1------

from unittest import result


salario = int(input('Diga o valor:'))

if salario > 600 and salario <= 1200:
    valor1 = salario - salario * 0.20
    print('O valor final, após as alterações, resulta no valor de: ', valor1)
elif salario >= 1200 and salario <= 2000:
    valor1 = salario - salario * 0.25
    print('O valor final, após as alterações, resulta no valor de: '+ valor1)
elif salario > 2000:
    valor1 = salario - salario * 0.30
    print('O valor final, após as alterações, resulta no valor de: '+ valor1)
else:
    print(salario)

print('\n')

#-----QUESTÃO 2------

saldo = int(input('Diga um valor inicial:'))
debito = int(input('Agora diga o valor que deseja contabilizar no desconto do débito: '))
credito = int(input('Faça a mesma coisa, só que para acrescentar como crédito:'))
resultado = saldo - debito + credito
pergunta = input('Atenção! O seu saldo está em %s, ainda deseja fazer alguma alteração? Se sim, responda com S/D para débito e S/C para crédito: ' %(resultado))

if pergunta == 'S/D' or 's/d':
    pergunta2 = int(input('Quanto você deseja utilizar em seu débito?'))
    print('Enfim, seu saldo final, após o desconto do débito, ficou em R$%s' %(resultado - pergunta2))
elif pergunta == 'S/C' or 's/c':
    pergunta2 = int(input('Quanto você deseja adicionar como crédito?'))
    print('Enfim, seu saldo final, após acrescentado o crédito, ficou em R$%s' %(resultado + pergunta2))
else:
    print('ERRO')

print('\n')


#----QUESTÃO 3----

vezes = 5
valores = []
while vezes >0:
    pergunta3 = int(input('Fale um número: '))
    valores.append(pergunta3)
    vezes -= 1

valores.sort()

print('Menor valor: %s' %(valores[0]))
print('Maior valor: %s' %(valores[4]))