# Algoritmo que lê o preço de um produto e mostre o preço com 5% de desconto

valor = float(input('Qual o valor do produto? '))

print('Houve uma mudança e o produto está com 5% de desconto. Logo, o novo preço dele é de {:.2f} Reais'.format(valor - (valor * 0.05)))