from string import digits

print("Digite numeros e veja-os ordenados")

lista = [num for num in input("Digite os numeros que deseja ordernar (separados por espaço): ").split()]
ordenados = []

for i in range(len(lista)):
    if lista[i] not in digits:
        print(f"O valor {lista[i]} não foi aceito")
    else:    
        num = int(lista[i])
        ordenados.append(num)

ordenados.sort()
print(f"Números ordenados: {ordenados}")