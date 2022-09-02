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
   letras_testadas = list(letras_testadas)
   letras_testadas.sort()
   print("A palavra secreta é:", end= ' ')
   print("".join(ch if ch in letras_testadas else "*" for ch in palavra_secreta))
   print("As letras escolhidas até agora foram:", end= ' ')
   for letra in letras_testadas:
      print(letra.upper(), end= ' ')



