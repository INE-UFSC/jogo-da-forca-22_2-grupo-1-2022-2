def escolher_palavra() -> str:
    """Escolhe uma palavra aleatória de uma lista predefinida."""
    ...


def verificar_match(palavra: str, letras_testadas: set[str]) -> bool:
    """
    Verifica se o usuário acertou a palavra escolhida com base nas letras
    já testadas.
    """
    ...


def print_forca(palavra: str, letras_testadas: set[str], vidas: int):
    """Imprime no terminal a interface do jogo com a devida formatação."""
    ...


def jogo_da_forca():
    """Inicia o jogo da forca."""
    ...


if __name__ == "__main__":
    jogo_da_forca()
