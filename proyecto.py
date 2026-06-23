import streamlit as st 
import matplotlib.pyplot as plt
import csv
st.title ("Proyecto Grupal Programacion")
st.write ("Empecemos a trabajar en equipo")

#   AL TERMINAR
# git add . 
# git commit -m "Descripcion breve de lo hecho"
# git push

#   AL COMENZAR
# git pull

# 09-06-26
# ESTRUCTURA UTILIZADA PARA TRATAR LOS DATOS DEL ARCHIVO:
# DICT: Key: categoria - Value: List . ej CLAVE:id - VALOR: List of int (ids) -> ELEGIDA
# LIST OF DICT: Elem of list (Dict) -> Dict: CLAVE - VALOR ej.Dict {id: 002, host_name: Nacho, .....}

# Procesam_dataset:
def procesam_dataset(f):
    """procesam_dataset: FILE -> Dict(List(Str))
    procesam_dataset recibe un archivo, y lo procesa de la siguiente forma.
    Crea un diccionario vacío, donde se guardaran las categorias como listas.
    La funcion recorre el archivo linea por linea, guardando en primer lugar las categorias,
    y luego los datos de cada linea en cada categoria correspondiente."""
    tabla = {}
    lector=csv.reader(f)
    lista_indice = next(lector)
    for indice in lista_indice:
        tabla[indice] = []

    long = len(lista_indice)

    for lista_datos in lector:
        #agrega los datos al diccionario 
        for x in range(0,long):
            tabla[lista_indice[x]].append(lista_datos[x])
    #intento fallido de lectura del dataset sin bibliotecas
    # for linea in f:
    #     #para armar la linea en caso que este dividida en distintas filas
    #     while linea[-2]!="," and linea[-1]=="\n":
    #         linea=linea+f.readline()
    #         print(linea)
    #     #para ignorar las comas en caso que un nombre tenga una coma
    #     primer_comilla=linea.find('"')
    #     fin_comilla=linea.find('"', primer_comilla+1)
    #     if primer_comilla!=-1 and fin_comilla!=-1:
    #         nombre=linea[primer_comilla+1:fin_comilla]
    #         nombre=nombre.replace(",","")
    #         linea=linea[:primer_comilla+1]+nombre+linea[fin_comilla:]
    #     lista_datos=linea.split(",")
    #     #agrega los datos al diccionario 
    #     for x in range(0,long):
    #         tabla[lista_indice[x]].append(lista_datos[x])
    return tabla


# PREGUNTA ESTATICA A RESOLVER: ¿QUE TIPOS DE HABITACIONES SON LAS MAS ALQUILADAS?

# habitac_alquiladas:
def habitac_alquiladas(dataset:dict)->dict:
    """habitac_alquiladas: Dict(List(Str)) -> Dict(Int)
    habitac_alquiladas recibe la estructura con la que se representa el dataset,
    y devuelve un diccionario, que tiene la cantidad de cada tipo de habitacion.
    EJEMPLOS:
        habitac_alquiladas({"room_type":["Private_room", "Hotel_room", "Entire_home/apt"]}) -> {"Entire_home/apt":1, "Private_room":1, "Shared_room":0, "Hotel_room":1}
        habitac_alquiladas(habitac_alquiladas({"room_type":[]}) -> {"Entire_home/apt":0, "Private_room":0, "Shared_room":0, "Hotel_room":0}) """
    
    dicc_habita={"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

    for habitaciones in dataset["room_type"]:
        dicc_habita[habitaciones]+=1

    return dicc_habita

def Noches(num:int, dataset:dict)->dict:
    """Noches-> int, disct{str:list[str]}
    Noches recibe el numero que llega por el slider y recorre la seccion de minimum_nigths del diccionario
    que representa el dataset, de ahi busca cuando el numero del slider coincide con la value guarda un indice en una lista
    que seria el numero del airbnb que se esta guardando. Luego recorre esa lista accediendo a la latitud y longitud
    de cada airbnb guardado con su posicion para guardarlas en otro diccionario el cual sera returneado"""
    dicc_alquileres={"latitude":[], "longitude":[]}
    index_de_alquiler=[]
    num=str(num)
    i=0
    for noches in dataset["minimum_nights"]:
        if noches==num:
            index_de_alquiler.append(i)
        i+=1
    
    for x in index_de_alquiler:
        dicc_alquileres["latitude"].append(float(dataset["latitude"][x]))
        dicc_alquileres["longitude"].append(float(dataset["longitude"][x]))
    
    return dicc_alquileres

#dataset_airbnb.csv
# Funcion Principal:
def main():
    """main es la funcion principal de nuestro programa, es la encargada
    del control del mismo."""
    tabla = {}
    #tenemos problemas para leer el data set pero no sabemos cual ya distinguimos los dos casos problematicos
    #y los resolvimos se puede ver en el archivo de prueba.txt pero sin embargo sigue tirando un error de index
    with open("dataset_airbnb.csv") as f:
        tabla = procesam_dataset(f)
    source = habitac_alquiladas(tabla)

    #grafica de barras de las habitaciones alquiladas
    fig, ax = plt.subplots()
    bar_labels = source.keys()
    bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange']
    ax.bar(source.keys(), source.values(), label=bar_labels, color=bar_colors)
    ax.set_ylabel('Cantidad de alquileres')
    ax.set_title('Cantidad de alquileres por tipo de habitacion')
    ax.legend(title='Tipo de habitacion')
    st.pyplot(fig)

    #slider para elegir la cantidad de personas de la busqueda
    valor = st.slider("Minimo de noches que buscan alquilar", min_value=1, max_value=100, value=0)
    st.write("", valor)
    dicc_noches=Noches(valor, tabla)
    #pudimos poner el slider e intentamos usar el mapa con el archivo de prueba pero aunque no tiraba ningun error
    #el mapa igual no se mostraba
    st.map(data=dicc_noches, latitude="latitude", longitude="longitude", zoom=11)
    return 0

main()
st.write ("Empecemos a trabajar en equipo")