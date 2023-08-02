#3) Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais. Considere U$1,00 =
#R$3,80.

#Input

conv = int(input("Informe um valor em Dólar:"))

#Cálculos
real = 3.80
dol = 1.00

#Prints

print("O valor em Real é: R$%.2f" %(dol * real))