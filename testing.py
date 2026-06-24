import proyecto

def testing():
    
    dicc_prueba={"room_type":["Entire home/apt","Entire home/apt","Entire home/apt"]}
    assert habitac_alquiladas(dicc_prueba) == {"Entire home/apt":3, "Private room":0, "Shared room":0, "Hotel room":0}