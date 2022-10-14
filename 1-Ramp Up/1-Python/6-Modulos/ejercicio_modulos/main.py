
import os
os.getcwd()


# Leemos los datos
import pandas as pd
from clases import Estacion, ComunidadMadrid
from funciones import dist_estaciones

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")

tot_est = []

for index, row in df.iterrows():
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)


comunidad = ComunidadMadrid(tot_est)


while True:
    
    resp_usu1 = input("Escoge una opcion: \n1. Busca estacion\
                      \n2. Calcula distancia \n3. Salir del programa\n")
    
    try:
        resp_usu1 = int(resp_usu1)
    except:
        print("Respuesta no valida. Por favor introduce 1, 2 o 3")
        continue
        
    # Elige buscar una estacion por nombre
    if resp_usu1 == 1:
        resp_usu2 = input("Muy bien, introduce el nombre de la estacion")
        busqueda = comunidad.busca_estacion(resp_usu2, "name")
        if busqueda == None:
            print("Esta estacion no está en la base de datos")
        else:
            print("¡Estacion encontrada! La estación es",busqueda.name,"\n\n\n¿Qué más deseas hacer?")
            
    elif resp_usu1 == 2:
        resp_usu3_1 = int(input("Introduce el identificador de la primera estacion "))
        resp_usu3_2 = int(input("Introduce el identificador de la segunda estacion "))
        
        distancia = dist_estaciones(resp_usu3_1, resp_usu3_2, comunidad)
        
        if type(distancia) == str:
            print(distancia)
        else:
            print("Las estacines introducidas están a una distancia de", round(distancia, 2), "km")
        
    elif resp_usu1 == 3:
        print("¡Hasta la próxima!")
        break
    
    else:
        print("Respuesta no valida. Por favor introduce 1, 2 o 3")
    
        
        
        


