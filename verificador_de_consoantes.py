def solicitar_palavra():
    palavra = input("Digite uma palavra: ").replace(" ", "")
    while palavra == "" or palavra.isnumeric():
        if palavra.isnumeric():
            print(f"O valor não é válido!")
            palavra = input("Digite uma palavra: ").replace(" ", "")
        else:
            print("Você precisa digitar uma letra para que eu possa contar!")
            palavra = input("Digite uma palavra: ").replace(" ", "")
    return palavra

print(f"{"-"*7} Verificador de Consoantes {"-"*7}")
palavra = solicitar_palavra()
contador = 0

for letra in palavra:
    if letra not in "aeiou":
        contador +=  1

print(f"A palavra contém {contador} consoante(s)")