# https://www.beecrowd.com.br/judge/pt/problems/view/1036

import math
A, B ,C = map(float, input().split())
delta = B*B - 4.0*A*C
if (delta < 0 or A == 0):
    print("Impossivel calcular")
else:
    print(f"R1 = {(-B+math.sqrt(delta))/(2.0*A):.5f}")
    print(f"R2 = {(-B-math.sqrt(delta))/(2.0*A):.5f}")
