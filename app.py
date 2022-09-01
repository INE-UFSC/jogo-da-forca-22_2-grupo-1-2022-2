import word 

TOTAL_VIDAS = 4


def escolher_palavra() -> str:
    """
    Escolhe uma palavra aleatória de uma lista predefinida.

    :param word_object.word: Selected word to play the game
    :type word_object.word: String
    """
    print("Digite a palavra para jogar a forca ou aperte enter para escolher uma palavra aleatória:")
    word_object = word.Word()
    return word_object.word


def verificar_match(palavra: str, letras_testadas: set[str]) -> bool:
    """
    Verifica se o usuário acertou a palavra escolhida com base nas letras
    já testadas. Assume que todas as letras em 'letras_testadas' são minúsculas
    """
    letras_acentos = { 'á':'a', 'à':'a', 'ã':'a', 'â':'a', 'é':'e', 'ê':'e', 'í':'i', 
               'ó':'o', 'õ':'o', 'ô':'o', 'ú':'u'}
    
    if '-' in palavra:
        aux = palavra.split('-')
        palavra = "".join(aux)
    
    elif " " in palavra:
        aux = palavra.split()
        palavra = "".join(aux)
    
    for letra in palavra.lower():
        if letra in letras_acentos.keys(): #se a letra for acentuada, ela recebe
            letra = letras_acentos[letra]  #um valor equivalente sem acento
        
        if letra not in letras_testadas:
            return False
    
    return True


def print_forca(palavra: str, letras_testadas: set[str], vidas: int):
    """Imprime no terminal a interface do jogo com a devida formatação."""
    ...


def pedir_letra() -> str:
    """
    Pede ao usuário para digitar uma letra no terminal. Certifica que
    a valor inserido é válido.
    
    Retorna a letra em lowercase e sem acento.
    """
    ...


def jogo_da_forca():
    """Inicia o jogo da forca."""

    palavra = escolher_palavra()
    letras_testadas = set()
    vidas = TOTAL_VIDAS

    while True:
        print_forca(palavra, letras_testadas, vidas)

        if verificar_match(palavra, letras_testadas):
            print("Você acertou!")
            break

        if vidas <= 0:
            print(
                f"Você errou, a palavra era '{palavra}'. Mais sorte na próxima vez :/"
            )
            break

        letra = pedir_letra()

        if not letra in letras_testadas:
            letras_testadas.add(letra)

            if not letra in palavra:
                vidas -= 1

jogo_da_forca()