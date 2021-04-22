
def conversion_binaria (numero):
    if (numero == 0):
        return ''
    else:
        #if (numero // 2 != 0):
            return conversion_binaria(numero//2) + str(numero % 2)


#binario = str(decimal % 2) + binario
#decimal = decimal // 2
#return str(decimal) + binario

print (conversion_binaria(252))
