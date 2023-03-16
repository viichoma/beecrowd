n = int(input())
for i in range(n):
    a, b= map(int, input().split())
    resultado = a ** b
    resultado = str(resultado)
    print(len(resultado))