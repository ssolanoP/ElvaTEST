from fastapi import FastAPI
import googlemaps


app = FastAPI()

@app.get("/")
def index():

    vecindario = geolocalizacion(1300)
    return {"status": "200", "Vecindario" : vecindario}

@app.get("/OtherNeighborhood")
def Other():

    vecindario,val = recursividad(1300,"Southeast Portland")
    return {"status": "200", "Vecindario":vecindario, "address":str(val)+" SE Stark Street, Portland, OR 97214"}

def geolocalizacion(numero):

    gmaps = googlemaps.Client(key='---------------------------------------')

    geocode_result = gmaps.geocode(str(numero)+' SE Stark Street, Portland, OR 97214')
    Latitud = geocode_result[0]['geometry']['location']['lat']
    Longitud = geocode_result[0]['geometry']['location']['lng']
    reverse_geocode_result = gmaps.reverse_geocode((Latitud, Longitud))
    #print(reverse_geocode_result[0]['address_components'][3]['types'][0])
    #print(len(reverse_geocode_result))
    cond = False  
    for i in range(len(reverse_geocode_result)):
        for j in range(len(reverse_geocode_result[i]['address_components'])):
            #print(len(reverse_geocode_result[i]['address_components']))
            for k in range(len(reverse_geocode_result[i]['address_components'][j]['types'])):
                #print(reverse_geocode_result[i]['address_components'][j]['types'][k])
                #print(reverse_geocode_result[i]['address_components'][j]['types'][k]=="neighborhood")
                if reverse_geocode_result[i]['address_components'][j]['types'][k]=="neighborhood" and (cond == False):
                    vecin = reverse_geocode_result[i]['address_components'][j]['long_name']
                    #print(vecin)
                    cond = True                
    
    return vecin

def recursividad(valor, vecindario):

    vecin = geolocalizacion(valor)
    if vecin != vecindario:
        return (vecin,valor)
    else: 
        return recursividad(valor+100, vecindario)
