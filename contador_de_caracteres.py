print(f"Contador de Caracteres\n")
contador = 0
palavra = input("Digite uma palavra: ")

for i in range(len(palavra)):
    contador += 1
print(f"A palavra contém {contador} caractere(s)")