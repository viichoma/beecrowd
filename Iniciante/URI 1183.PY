# https://www.beecrowd.com.br/judge/pt/problems/view/1183

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
# Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da matriz, 
# conforme ilustrado abaixo (área verde).

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada 
# com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.


op = input()
matriz=[]
for i in range(12):
    matriz.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

if op == 'S':
    soma = 0
    coluna = 1
    for i in range(12):
        for j in range(coluna, 12):
            soma += matriz[i][j]
        coluna += 1
    print('{:.1f}'.format(soma))

if op == 'M':
    soma = 0
    coluna = 1
    contador = 0
    for i in range(12):
        for j in range(coluna, 12):
            soma += matriz[i][j]
            contador += 1
        coluna += 1
    print('{:.1f}'.format(soma/contador))
