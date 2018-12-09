ruta = []
def busqueda(laberinto, inicio, fin, i = 0):
	global ruta
	f, c = inicio
	ff, cf = fin
	laberinto[ff][cf] = 'T'
	if(laberinto[f][c] == 'T'):
		print("Se Encuentra:", (f, c))
		return True
	elif(laberinto[f][c] == '*'):
		print("Obstaculo: ", (f, c))
		return False
	elif(laberinto[f][c] == '+'):
		print("Posicion visitada: ", (f, c))
		return False
	
	print("Visitando ", (f, c))
	ruta.append((f, c))
	
	laberinto[f][c] = '+'
	
	if(f < len(laberinto) - 1 and busqueda(laberinto, (f + 1, c), fin, i + 1)):
		return True
	if(c < len(laberinto) -1 and busqueda(laberinto, (f, c + 1), fin, i + 1)):
		return True
	if(f > 0 and busqueda(laberinto, (f - 1, c), fin, i + 1)):
		return True
	if(c > 0 and busqueda(laberinto, (f, c - 1), fin, i + 1)):
		return True
	return False
	
def devolverRuta():
	return ruta
