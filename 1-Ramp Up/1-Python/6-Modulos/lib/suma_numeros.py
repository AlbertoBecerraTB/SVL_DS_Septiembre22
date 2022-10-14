#############################################
############ SUMA NÚMEROS ###########

# Autor: fjdsfl
# Fecha: ddfjknrsjfs
# Contacto: khksahgf

def suma_impares(ls):
    '''
    Función que, dada una lista de números enteros,
    nos da la suma de los impares
    '''
    suma = 0
    for num in ls:
        if num%2!=0:
            suma += num
    return suma

def suma_pares(ls):
    '''
    Función que, dada una lista de números enteros,
    nos da la suma de los pares
    '''
    suma = 0
    for num in ls:
        if num%2==0:
            suma += num
    return suma