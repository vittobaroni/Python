# Algoritmo que lê um número do usuário, mostra o sucessor e o antecessor

numero = int(input('Digite um número: '))

print('Você digitou o número {} \nSeu antecessor é {}\nE seu sucessor é {}'.format(numero, numero - 1, numero + 1 ))