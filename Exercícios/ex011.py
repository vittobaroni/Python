# Programa que lê a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Qual a largura da parede ? '))
altura = float(input('Qual a altura da parede ? '))
area = largura * altura

print(' De acordo com os dados de largura e altura informados, a área da parede é de {:.2f}m²\n Sabendo que cada litro de tinta cobre 2m², a quantidade necessária de tinta será de {:.2f} litros'.format(area, area / 2 ))