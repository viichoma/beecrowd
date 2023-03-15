# https://www.beecrowd.com.br/judge/pt/problems/view/1183

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