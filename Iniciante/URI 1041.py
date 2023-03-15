# https://www.beecrowd.com.br/judge/pt/problems/view/1041

X, Y = map(float, input().split())
if (X == 0.0 and Y == 0.0):
    print("Origem")
elif (X == 0.0 and Y != 0.0):
    print("Eixo Y")
elif (Y == 0.0 and X != 0.0):
    print("Eixo X")
elif (X > 0.0):
    if (Y > 0.0):
        print("Q1")
    else: print("Q4")
elif (Y > 0.0):
    print("Q2")
else: print("Q3")
