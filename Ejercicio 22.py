
def usar_la_fuerza (vector):  
    if (len(vector) == 0):
        return 0
    else:
        if (vector[0] == 'sable de luz'):
          return 1 
        else:
             global contador
             contador +=1
        return usar_la_fuerza(vector[1:])             


mochila = ['a','b','c','d','g','sable de luz','e','f',]
contador = 0

if ((usar_la_fuerza(mochila)) == 1):
    
    print ('La mochila contiene un sable de luz. Se necesitaron sacar ',contador, ' objetos para encontrarlo')
else:
    print ('La mochila no contiene un sable de luz')


