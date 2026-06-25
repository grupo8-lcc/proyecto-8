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
        # agrega los datos al diccionario 
        for x in range(0,long):
            tabla[lista_indice[x]].append(lista_datos[x])
    # intento fallido de lectura del dataset sin bibliotecas
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
        habitac_alquiladas({"room_type":["Private room", "Hotel room", "Entire home/apt"]}) -> {"Entire home/apt":1, "Private room":1, "Shared room":0, "Hotel room":1}
        habitac_alquiladas(habitac alquiladas({"room type":[]}) -> {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}) """
    
    dicc_habita={"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

    for habitaciones in dataset["room_type"]:
        dicc_habita[habitaciones]+=1

    return dicc_habita

# PREGUNTA: ¿Que alquileres tienen disponibles una cierta cantidad minima de noches?
def Noches(num:int, dataset:dict)->dict:
    """Noches-> int, Dict{str:list[str]}
    Noches recibe el numero que llega por el slider y recorre la seccion de minimum_nigths del diccionario
    que representa el dataset, de ahi busca cuando el numero del slider coincide con la value guarda un indice en una lista
    que seria el numero del airbnb que se esta guardando. Luego recorre esa lista accediendo a la latitud y longitud
    de cada airbnb guardado con su posicion para guardarlas en otro diccionario el cual sera returneado"""
    dicc_alquileres={"latitude":[], "longitude":[]}
    index_de_alquiler=[]
    num=num
    i=0
    for noches in dataset["minimum_nights"]:
        if int(noches)<=num:
            index_de_alquiler.append(i)
        i+=1
    
    for x in index_de_alquiler:
        dicc_alquileres["latitude"].append(float(dataset["latitude"][x]))
        dicc_alquileres["longitude"].append(float(dataset["longitude"][x]))
    
    return dicc_alquileres

# PREGUNTA: ¿Que alquileres hay por debajo de un precio seleccionado?
def precios(precio_max:int, tabla:dict):
    """precios: str, dicc{str: list[str]} -> dicc{
    precios, toma el valor ingresado por el usuario y el diccionario que representa el dataset
    y devuelve un diccionario con los datos de todos los airbnb cuyo precio es menor o igual
    al precio ingresado
    Ejemplo:
    (los tres puntos son el resto de campos del diccionario)
    precios(600, {"price":[600, 400, 1000, 4000, 300], ...})== {...,"price":[600, 400, 300], ...}
    precios(62, {"price":[600, 400, 1000, 4000, 300], ...})== {}"""

    # defino el diccionario y asigno las keys
    airbnbs={}
    for llave in tabla:
        airbnbs[llave]=[]
    # guardo el indice de cada airbnb en el dataset que cumple lo que necesito
    index_de_alquiler=[]
    i=0
    for precio in tabla["price"]:
        if precio and float(precio)<=float(precio_max):
            index_de_alquiler.append(i)
        i+=1
    # formo el diccionario con todos los airbnb que cumplen la condicion
    for index in index_de_alquiler:
        for llave in tabla:
            airbnbs[llave].append(tabla[llave][index])
   
    return airbnbs

# PREGUNTA: ¿Cuantos alquileres hay en cada vecindario?
def cont_vecindarios(dataset:dict)->dict:
    """cont_vecindarios: Dict(List(Str)) -> Dict(Int)
    cant_vecindarios recibe la estructura con la que se representa el dataset,
    y devuelve un diccionario, que tiene la cantidad de cada vecindario.
    EJEMPLO:
    cont_vecindario({"neighbourhood":["Copacabana", "Copacabana", "Copacabana", "Centro"]}) == {"Copacabana":3,"Centro":1}
    cont_vecindario({"neighbourhood":["Copacabana"]}) == {"Copacabana":1}
    """  
    
    dicc_vecindarios={}

    for vecindarios in dataset["neighbourhood"]:
        try:
            dicc_vecindarios[vecindarios]+=1
        except:
            dicc_vecindarios[vecindarios]=1

    return dicc_vecindarios

# PREGUNTA: ¿Cuales alquileres son de determinado tipo de establecimiento?
def clasif_props(tipo_de_prop:list[str], dataset:dict)->dict:
    """clasif_props-> list(str), Dict{str:list[str]}
    clasif_props recibe el tipo de propiedad que llega por el checkbox y recorre la seccion de room_type del diccionario
    que representa el dataset, de ahi busca cuando el tipo de prop. ingresado coincide con la value guarda un indice en 
    una lista que seria el numero del airbnb que se esta guardando. Luego recorre esa lista accediendo a la latitud y 
    longitud de cada airbnb guardado con su posicion para guardarlas en otro diccionario el cual sera returneado.
    EJEMPLO:
    clasif_props(["Entire home/apt", "Private room"],{...,"room_type":["Entire home/apt","Entire home/apt","Private room"]},...) == {"latitude":[0, 90, 38], "longitude":[1, 20, 17]}
    clasif_props(["Entire home/apt","Private room", "Shared room","Hotel room"],{...,"room_type":["Entire home/apt","Private room","Shared room", "Hotel room"],...})=={"latitude":[20, 0, 30, 15],"longitude":[0,21,45, 9]}"""
    dicc_alq_filtrados={"latitude":[], "longitude":[]}
    index_de_alquiler = {}
    for check in tipo_de_prop:
        index_de_alquiler[check]=[]
    # index_de_alquiler={"Entire home/apt":[], "Private room":[], "Shared room":[], "Hotel room":[]}
    i=0
    #for propiedad in tipo_de_prop:
    for prop in dataset["room_type"]:
            #if prop==propiedad:
            if prop in index_de_alquiler.keys():
                index_de_alquiler[prop].append(i)
            i+=1
        #i = 0
    for lista_dp in index_de_alquiler.values():
        for ind_p in lista_dp:
            dicc_alq_filtrados["latitude"].append(float(dataset["latitude"][ind_p]))
            dicc_alq_filtrados["longitude"].append(float(dataset["longitude"][ind_p])) 
    return dicc_alq_filtrados

#dataset_airbnb.csv
# Funcion Principal:
def main():
    """main es la funcion principal de nuestro programa, es la encargada
    del control del mismo."""
    tabla = {}
    # tenemos problemas para leer el data set pero no sabemos cual ya distinguimos los dos casos problematicos
    # y los resolvimos se puede ver en el archivo de prueba.txt pero sin embargo sigue tirando un error de index
    with open("dataset_airbnb.csv") as f:
        tabla = procesam_dataset(f)
    source = habitac_alquiladas(tabla)

    # Grafica de barras de las habitaciones alquiladas
    fig, ax = plt.subplots()
    bar_labels = source.keys()
    bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange']
    ax.bar(source.keys(), source.values(), label=bar_labels, color=bar_colors)
    ax.set_ylabel('Cantidad de alquileres')
    ax.set_title('Cantidad de alquileres por tipo de habitacion')
    ax.legend(title='Tipo de habitacion')
    st.pyplot(fig)

    # Slider para elegir la cantidad de personas de la busqueda y mapa que muestra los alquileres
    valor = st.slider("Minimo de noches que buscan alquilar", min_value=1, max_value=50, value=1)
    dicc_noches=Noches(valor, tabla)
    st.map(data=dicc_noches, latitude="latitude", longitude="longitude", zoom=11)

    # Checkbox para elegir el tipo de propiedad buscada y mapa que muestra los alquileres
    # "Entire home/apt"  | "Private room" | "Shared room" | "Hotel room"
    ent = st.checkbox("Entire home/apt")
    priv_room = st.checkbox("Private room")
    shd_room = st.checkbox("Shared room")
    hotel_r = st.checkbox("Hotel room")
    clasific =[]
    if ent:
        clasific.append("Entire home/apt")
    if priv_room:
        clasific.append("Private room")
    if shd_room:
        clasific.append("Shared room")
    if hotel_r:
        clasific.append("Hotel room")
    # En caso de no tener ningun checkbox tildado, se opta por mostrar todas las ubicaciones de las propiedades del dataset
    if not clasific:
        clasific = ["Entire home/apt", "Private room", "Shared room", "Hotel room"]
    dicc_clasifprop = clasif_props(clasific, tabla)
    st.map(data=dicc_clasifprop, latitude="latitude", longitude="longitude", zoom=11)
    
    # Widget que toma un precio maximo
    precio = st.number_input("Precio maximo que desea pagar:", value=0, placeholder="", step=1)
    # Tabla donde se muestran los airbnb que cumplen con ese precio o menor
    dicc_precios = precios(precio, tabla)
    # Mostrar como tabla
    # estara dividida en paginas ya que sino cuando hay muchas filas toda la pagina se traba
    # haciendola lenta y pesada
    # Parametros para las paginas
    page_size = 30
    page = st.number_input("Página", min_value=1, max_value=(len(dicc_precios["price"]) // page_size)+1, step=1)
    start = (page - 1) * page_size
    end = start + page_size
    # se crean las subtablas que se van a mostrar en cada pagina
    subtabla={}
    # k y v se refieren a keys y values
    for k, v in dicc_precios.items():
        # Tomar el slice de esa lista entre start y end
        valores_recortados = v[start:end]
        # Guardar en el nuevo diccionario
        subtabla[k] = valores_recortados
    st.table(subtabla, border="horizontal")


    # Grafica de torta de cont_vecindarios
    vecindarios=cont_vecindarios(tabla)
    fig, ax = plt.subplots(figsize=(1,1))
    ax.pie(vecindarios.values(), labels=vecindarios.keys(), autopct='%1.1f%%', labeldistance = 1.1, radius = 1.1)
    fig.tight_layout()
    ax.axis('equal')
    ax.set_title('Cantidad de valores por vecindario')
    st.pyplot(fig)

    return 0
main()