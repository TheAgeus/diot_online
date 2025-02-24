import os

fiels_path = "C:\\Users\\DIOT\\Desktop\\Diot-online\\fiel\\"

def get_cer_path(rfc):
    rfc_folder = [f for f in os.listdir(fiels_path) if rfc in f][0] + "\\"
    files = os.listdir(fiels_path + rfc_folder)
    cer_name = [f for f in files if f.endswith(".cer")][0]
    cer_path = fiels_path + rfc_folder + cer_name
    return cer_path

def get_key_path(rfc):
    rfc_folder = [f for f in os.listdir(fiels_path) if rfc in f][0] + "\\"
    files = os.listdir(fiels_path + rfc_folder)
    key_name = [f for f in files if f.endswith(".key")][0]
    key_path = fiels_path + rfc_folder + key_name
    return key_path

def get_password(rfc):
    rfc_folder = [f for f in os.listdir(fiels_path) if rfc in f][0] + "\\"
    files = os.listdir(fiels_path + rfc_folder)
    password_name = [f for f in files if f.endswith(".txt")][0]
    password_path = fiels_path + rfc_folder + password_name
    
    with open(password_path, "r", encoding="utf-8") as file:
        contenido = file.read()
    return(contenido)
