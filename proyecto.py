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
def habitac_alquiladas(lista_habitaciones:list)->dict:
    """
    Representamos tipos de habitaciones por str y un contador de cada habitacion por int
    habitac_alquiladas: List(Str) -> Dict(str:Int)
    habitac_alquiladas recibe la lista del dataset conteniendo los tipos de habitaciones,
    y devuelve un diccionario, que tiene la cantidad de cada tipo de habitacion.
    EJEMPLOS:
        ->habitac_alquiladas(["Private room", "Hotel room", "Entire home/apt"]) == 
        {"Entire home/apt":1, "Private room":1, "Shared room":0, "Hotel room":1}
        ->habitac_alquiladas(habitac alquiladas([]) == 
        {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}) """
    
    dicc_habita={"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

    for habitaciones in lista_habitaciones:
        dicc_habita[habitaciones]+=1

    return dicc_habita

def indice_alquiler(key:str, lista:list, num:int):
    """indice_alquiler toma una key de un diccionario de listas
    la lista que corresponde a esa key y un parametro que es num
    indice_alquiler-> str, list, int
    la funcion indice_alquiler devuelve una lista donde cada elemento es un entero
    que representa la posicion de un elemento de la lista del diccionario que 
    cumpla las condiciones dadas en cada caso respecto de num
    Ejemplos
        ->indice_alquiler("price", [200, 3000, 40, 100], 200)==
        [0,2,3]
        ->indice_alquiler("minimum_nights", [1, 3, 5, 2], 3)==
        [1,2]
    """
    lista_indice=[]
    i=0
    #num sera un parametro que usa la funcion para recibir datos
    #int o float para asi poder recibir datos como la cantidad minima
    #de noches o el precio maximo
    if key=="price":
        for precio in lista:
            if precio and float(precio)<=float(num):
                lista_indice.append(i)
            i+=1
    elif key=="minimum_nights":
        for noches in lista:
            if int(noches)>=num:
               lista_indice.append(i)
            i+=1
    return lista_indice



# PREGUNTA: ¿Que alquileres tienen disponibles una cierta cantidad minima de noches?
def Noches(cant_noches:int, dataset:dict)->dict:
    """
    Esta funcion representa la cantidad minima de noches que se busca
    como un entero
    Noches-> int, Dict{str:list[str]}
    toma una cantidad de noches y guarda las longitud y latitud de todos
    los airbnb que tengan como minimo de noches una cantidad mayor o igual
    a la cantidad de noches ingresada por el usuario"""
    dicc_alquileres={"latitude":[], "longitude":[]}
    index_de_alquiler=[]
    index_de_alquiler=indice_alquiler("minimum_nights", dataset["minimum_nights"], cant_noches)
    
    for x in index_de_alquiler:
        dicc_alquileres["latitude"].append(float(dataset["latitude"][x]))
        dicc_alquileres["longitude"].append(float(dataset["longitude"][x]))
    
    return dicc_alquileres

# PREGUNTA: ¿Que alquileres hay por debajo de un precio seleccionado?
def precios(precio_max:int, tabla:dict):
    """precios: str, dicc{str: list[str]} -> dicc{
    precios, toma el valor ingresado por el usuario y el diccionario que 
    representa el dataset y devuelve un diccionario con los datos de todos 
    los airbnb cuyo precio es menor o igual al precio ingresado
    Ejemplo:
    (los tres puntos son el resto de campos del diccionario)
    ->precios(600, {"price":[600, 400, 1000, 4000, 300], ...})== 
    {...,"price":[600, 400, 300], ...}
    ->precios(62, {"price":[600, 400, 1000, 4000, 300], ...})== {}"""

    # defino el diccionario y asigno las keys
    airbnbs={}
    for llave in tabla:
        airbnbs[llave]=[]
    # guardo el indice de cada airbnb en el dataset que cumple lo que necesito
    index_de_alquiler=[]
    index_de_alquiler=indice_alquiler("price", tabla["price"], precio_max)
    # formo el diccionario con todos los airbnb que cumplen la condicion
    for index in index_de_alquiler:
        for llave in tabla:
            airbnbs[llave].append(tabla[llave][index])
   
    return airbnbs

# PREGUNTA: ¿Cuantos alquileres hay en cada vecindario?
def cont_vecindarios(lista_vecindarios:list)->dict:
    """
    representamos vecindarios como strings dentro de una list y la cantidad 
    de sus apariciones en la lista como ints
    vecindario: str
    cantidad de apariciones de cada vecindarios: int
    cont_vecindarios: List(Str) -> Dict(str:Int)
    cont_vecindarios recibe la lista del dataset de los vecindarios de cada 
    airbnb y devuelve un diccionario, cuyo key es cada vecindario y cada value 
    es un contador de apariciones de dicho vecindario.
    EJEMPLO:
    cont_vecindario(["Copacabana", "Copacabana", "Copacabana", "Centro"]) == {"Copacabana":3,"Centro":1}
    cont_vecindario(["Copacabana"]) == {"Copacabana":1}
    """  
    
    dicc_vecindarios={}

    for vecindarios in lista_vecindarios:
        if vecindarios in dicc_vecindarios:
            dicc_vecindarios[vecindarios]+=1
        else:
            dicc_vecindarios[vecindarios]=1

    return dicc_vecindarios

# PREGUNTA: ¿Cuales alquileres son de determinado tipo de establecimiento?
def clasif_props(tipo_de_prop:list[str], dataset:dict)->dict:
    """clasif_props-> list(str), Dict{str:list[str]}
    clasif_props recibe el tipo de propiedad que llega por el checkbox y recorre
    la seccion de room_type del diccionario que representa el dataset, de ahi busca
    cuando el tipo de prop. ingresado coincide con la value guarda un indice en 
    una lista que seria el numero del airbnb que se esta guardando. Luego recorre
    esa lista accediendo a la latitud y longitud de cada airbnb guardado con su
    posicion para guardarlas en otro diccionario el cual sera returneado.
    EJEMPLO:
    ->clasif_props(["Entire home/apt", "Private room"],
    {...,"room_type":["Entire home/apt","Entire home/apt","Private room"]},...)
    == {"latitude":[0, 90, 38], "longitude":[1, 20, 17]}
    ->clasif_props(["Entire home/apt","Private room", "Shared room","Hotel room"],
    {...,"room_type":["Entire home/apt","Private room","Shared room", "Hotel room"],...})
    =={"latitude":[20, 0, 30, 15],"longitude":[0,21,45, 9]}"""
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

def fecha_valida(mes, mes_review, mes_intervalo, año, año_review, año_intervalo):
    return  (año_review > año_intervalo or 
            (año_review == año_intervalo and mes_review >= mes_intervalo)) \
            and (año_review < año or 
            (año_review == año and mes_review <= mes))

def ultima_review(fecha:str, intervalo:str, tabla:dict):
    partes_fecha=fecha.split("/")
    mes=int(partes_fecha[1])
    año=int(partes_fecha[0])
    mes_intervalo=mes

    dicc_alquileres={"latitude":[], "longitude":[]}
    index_de_alquiler=[]
    if intervalo=="ultimos 3 meses":
        mes_intervalo=mes-3
    elif intervalo=="hace un mes":
        mes_intervalo=mes-1
    elif intervalo=="ultimos 6 meses":
        mes_intervalo=mes-6
    
    if mes_intervalo<=0:
        mes_intervalo=mes_intervalo+12
        año_intervalo=año-1
    else:
        año_intervalo=año

    i=0
    for fechas in tabla["last_review"]:
        if fechas:
            mes_review=int(fechas[5:7])
            año_review=int(fechas[:4])
            if fecha_valida(mes, mes_review, mes_intervalo, año, año_review,
                año_intervalo):
               index_de_alquiler.append(i)
        i=i+1
    
    for indice in index_de_alquiler:
        dicc_alquileres["latitude"].append(float(tabla["latitude"][indice]))
        dicc_alquileres["longitude"].append(float(tabla["longitude"][indice]))

    return dicc_alquileres



#dataset_airbnb.csv
# Funcion Principal:
def main():
    """main es la funcion principal de nuestro programa, es la encargada
    del control del mismo."""
    tabla = {}

    with open("dataset_airbnb.csv") as f:
        tabla = procesam_dataset(f)

    source = habitac_alquiladas(tabla["room_type"])
    # Grafica de barras de las habitaciones alquiladas
    fig, ax = plt.subplots()
    bar_labels = source.keys()
    bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange']
    ax.bar(source.keys(), source.values(), label=bar_labels, color=bar_colors)
    ax.set_ylabel('Cantidad de alquileres')
    ax.set_title('Cantidad de alquileres por tipo de habitacion')
    ax.legend(title='Tipo de habitacion')
    st.pyplot(fig)

    # Slider para elegir la cantidad de personas de la busqueda y mapa que 
    #muestra los alquileres
    valor = st.slider("Minimo de noches que buscan alquilar", min_value=1, 
    max_value=50, value=1)
    dicc_noches=Noches(valor, tabla)
    
    st.map(data=dicc_noches, latitude="latitude", longitude="longitude", zoom=11)
    # Checkbox para elegir el tipo de propiedad buscada y mapa que muestra los 
    #alquileres
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
    # En caso de no tener ningun checkbox tildado, se opta por mostrar 
    #todas las ubicaciones de las propiedades del dataset
    if not clasific:
        clasific = ["Entire home/apt", "Private room", "Shared room", "Hotel room"]
    dicc_clasifprop = clasif_props(clasific, tabla)
    st.map(data=dicc_clasifprop, latitude="latitude", longitude="longitude", zoom=11)
    
    # Widget que toma un precio maximo
    precio = st.number_input("Precio maximo que desea pagar:", value=0, 
    placeholder="", step=1)
    # Abajo estara el programa de la tabla
    dicc_precios = precios(precio, tabla)
    # estara dividida en paginas ya que sino cuando hay muchas filas toda la pagina se traba
    # haciendola lenta y pesada
    page_size = 30
    page = st.number_input("Página", min_value=1,
    max_value=(len(dicc_precios["price"]) // page_size)+1, step=1)
    start = (page - 1) * page_size
    end = start + page_size
    # se crean las subtablas que se van a mostrar en cada pagina
    subtabla={}
    for k, v in dicc_precios.items():
        # Tomar el slice de esa lista entre start y end
        valores_recortados = v[start:end]
        # Guardar en el nuevo diccionario
        subtabla[k] = valores_recortados
    st.table(subtabla, border="horizontal")

    # Grafica de torta de cont_vecindarios
    vecindarios=cont_vecindarios(tabla["neighbourhood"])
    fig, ax = plt.subplots()
    ax.pie(vecindarios.values(), labels=vecindarios.keys(),
    autopct='%1.1f%%', labeldistance = 1.1, radius = 0.5)
    fig.tight_layout()
    ax.axis('equal')
    ax.set_title('Cantidad de valores por vecindario')
    st.pyplot(fig)

    #entrada de fecha actual y el lapso de tiempo que se desea abarcar
    fecha = "2025/09/07"
    Intervalo= st.radio(
    "Tiempo desde la ultima reseña",
    ["menos de un mes", "hace un mes", "ultimos 3 meses", "ultimos 6 meses"],)

    dicc_review=ultima_review(fecha, Intervalo, tabla)
    st.map(data=dicc_review, latitude="latitude", longitude="longitude", zoom=11)

    return 0
main()