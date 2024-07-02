import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'dados', 'inteligencia']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    palavra_secreta = ['_'] * len(palavra)
    letras_erradas = []
    tentativas = 6  # Número máximo de tentativas antes de ser enforcado

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta. Você tem", tentativas, "tentativas.")

    while True:
        print("\nPalavra: " + " ".join(palavra_secreta))
        print("Letras erradas: " + " ".join(letras_erradas))

        if '_' not in palavra_secreta:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break
        elif tentativas == 0:
            print("\nVocê foi enforcado! A palavra era:", palavra)
            break

        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        elif letra in letras_erradas or letra in palavra_secreta:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        jogar_forca()
    else:
        print("\nObrigado por jogar!")

if __name__ == "__main__":
    jogar_forca()