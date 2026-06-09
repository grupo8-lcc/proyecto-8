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
def procesam_dataset(f:FILE):-> dict
    tabla = {}
    lista=["hola", "si", "no"]
    linea = readline(f)
    for linea in f:
        tabla[id] = []
# PREGUNTA ESTATICA A RESOLVER: ¿QUE TIPOS DE HABITACIONES SON LAS MAS ALQUILADAS?

# habitac_alquiladas:
def habitac_alquiladas(dataset:dict):->tuple


# Graf_p_est:


# Funcion Principal:
def main():
    tabla = {}
    with open("dataset_airbnb.csv") as f:
        tabla = procesam_dataset(f)