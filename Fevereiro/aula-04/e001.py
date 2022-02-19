#Desenvolva o código em python, em que você receba 3 variáveis a,b e c, e as coloque em ordem crescente. 
# Para isso você deve usar apenas os comandos if, else e elif 
# e não fazer mais que uma comparação entre duas variáveis por comanda (if, else e elif) utilizado,
#  assim você precisará utilizar comandos aninhados.

a = int(input('Diga um número bem bonito:'))
b = int(input('Diga outro número bem interessante:'))
c = int(input('Para fechar com chave de ouro, escolha aquele número bem chamativo que aguça sua cabeça:'))
lista_num = []

if a > b:
    if a > c:
        lista_num = [b,c,a]
    else:
        lista_num = [b,a,c]

elif b > a:
    if b > c:
        lista_num = [a,c,b]
    else:
        lista_num = [a,b,c]

else:
    lista_num = [c,a,b]


print(lista_num)