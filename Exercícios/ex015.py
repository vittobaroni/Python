# Programa que pergunta a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado, mostrando o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

dias = int(input('Quantos dias o carro foi alugado? '))
rodado = float(input('Foram quantos km rodados ?'))
total = (dias * 60) + (rodado * 0.15)

print('O total a pagar é de R${}'.format(total))