# jogo de adivinhar o número

guess = 1

while True:
    num = input("Tente um número entre 0-100: ")
    try:
        num = int(num)
    except:
        print("Número inválido, por favor tente novamente.")
        continue

    if num < 45:
        print("Sua tentativa foi a baixo do número.")
    elif num > 45:
        print("Sua tentativa foi acima do número.")
    else:
        break

    guess += 1

print(f"Você acertou em {guess} tentativas.")