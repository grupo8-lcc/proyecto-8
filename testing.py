from proyecto import *
#archivo de testing

def test_habitac_alquiladas():

    dicc_prueba1={"room_type":["Entire home/apt","Entire home/apt","Entire home/apt"]}
    dicc_prueba2={"room_type":["Entire home/apt","Private room","Shared room","Hotel room"]}
    dicc_prueba3={"room_type":[]}

    assert habitac_alquiladas(dicc_prueba1) == {"Entire home/apt":3, "Private room":0, "Shared room":0, "Hotel room":0}
    assert habitac_alquiladas(dicc_prueba2) == {"Entire home/apt":1, "Private room":1, "Shared room":1, "Hotel room":1}
    assert habitac_alquiladas(dicc_prueba3) == {"Entire home/apt":0, "Private room":0, "Shared room":0, "Hotel room":0}

def test_Noches():
    dicc1={"latitude":[120, 300, 40], "longitude":[500, -100, 30], "minimum_nights":[2, 3, 6]}
    dicc2={"latitude":[120, 300, 40], "longitude":[500, -100, 30], "minimum_nights":[5, 3, 1]}
    dicc3={"latitude":[], "longitude":[], "minimum_nights":[]}
    
    assert Noches(3, dicc1) == {"latitude":[120, 300], "longitude":[500, -100]}
    assert Noches(3, dicc2) == {"latitude":[300, 40], "longitude":[-100, 30]}
    assert Noches(1, dicc1) == {"latitude":[], "longitude":[]}
    assert Noches(20, dicc3) == {"latitude":[], "longitude":[]}

def test_precios():
    dicc1={'id': ['30', '6', '255'], 'name': ['Apa', 'Rio', 'Man'], 'host_id': ['154', '475', '103'], 'host_name': ['Gaetano', 'Renato Silva Vianna', 'Andre Melo'], 'neighbourhood_group': ['', '', ''], 'neighbourhood': ['Campo', 'Jacarepaguá', 'Recreio dos Bandeirantes'], 'latitude': ['-22.92161', '-22.97187', '-23.02954'], 'longitude': ['-43.55507', '-43.41419', '-43.49523'], 'room_type': ['Entire home/apt', 'Entire home/apt', 'Entire home/apt'], 'price': ['', '665.0', '2104.0'], 'minimum_nights': ['5', '1', '1'], 'number_of_reviews': ['0', '0', '163'], 'last_review': ['', '', '2025-07-18'], 'reviews_per_month': ['', '', '1.85'], 'calculated_host_listings_count': ['1', '160', '1'], 'availability_365': ['363', '365', '347'], 'number_of_reviews_ltm': ['0', '0', '17'], 'license': []}
    dicc2={"price":[1000, 6000, 3000, 400]}
    dicc3={"price":[]}

    assert precios(1000, dicc1) == {'id': [ '6'], 'name': ['Rio'], 'host_id': ['475'], 'host_name': ['Renato Silva Vianna'], 'neighbourhood_group': ['', '', ''], 'neighbourhood': ['Jacarepaguá'], 'latitude': ['-22.97187'], 'longitude': ['-43.41419'], 'room_type': ['Entire home/apt',], 'price': ['665.0'], 'minimum_nights': ['1'], 'number_of_reviews': ['0'], 'last_review': [''], 'reviews_per_month': [''], 'calculated_host_listings_count': ['160'], 'availability_365': [ '365'], 'number_of_reviews_ltm': ['0'], 'license\n': []}