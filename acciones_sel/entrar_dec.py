from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui as pag
from datetime import datetime
import time

# Procedimiento para picar el circulo de la dec
def picar_dec(rfc, d):
    circulito_picado = False
    d.get("https://pstcdi.clouda.sat.gob.mx/Declaracion/PerfilDeclaracion")
    section_obl = d.find_element(By.ID, "sectionObligaciones")
    divs = section_obl.find_elements(By.TAG_NAME, "div")
    for div in divs:
        if div.text == "Declaración Informativa de Operaciones con Terceros (DIOT)":
            lab = div.find_element(By.TAG_NAME, "label")
            span = lab.find_element(By.TAG_NAME, "span")
            clase = span.get_attribute("class")
            if clase == "checkOff":
                span.click()
                print("=> Se hace click sobre obligacion diot para: " + rfc)
                circulito_picado = True
            else:
                print("=> Ya se encuentra realizada obligacion diot para: " + rfc)
                circulito_picado = False
    return circulito_picado


# Procedimiento para ingresar el año y el mes y continuar
def ingresa_per_para_continuar(d):
    # Restar el mes (mes anterior)
    ahora = datetime.now()
    mes = ahora.month   
    año = ahora.year    
    if mes == 1:
        mes = 12
        año = año - 1
    else:
        mes = mes - 1   

    # Obtener selects de ejercicio y periodicidad
    año_sel = d.get_elemet(By.ID, "ejercicio")
    per_sel = d.get_elemet(By.ID, "periocidad")

    año_sel_obj = Select(año_sel)                   # Seleccionar año
    año_sel_obj.select_by_visible_text(str(año))

    per_sel_obj = Select(per_sel)                   # Seleccionar periodicidad
    per_sel_obj.select_by_index(1)  

    # Obtener select del mes
    time.sleep(1)
    prs_sel = d.get_elemet(By.ID, "periodos")
    prs_sel_obj = Select(prs_sel) # Seleccionar el mes
    prs_sel_obj.select_by_index(mes) 

    # Obtener select del tipo de declaracion
    time.sleep(1)
    tde_sel = d.get_elemet(By.ID, "tipodeclaracion")
    tde_sel_obj = Select(tde_sel)  # Seleccionar el mes
    tde_sel_obj.select_by_index(1) # 1: Normal, 2: Normal por correccion fiscal

    # Picarle a siguente
    time.sleep(1)
    pag.press("tab")
    pag.press("enter")

