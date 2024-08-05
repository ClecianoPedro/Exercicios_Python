import random, string

def gerar_senha(tamanho):
    if tamanho < 4:
        raise ValueError ("O tamanho da senha deve ser 4 ou maior! ")
    
    minusculas = random.choice(string.ascii_lowercase)
    maiusculas = random.choice(string.ascii_uppercase)
    numeros = random.choice(string.digits)
    simbolos = random.choice(string.punctuation)

    restantes = tamanho - 4
    letras_numeros = string.ascii_letters + string.digits
    outras_partes = ''.join(random.choice(letras_numeros) for _ in range(restantes))

    senha = minusculas + maiusculas + numeros + simbolos + outras_partes
    senha = ''.join(random.sample(senha, len(senha)))

    return senha

print("Gerador de Senha\n")

try:
    tamanho_senha = input("Digite o tamanho da senha: ")

    while not tamanho_senha.isnumeric():
        print("O tamanho deve ser um número (positivo)!")
        tamanho_senha = input("Digite o tamanho da senha: ")

    tamanho_senha = int(tamanho_senha)
    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Senha gerada: {senha_gerada}")
    
except ValueError:
    print("Erro: O tamanho da senha deve ser pelo menos 4!")
