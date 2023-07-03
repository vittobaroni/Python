# Programa que lê duas notas de um aluno, calcula e mostra a média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('-'*40)
print('A média do aluno foi de {:.1f}'.format((n1+n2)/2))