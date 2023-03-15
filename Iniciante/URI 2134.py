# https://www.beecrowd.com.br/judge/pt/problems/view/2143

while True:
    n = int(input())
    if not n:
        break
    pessoas = 0
    while n:
        n -= 1
        pessoas = int(input())
        if pessoas % 2 == 0:
            pessoas = (pessoas * 2) - 2
        else:
            pessoas = (pessoas * 2) - 1
        print(pessoas)  