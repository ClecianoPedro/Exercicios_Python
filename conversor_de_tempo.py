def solicitar_tempo():
    tempo = input("Digite o tempo em segundos: ")
    while not tempo.isnumeric():
        print("Você deve digitar apenas valores numéricos!")
        tempo = input("Digite o tempo em segundos: ")

    return float(tempo)

print("Conversor de segundos em: Horas, Minutos e Segundos.\n")
try:
    tempo = solicitar_tempo()
    minutos = tempo / 60
    horas = tempo / 3600
    segundos = tempo * 3600
    print(f"Seu tempo de {tempo:.0f} segundos contém: {horas:.3f} hora(s), {minutos:.3f} minuto(s) e {segundos:.1f} segundo(s).")

except ValueError:
    print("Erro: O valor deve ser apenas numérico!")