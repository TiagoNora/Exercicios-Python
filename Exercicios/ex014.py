#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
t = float(input('Introduza a temperatura em ºC: '))
f = 1.8 * t + 32
print(f'{t}ºC é igual a {f}ºF')