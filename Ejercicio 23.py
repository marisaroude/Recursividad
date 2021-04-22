def laberinto (matriz,x,y,caminos = []):
    if ( x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz [x][y] == 2):
            caminos.append ([x, y]) #Se le agrega un elemento con los valores de las posiciones x e y a la lista de caminos
            print ('Saliste del laberinto')
            print (caminos) 
            caminos.pop() #Elimina y retorna el ultimo elemento de la lista
        else:
            if (matriz [x][y] == 1) :
                matriz[x][y] = 3 #si la matriz es 1 quiere decir que no es pared entonces se la va marcando con un 3 para no volver a pasar por esa posicion y evitar un bucle en el laberinto
                caminos.append([x, y]) 
                laberinto(matriz, x, y+1, caminos) #mover este
                laberinto(matriz, x, y-1, caminos) #mover oeste
                laberinto(matriz, x-1, y, caminos) #mover norte
                laberinto(matriz, x+1, y, caminos) #mover sur
                caminos.pop()
                matriz[x][y] = 1
                



lab = [[1, 1, 1, 0, 1],
       [1, 0, 1, 1, 1],
       [1, 1, 0, 0, 1],
       [0, 1, 1, 0, 1],
       [0, 0, 1, 1, 2]]


laberinto(lab,0,0)