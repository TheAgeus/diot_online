from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pag
import pyperclip as pc
import openpyxl as opx
import os

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
def abrir_navegador():
    print("=> Abriedo navegador")
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# Prodecimiento para ir a la página
def ir_pagina(driver):
    print("=> Yendo a la página")
    driver.get(liga_portal)

def login():
    d = abrir_navegador()   
    ir_pagina(d)
    if not validar_pagina(d): # Nos aseguramos de que estén los elementos para proseguir
        print("=> No se ha cargado bien la página de login")
    else:
        # Estos son los datos que vamos a necesitar
        cer_path = ""
        key_path = ""
        password = ""

        # Ingresar el certificado
        # Ingresar el archivo key
        # Ingresar la contraseña
        # Hacer click en submit
        # Obtenemos los controles
        txt_cert = d.find_element(By.ID, "txtCertificate")
        txt_keyy = d.find_element(By.ID, "txtPrivateKey")
        txt_pass = d.find_element(By.ID, "privateKeyPassword")
        btn_subm = d.find_element(By.ID, "submit")

        txt_cert.click()
        d.implicitly_wait(3)
        candp(cer_path)
        d.implicitly_wait(3)
        pag.press("enter")
        d.implicitly_wait(3)

        txt_keyy.click()
        d.implicitly_wait(3)
        candp(key_path)
        d.implicitly_wait(3)
        pag.press("enter")
        d.implicitly_wait(3)

        txt_pass.click()
        d.implicitly_wait(3)
        candp(password)
        d.implicitly_wait(3)

        btn_subm.click()

        return d