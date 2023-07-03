# Algoritmo que lê um número e mostra seu dobro, seu triplo e sua raiz quadrada

numero = int(input('Digite um número inteiro: '))

print('Você digitou o número {}\nSeu dobro é {}\nSeu triplo é {}\nE sua raíz quadrada é {:.0f}'.format(numero,numero*2, numero*3, numero**(1/2)))