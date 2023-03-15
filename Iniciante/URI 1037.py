# https://www.beecrowd.com.br/judge/pt/problems/view/1037

A = float(input())
if(A<0 or A>100.0):
    print("Fora de intervalo")
elif (A<=25.0):
    print("Intervalo [0,25]")
elif(A<=50.0):
    print("Intervalo (25,50]")
elif(A<=75.0):
    print("Intervalo (50,75]")
elif(A<=100.0):
    print("Intervalo (75,100]")
