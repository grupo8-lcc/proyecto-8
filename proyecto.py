import streamlit as st 
import matplotlib.pyplot as plt
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
    primer_linea = f.readline()
    lista_indice = primer_linea.split(",")
    for indice in lista_indice:
        tabla[indice] = []

    long = len(lista_indice)-1

    for linea in f:
        lista_datos=linea.split(",")
        for x in range(0,long):
            tabla[lista_indice[x]].append(lista_datos[x])

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

    dicc_alquileres={"latitude":[], "longitude":[]}
    index_de_alquiler=[]
    num=str(num)
    i=0
    for noches in dataset["minimum_nights"]:
        if noches==num:
            index_de_alquiler.append(i)
        i+=1
    
    for x in index_de_alquiler:
        dicc_alquileres["latitude"].append(dataset["latitude"][x])
        dicc_alquileres["longitude"].append(dataset["longitude"][x])
    
    return dicc_alquileres



# Graf_p_est:

#dataset_airbnb.csv
# Funcion Principal:
def main():
    """main es la funcion principal de nuestro programa, es la encargada
    del control del mismo."""
    tabla = {}
    with open("prueba.txt") as f:
        tabla = procesam_dataset(f)
    source = habitac_alquiladas(tabla)

    #grafica de barras de las habitaciones alquiladas
    # primer intento ->>>st.bar_chart({"Cantidad": list(source.values())})
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
    Noches(valor, tabla)

    return 0

main()