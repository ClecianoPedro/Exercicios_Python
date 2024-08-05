print("---- Soma de digitos ----\n")
numero = input("Digite um valor qualquer (sem espaços): ") # Deve ser digitado apenas numeros em uma única linha
soma = 0
for i in numero:
    soma = soma + int(i)
print(f"A soma dos digitos foi: {soma}")