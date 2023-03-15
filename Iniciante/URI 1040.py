# https://www.beecrowd.com.br/judge/pt/problems/view/1040

a, b, c, d = map(float, input().split())
m = (a * 2 + b * 3 + c * 4 + d) / 10
print(f"Media: {m:.1f}")
if (m >= 7.0):
    print("Aluno aprovado.")
elif (m >= 5.0):
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    if (exame + m / 2.0 > 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {((exame+m)/2.0):.1f}")
else:
    print("Aluno reprovado.")
