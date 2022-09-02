from print import print_forca
import word 
import unicodedata

TOTAL_VIDAS = 6


def escolher_palavra() -> str:
    """
    Escolhe uma palavra aleatória de uma lista predefinida.

    :param word_object.word: Selected word to play the game
    :type word_object.word: String
    """
    print("Digite a palavra para jogar a forca ou aperte enter para escolher uma palavra aleatória:")
    word_object = word.Word()
    return word_object.word




def remove_acento(palavra: str) -> str:
    nkfd_form = unicodedata.normalize('NFKD', palavra)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    
    return only_ascii.decode("utf-8")



def verificar_match(palavra: str, letras_testadas: "set[str]") -> bool:
    """
    Verifica se o usuário acertou a palavra escolhida com base nas letras
    já testadas. Assume que todas as letras em 'letras_testadas' são minúsculas
    """
    
    palavra = remove_acento(palavra)
    
    if '-' in palavra:
        aux = palavra.split('-')
        palavra = "".join(aux)
    
    elif " " in palavra:
        aux = palavra.split()
        palavra = "".join(aux)
    
    for letra in palavra.lower():    
        if letra not in letras_testadas:
            return False
    
    return True


def pedir_letra() -> str:
    """
    Pede ao usuário para digitar uma letra no terminal. Certifica que
    a valor inserido é válido.
    
    Retorna a letra em lowercase e sem acento.
    """
    inputletra = "0" 
    while inputletra.isalpha() == False:
        while True:
            inputletra = input(" Digite a letra escolhida:  ").lower()
            if len(inputletra)>1:
                print("Por favor digite apenas uma letra.")
            else:
                break
        
        if inputletra.isalpha():
            return(remove_acento(inputletra))
            inputletra.isalpha() == True
            
        else:
            print("Por favor digite uma letra válida.")


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
