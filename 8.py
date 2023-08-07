#8) Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
#programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
#valor do consumo médio do automóvel, em quilômetros por litro.

print("Insira abaixo as informações:")
dst = int(input("Qual a distância em km?"))
lt = int(input("Qual o valor de consumo médio do automóvel?"))

dist = dst
litro = lt

vt = dist // lt

print("Distância em Km:",dist)
print("Consumo médio do automóvel em litros:",litro)
print("Consumo médio do automóvel em quilometros por litro",vt)
print(f"Você gastar {vt} litros de combustível em sua viagem")

