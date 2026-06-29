from proyecto import *
#archivo de testing

def test_habitac_alquiladas():

    lista_prueba1=["Entire home/apt","Entire home/apt","Entire home/apt"]
    lista_prueba2=["Entire home/apt","Private room","Shared room","Hotel room"]
    lista_prueba3=[]

    assert habitac_alquiladas(lista_prueba1) == {"Entire home/apt":3, "Private room":0, "Shared room":0, "Hotel room":0}
    assert habitac_alquiladas(lista_prueba2) == {"Entire home/apt":1, "Private room":1, "Shared room":1, "Hotel room":1}
    assert habitac_alquiladas(lista_prueba3) == {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

def test_cont_vecindarios():

    lista_prueba1=["Copacabana", "Copacabana", "Copacabana", "Centro"]
    lista_prueba2=["Copacabana"]
    lista_prueba3=["Copacabana"]

    assert cont_vecindarios(lista_prueba1) == {"Copacabana": 3, "Centro": 1}
    assert cont_vecindarios(lista_prueba2) == {"Copacabana": 1}
    assert cont_vecindarios(lista_prueba3) == {"Copacabana": 1}