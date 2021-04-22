valores = {'I' : 1, 'V' : 5, 'X' : 10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000}

def conversion_numeros (romano):
     if (len(romano) == 1):   #Si el tamaño del romano es 1 devuelve el valor de la posicion 0 del diccionario,
          return valores[romano[0]]
     else:
          if (valores[romano[0]] >= valores[romano[1]]): # si el valor de la posicion 0 es mayor o igual al valor de la posicion 1 
               return conversion_numeros(romano[1:]) + valores[romano[0]] #retorna la funcion que va recorriendo el nro romano mientras va particionandolo, a su vez va sumando los valores
          else:  
               if (valores[romano[0]] < valores[romano[1]]): 
                    return conversion_numeros(romano[1:]) - valores[romano[0]]
          


print (conversion_numeros('IV'))