from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pag
import pyperclip as pc
import openpyxl as opx
import time

from acciones_sel.credential import get_cer_path, get_key_path, get_password

liga_portal = "https://pstcdi.clouda.sat.gob.mx/Home/"

# Procedimiento para copiar y pegar un texto
def candp(text):
    pc.copy(text)
    pag.hotkey('ctrl', 'v')
    pc.copy('')

# Procedimiento que valida que la página de login esté lista para interactuar
def validar_pagina(d):
    print("=> Esperando 5 segundos para validar página de login")
    d.implicitly_wait(5.0)
    print("=> Validando página de login")
    try:
        txt_cert = d.find_element(By.ID, "txtCertificate")
        txt_keyy = d.find_element(By.ID, "txtPrivateKey")
        txt_pass = d.find_element(By.ID, "privateKeyPassword")
        btn_subm = d.find_element(By.ID, "submit")
        print("=> Página validada con éxito")
    except: return False
    return True

# Procedimieno para abrir el navegador
def abrir_navegador(d):
    print("=> Abriedo navegador")
    d.maximize_window()
    return d


# Prodecimiento para ir a la página
def ir_pagina(driver):
    print("=> Yendo a la página")
    driver.get(liga_portal)

def login(rfc, d):

    # Obtener credenciales
    # Estos son los datos que vamos a necesitar
    cer_path = get_cer_path(rfc)
    key_path = get_key_path(rfc)
    password = get_password(rfc)


    d = abrir_navegador(d)   
    ir_pagina(d)

    if not validar_pagina(d): # Nos aseguramos de que estén los elementos para proseguir
        
        print("=> No se ha cargado bien la página de login")

    else:

        # Obtenemos los controles
        txt_cert = d.find_element(By.ID, "txtCertificate")
        txt_keyy = d.find_element(By.ID, "txtPrivateKey")
        txt_pass = d.find_element(By.ID, "privateKeyPassword")
        btn_subm = d.find_element(By.ID, "submit")
        
        # Ingresar el certificado
        txt_cert.click()
        time.sleep(3)
        candp(cer_path)
        time.sleep(3)
        pag.press("enter")
        time.sleep(3)

        # Ingresar el archivo key
        txt_keyy.click()
        time.sleep(3)
        candp(key_path)
        time.sleep(3)
        pag.press("enter")
        time.sleep(3)

        # Ingresar la contraseña
        txt_pass.click()
        time.sleep(3)
        candp(password)
        time.sleep(3)

        # Hacer click en submit
        btn_subm.click()

        return d