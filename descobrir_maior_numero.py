print("--------- Verificação de maior número ---------")
lista_numeros = []
maior_numero = 0

quantidade = input("Quantos números você deseja verificar: ")

while not quantidade.isnumeric():
    print("Você deve digitar apenas números (positivos)!")
    quantidade = input("Quantos números você deseja verificar: ")

quantidade = int(quantidade)
for i in range(quantidade):
    numero = input(f"Digite o {i+1}° número: ")

    while not numero.isnumeric():
        print("Você deve digitar apenas números (positivos)!")
        numero = input(f"Digite o {i+1}° número: ")
    lista_numeros.append(numero)

maior_numero = lista_numeros[0]

for i in range(1, len(lista_numeros)):
    if maior_numero < lista_numeros[i]:
        maior_numero = lista_numeros[i]

print(f"O maior número é {maior_numero}")