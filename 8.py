#8) Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
#programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
#valor do consumo médio do automóvel, em quilômetros por litro.

print("Insira abaixo as informações:")
dst = float(input("Qual a distância?"))
lt = float(input("Qual o valor de consumo médio do automóvel?"))

distancia = 1000 * dst
litro = 1000 * lt

print("Distância em Km:",distancia)
print("Consumo médio do automóvel em litro:",litro)

