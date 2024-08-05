print("Contagem regressiva\n")
try:
    maior_numero = input("Digite um numero para que seja feita a contagem regressiva: ")

    while not maior_numero.isnumeric():
        print("O valor de ser um número (positivo)!")
        maior_numero = input("Digite um numero para que seja feita a contagem regressiva: ")

    else:
        maior_numero = int(maior_numero)
        for i in range(maior_numero, -1, -1):
            print(i)
except ValueError:
    print("Erro: Você precisa digitar um número válido!")