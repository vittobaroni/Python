# Programa que lê quanto uma pessoa tem na carteira e mostra quantos dólares ela pode comprar (Valor do dólar = R$ 4,80 , no dia 3 de julho de 2023, às 16:00 do horario de Brasília)

dinheiro = float (input('Quanto de dinheiro você possui na carteira ? '))

print('De acordo com esta quantidade, você consegue ter {:.2f} em Dólares'.format(dinheiro / 4.80))