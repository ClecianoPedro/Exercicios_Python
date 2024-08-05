import random

print("Jogo de Advinhacao de numeros\n")
numero_aleatorio = random.randint(0,100)

try:
    chute = int(input("Digite um numero: "))
    
    while chute != numero_aleatorio:
        if chute < numero_aleatorio:
            chute = int(input("Digite um numero maior: "))
 
        else:
            chute = int(input("Digite um numero menor: "))
     
    print(f"Parabéns, você acertou!! O número era {numero_aleatorio}")

except ValueError:
    print("Erro: O valor deve ser um número (positivo)!")