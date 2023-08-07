#9) Fazer um algoritmo que pergunte 1 número e apresente:
#a) O próprio número
#b) O quadrado deste número
#c) A raiz quadrada deste número

import math

num1 = int(input("Informe um número?" ))
quad = int(math.pow(num1,2))

rq = float(math.sqrt(num1))

print(f"O valor do proprio numero: {num1}\nO quadrado deste numero: {quad}\nSua raiz quadrada: {rq}")