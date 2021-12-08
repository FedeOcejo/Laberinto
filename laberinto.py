laberinto = [
[' ', 'X', 'X', 'X', 'X'], 
[' ', 'X', ' ', ' ', ' '], 
[' ', 'X', ' ', 'X', ' '],
[' ', ' ', ' ', 'X', ' '], 
['X', 'X', 'X', 'X', 'S'] ]

x=0
y=0

print (laberinto[y])[x]
listarespuestas= [" "," "," "," "," "," "," "," "," "," "," "," "," "]
i=0

while (laberinto[y])[x]== 'camino':
    direccion  = input("selecione a donde quiera moverse")
    if direccion == "Right" or "Down" or "Left" or "Up":
        print ("seleccionaste {}".format(direccion))
        listarespuestas[i] = direccion
        i= i + 1

    if direccion == "Right":
        x = x + 1
        y = y 
    elif direccion == "Down":
        x = x
        y = y -1
    elif direccion == "Left":
        x = x -1
        y = y
    elif direccion == "Up":
        x = x
        y = y + 1
    else:
        print('\n')

    print ("Te encuentras en la casilla ({},{})" .format(x,y))
    if (laberinto [y])[x]== 'camino':
        print(" la casilla que usted eligio no es un muro avance")
    elif(laberinto [y])[x]== 'S':
        print("Llegaste al final Felicidades")
        break

else:
    print("La casilla es un muro \nReinicia el juego para volver a empezar")

print ("tus movimientos han sido")
print(listarespuestas)