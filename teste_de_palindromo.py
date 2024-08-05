print("Teste de palíndromo")
palavra = input("Digite uma palavra: ")
palavra_invertida = ''.join(reversed(palavra))
if palavra == palavra_invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")