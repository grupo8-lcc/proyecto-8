from proyecto import *
#archivo de testing

def test_habitac_alquiladas():

    lista_prueba1=["Entire home/apt","Entire home/apt","Entire home/apt"]
    lista_prueba2=["Entire home/apt","Private room","Shared room","Hotel room"]
    lista_prueba3=[]
    
    assert habitac_alquiladas(lista_prueba1) == {"Entire home/apt":3, "Private room":0, "Shared room":0, "Hotel room":0}
    assert habitac_alquiladas(lista_prueba2) == {"Entire home/apt":1, "Private room":1, "Shared room":1, "Hotel room":1}
    assert habitac_alquiladas(lista_prueba3) == {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

def test_indice_alquiler():

    lista_prueba1=[200, 3000, 40, 100]
    lista_prueba2=[1, 3, 5, 2]
    

    assert indice_alquiler("price", lista_prueba1 , 200) == [0,2,3]
    assert indice_alquiler("minimum_nights", lista_prueba2, 3) == [1,2]
    assert indice_alquiler("neighbourhood", lista_prueba2, 3) == []

def test_Noches():
    dicc1={"latitude":[120, 300, 40], "longitude":[500, -100, 30], "minimum_nights":[2, 3, 6]}
    dicc2={"latitude":[120, 300, 40], "longitude":[500, -100, 30], "minimum_nights":[5, 3, 1]}
    dicc3={"latitude":[], "longitude":[], "minimum_nights":[]}
    
    assert Noches(3, dicc1) == {"latitude":[300, 40], "longitude":[-100, 30]}
    assert Noches(3, dicc2) == {"latitude":[120, 300], "longitude":[500, -100]}
    assert Noches(7, dicc1) == {"latitude":[], "longitude":[]}
    assert Noches(20, dicc3) == {"latitude":[], "longitude":[]}

def test_precios():
    dicc1={'id': ['30', '6', '255'], 'name': ['Apa', 'Rio', 'Man'], 'host_id': ['154', '475', '103'], 'host_name': ['Gaetano', 'Renato Silva Vianna', 'Andre Melo'], 'neighbourhood_group': ['', '', ''], 'neighbourhood': ['Campo', 'Jacarepaguá', 'Recreio dos Bandeirantes'], 'latitude': ['-22.92161', '-22.97187', '-23.02954'], 'longitude': ['-43.55507', '-43.41419', '-43.49523'], 'room_type': ['Entire home/apt', 'Entire home/apt', 'Entire home/apt'], 'price': ['', '665.0', '2104.0'], 'minimum_nights': ['5', '1', '1'], 'number_of_reviews': ['0', '0', '163'], 'last_review': ['', '', '2025-07-18'], 'reviews_per_month': ['', '', '1.85'], 'calculated_host_listings_count': ['1', '160', '1'], 'availability_365': ['363', '365', '347'], 'number_of_reviews_ltm': ['0', '0', '17']}

    assert precios(20, dicc1) =={'id': [],'name': [],'host_id': [],'host_name': [],'neighbourhood_group': [],'neighbourhood': [],'latitude': [],'longitude': [],'room_type': [],'price': [],'minimum_nights': [],'number_of_reviews': [],'last_review': [],'reviews_per_month': [],'calculated_host_listings_count': [],'availability_365': [],'number_of_reviews_ltm': []}
    assert precios(1000, dicc1) == {'id': [ '6'], 'name': ['Rio'], 'host_id': ['475'], 'host_name': ['Renato Silva Vianna'], 'neighbourhood_group': [''], 'neighbourhood': ['Jacarepaguá'], 'latitude': ['-22.97187'], 'longitude': ['-43.41419'], 'room_type': ['Entire home/apt',], 'price': ['665.0'], 'minimum_nights': ['1'], 'number_of_reviews': ['0'], 'last_review': [''], 'reviews_per_month': [''], 'calculated_host_listings_count': ['160'], 'availability_365': [ '365'], 'number_of_reviews_ltm': ['0']}

def test_cont_vecindarios():

    lista_prueba1=["Copacabana", "Copacabana", "Copacabana", "Centro"]
    lista_prueba2=["Copacabana"]

    assert cont_vecindarios(lista_prueba1) == {"Copacabana": 3, "Centro": 1}
    assert cont_vecindarios(lista_prueba2) == {"Copacabana": 1}

def test_clasif_props():
    lista1=["Entire home/apt", "Private room"]
    dicc1= {"room_type":["Entire home/apt", "shared room", "Entire home/apt"], "latitude":[120, 300, 40], "longitude":[500, -100, 30]}
    dicc2= {"room_type":["shared room", "shared room", "Hotel room"], "latitude":[120, 300, 40], "longitude":[500, -100, 30]}

    assert clasif_props(lista1, dicc1) == {"latitude":[120, 40], "longitude":[500, 30]}
    assert clasif_props(lista1, dicc2) == {"latitude":[], "longitude":[]}

def test_fecha_valida():
    assert fecha_valida(9, 3, 2026, 2026, "hace un mes") == False
    assert fecha_valida(9, 8, 2026, 2026, "hace un mes")== True
    assert fecha_valida(9, 8, 2026, 2025, "ultimos 3 meses")== False
    assert fecha_valida(5, 12, 2026, 2025, "ultimos 6 meses")== True

def test_ultima_review():
    dicc1={"last_review":["2023-09-23"], "latitude":"88998", "longitude":"89090"}

    assert ultima_review("2025/07/03", "hace un mes", dicc1) == {"latitude":[], "longitude":[]}
    