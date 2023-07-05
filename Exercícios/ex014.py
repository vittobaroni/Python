# Programa que lê uma temperatura em Celsius e a transforma em Fahrenheit 

temperatura = float(input('Informe a temperatura em Celsius(°C): '))
conversao = (9/5)*temperatura + 32

print('A temperatura de {}°C corresponde a {}°F'.format(temperatura, conversao))