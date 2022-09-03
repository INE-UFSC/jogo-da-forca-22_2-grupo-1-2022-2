import os
import unicodedata

def limpar_terminal():
   os.system('cls' if os.name == 'nt' else 'clear')

def remove_acento(palavra: str) -> str:
    nkfd_form = unicodedata.normalize('NFKD', palavra)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    
    return only_ascii.decode("utf-8")