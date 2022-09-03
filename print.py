from utils import remove_acento

IGNORED_CHARS = (" ", "-")


def print_forca(palavra_secreta="", letras_testadas={}, vidas=6):
   #Printa os estados do boneco e completa a palavra
	#o índice indica o número de vidas restantes
	#letras_testadas vem do set letras_testadas
   estados = ["""   _______
   /	  I 
   I	  I
   I	(ಥ_ಥ)
   I	 \|/
   I	  |
   I	 / \	      	
   I
===================
""",
"""   _______
   /	  I 
   I	  I
   I	(ಠ_ಥ)
   I	 \|/
   I	  |
   I	 / 	      	
   I
===================
""",
"""   _______
   /	  I 
   I	  I
   I	(ಠ╭╮ಠ)
   I	 \|/
   I	  |
   I	        	
   I
===================""",
"""   _______
   /	  I 
   I	  I
   I	(ಠ⌣ಠ)
   I	 \|
   I	  |
   I	        	
   I
===================""",
"""   _______
   /	  I 
   I	  I
   I	(⚆_⚆)
   I	  |
   I	  |
   I	        	
   I
===================""",
"""   _______
   /	  I 
   I	  I
   I	(ʘ‿ʘ)
   I	 
   I	  
   I	        	
   I
===================""",
"""   _______
   /	  I 
   I	  I
   I	                      
   I	 
   I	  
   I	        	       
   I
==================="""]

   print(estados[vidas], "\n")

   letras_testadas = list(letras_testadas)
   letras_testadas.sort()
   
   char_visiveis = (*letras_testadas, *IGNORED_CHARS)
   print("".join(ch if remove_acento(ch) in char_visiveis else "_" for ch in palavra_secreta), end="  ")

   if letras_testadas:
      print("(", " ".join(ch.upper() for ch in letras_testadas), ")", end="")
   
   print("\n")


