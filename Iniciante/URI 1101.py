# https://www.beecrowd.com.br/judge/pt/problems/view/1101

maior=0
menor= 0
while True:
    sum=0
    M, N=map(int, input().split())

    if (M <= 0 or N <= 0):
        break
    
    maior= M if M > N else N
    menor= N if N < M else M

    for x in range(menor, maior+1):
        print(x, end=" ")
        sum += x
    print (f"Sum={sum}")