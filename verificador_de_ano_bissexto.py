print("Descubra se o ano digitado é bissexto\n")
try:
    ano = input("Digite um ano qualquer: ").strip()

    if int(ano) % 400 == 0 or ano[-2] + ano[-1] not in "00" and int(ano) % 4 == 0:
        print("O ano digitado é Bissexto")
    else:
        print("O ano digitado não é Bissexto")

except ValueError:
    print("Erro: Ano inválido!")