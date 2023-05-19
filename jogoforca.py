import random

def draw_hangman(tentativas):
    partes_corpo = [
        '''
           --------
           |      |
           |      
           |     
           |      
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |     
           |     
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
        ''',
        '''
           --------
           |      |
           |      0
           |     /|\\
           |      |
           |     / \\
        '''
    ]
    print(partes_corpo[6 - tentativas])

def print_confetes():
    confetes = ["\n^-^","\n🎉", "\n✨", "\n🎊", "\nfrutas🎇"]
    for _ in range(5):
        print(random.choice(confetes), end="")
    print()

def print_triste():
    triste = ["\n°_°", "\n:/", " \n°~°"]
    for _ in range(3):
        print(random.choice(triste), end="")
        print()

def play_game():
    temas = {
        'Animais': ['Gato', 'Cachorro', 'Elefante'],
        'Frutas': ['Maça', 'Banana', 'Laranja'],
        'Países': ['Brasil', 'Canadá', 'Índia']
    }

    tema = input("\nEscolha um tema (Animais, Frutas, Países):\n").capitalize()
    while tema not in temas:
        tema = input("\nTema inválido. Por favor, escolha um tema válido: \n").capitalize()

    palavras = temas[tema]
    palavra = random.choice(palavras).lower()

    letras_adivinhadas = []
    letras_erradas = []
    tentativas = 6

    while True:
        letra_adivinhada = ''.join([letra if letra in letras_adivinhadas else ' _' for letra in palavra])
        print("\nPalavra:", letra_adivinhada)
        print("Letras erradas:", letras_erradas)

        if letra_adivinhada == palavra:
            print("\nParabéns! Você acertou a palavra!")
            print_confetes()
            break

        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra)
            print_triste()
            break

        letra = input("Digite uma letra: ").lower()
        if letra in letras_adivinhadas or letra in letras_erradas:
            print("Você já usou essa letra.")
            continue

        if letra in palavra:
            letras_adivinhadas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            draw_hangman(tentativas)


play_game()
