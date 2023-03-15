# https://www.beecrowd.com.br/judge/pt/problems/view/1180

n = int(input())
vetor = list(map(int, input().split()))
menor = min(vetor)
index = vetor.index(menor)
print (f"Menor valor: {menor}")
print (f"Posicao: {index}")