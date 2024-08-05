print("Contador de palavras\n")
palavras = input("Digite uma ou mais palavras: ").split(" ")
contagem_palavras = 0

for palavra in palavras:
    if len(palavra) > 1:
        contagem_palavras += 1
    else:
        contagem_palavras = 0

if contagem_palavras == 0:
    print(f"Você digitou {contagem_palavras} palavras, visto que são consideradas palavras acima de 2 caracteres")
else:
    print(f"Você digitou {contagem_palavras} palavra(s)")
        