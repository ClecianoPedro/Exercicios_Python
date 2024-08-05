def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def gerar_primos(limite):
    primos = []
    if limite <= 2:
        return "Não é primo!"
    
    else:
        for num in range(2, limite + 1):
            if e_primo(num):
                primos.append(num)
        return primos


print("Gerador de numeros primos\n")
numero = input("Digite um numero limite para gerar a sequência de numeros primos: ")

while not numero.isnumeric():
    print("O valor deve ser um número (positivo)!")
    numero = input("Digite um numero limite para gerar a sequência de numeros primos: ")

numero = int(numero)
primos_gerados = gerar_primos(numero)
print(primos_gerados)
