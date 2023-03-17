# https://www.beecrowd.com.br/judge/pt/problems/view/2140
# Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras, 
# ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, 
# escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando duas notas.

# As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

# Entrada
# A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago pelo cliente (N < M ≤ 104). A entrada termina com N = M = 0.

# Saída
# Seu programa deverá imprimir "possible" se for possível devolver o troco exato ou "impossible" se não for possível.

while True:
    n, m = map(int, (input().split()))
    if n  == 0 or m == 0:
        break
    troco = m - n
    notas = 0
    if troco >= 100:
        notas+=1
        troco -=100
        
    if troco >= 50:
        notas+=1
        troco-=50

    if troco >= 20:
        notas+=1
        troco-=20

    if troco >= 10:
        notas+=1
        troco-=10

    if troco >= 5:
        notas+=1
        troco-=5

    if troco >= 2:
        notas+=1
        troco-=2

    if notas != 2:
        print("impossible")
    else:
        print("possible")
