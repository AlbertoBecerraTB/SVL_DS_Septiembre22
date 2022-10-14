


import math
import unidecode

class Estacion:
    
    def __init__(self, name, identificador, num_bicis, address, longitude, latitude):
        self.name = name
        self.identificador = identificador
        self.num_bicis = num_bicis
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        
        
        
    def distancia(self, longitude, latitude):

        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d
        

        
class ComunidadMadrid:

    
    def __init__(self, estaciones):
        self.estaciones = estaciones
        

    def get_ids(self):
        todas = []
        
        for i in self.estaciones:
            todas.append(int(i.identificador))
        
        return todas
    
    def busca_estacion(self, estacion, tipo_busqueda):



        for i in self.estaciones:
            
            if tipo_busqueda == "name":
                est1 = unidecode.unidecode(estacion.lower())
                est2 = unidecode.unidecode(i.name.lower())

                if est1 in est2:
                    return i
                    
            elif tipo_busqueda == "id":
                if int(estacion) == int(i.identificador):
                    return i
                
        return None

