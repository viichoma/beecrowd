n=int(input())
for i in range(n):
    expressao = input()
    if expressao == "P=NP":
        print("skipped")
    else:
        resultado = eval(expressao)
        print(resultado)
    