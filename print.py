def print_forca(vidas=6, letras_digitadas=None, palavra_secreta=None, letra_escolhida=None):
	#letra_escolhida vem da função pedir_letra(), uso esse argumento pra ir completando a palavra.
	#o índice indica o número de vidas restantes
	#letras_digitadas vem do set letras_testadas
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
	""""""
	if vidas == 6:
		print(estados[6])
	elif vidas == 5:
		print(estados[5])
	elif vidas == 4:
		print(estados[4])
	elif vidas == 3:
		print(estados[3])
	elif vidas == 2:
		print(estados[2])
	elif vidas == 1:
		print(estados[1])
	else:
		print(estados[0])

	print('As letras testadas foram:', end= ' ')
	for letra in letras_digitadas:
		print(letra, end= ' ')
	palavra_secreta_escondida = len(palavra_secreta) * '*'#vou completar a palavra usando o argumento de letra escolhida


