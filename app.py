import word 

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


def jogo_da_forca():
    """Inicia o jogo da forca."""
    ...

jogo_da_forca()
