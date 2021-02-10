# EXERCÍCIO 066 - VÁRIOS NÚMEROS COM FLAG

# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

# SOLUÇÃO

num = soma = count = 0
while True:
    num = int(input('Digite um número [digite 999 para parar]: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Você digitou {count} números e a soma final foi {soma}')
