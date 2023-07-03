# Algoritmo que lê o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o salário do funcionário? '))

print('Houve uma mudança e o funcionário recebeu um aumento de 15% ! Agora, o salário dele é de {} Reais'.format(salario +(salario * 0.15)))