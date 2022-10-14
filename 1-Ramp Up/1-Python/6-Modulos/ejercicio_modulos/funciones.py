

def dist_estaciones(est1, est2, comunidad):
    
    estacion1 = comunidad.busca_estacion(est1, "id")
    estacion2 = comunidad.busca_estacion(est2, "id")
    
    if estacion1 != None and estacion2 != None:        
        return estacion1.distancia(estacion2.longitude, estacion2.latitude)
    
    else:
        return "Alguna de las estaciones no está en la base de datos"