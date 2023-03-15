# https://www.beecrowd.com.br/judge/pt/problems/view/1160 

n=int(input())

for i in range(n):
    pa,pb,g1,g2=map(float,input().split())
    pa = int(pa)
    pb = int(pb)
    anos=0
    while (pa <= pb):
        crescimento=int(pa*(g1/100))
        crescimento2=int(pb*(g2/100))
        anos+=1
        pa += crescimento
        pb += crescimento2
        if anos > 100:
            break

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")

