import streamlit as st 
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
    tabla = {}
    primer_linea=f.readline()
    lista_indice=primer_linea.split(",")
    for indice in lista_indice:
        tabla[indice]=[]

    long=len(lista_indice)-1
    
    for linea in f:
        lista_datos=linea.split(",")
        for x in range(0,long):
            tabla[lista_indice[x]].append(lista_datos[x])
    
    return tabla


# PREGUNTA ESTATICA A RESOLVER: ¿QUE TIPOS DE HABITACIONES SON LAS MAS ALQUILADAS?

# habitac_alquiladas:
def habitac_alquiladas(dataset:dict):->tuple
    dicc_habita={"Entire_home/apt":0, "Private_room":0, "Shared_room":0, "Hotel_room":0}
    for habitaciones in dataset["room_type"]:
        if  habitaciones=="Entire home/apt":
            dicc_habita["Entire_home/apt"]+=1
        elif habitaciones=="Private room":
            dicc_habita["Private_room"]+=1
        elif habitaciones=="Shared room":
            dicc_habita["Shared_room"]+=1
        else:
            dicc_habita["Hotel room"]+=1

    return dicc_habita




# Graf_p_est:

#dataset_airbnb.csv
# Funcion Principal:
def main():
    tabla = {}
    with open("dataset_airbnb.csv") as f:
        tabla = procesam_dataset(f)
    habitac_alquiladas(tabla)

    st.bar_chart({"Cantidad": list(habitaciones.values())}, x=list(habitaciones.keys()))
    return 0

main()