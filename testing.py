from proyecto import *
#archivo de testing

def test_habitac_alquiladas():

    dicc_prueba1={"room_type":["Entire home/apt","Entire home/apt","Entire home/apt"]}
    dicc_prueba2={"room_type":["Entire home/apt","Private room","Shared room","Hotel room"]}
    dicc_prueba3={"room_type":[]}

    assert habitac_alquiladas(dicc_prueba1) == {"Entire home/apt":3, "Private room":0, "Shared room":0, "Hotel room":0}
    assert habitac_alquiladas(dicc_prueba2) == {"Entire home/apt":1, "Private room":1, "Shared room":1, "Hotel room":1}
    assert habitac_alquiladas(dicc_prueba3) == {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}