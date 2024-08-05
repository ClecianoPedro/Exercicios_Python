print("Contagem de Vogais\n")
palavra = input("Digite uma palavra: ")
contagem = 0
while palavra == "":
    print("Você precisa digitar algo!")
    palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in "aeiou":
        contagem += 1

print(f"Contém {contagem} vogais")