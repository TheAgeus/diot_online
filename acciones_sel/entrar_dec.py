from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui as pag
from datetime import datetime
import time

# Procedimiento para picar el circulo de la dec
def picar_dec(rfc, d):
    circulito_picado = False
    d.get("https://pstcdi.clouda.sat.gob.mx/Declaracion/PerfilDeclaracion")

    # Suele dar algun error aquí, mejor recargar
    while True:
        try:
            time.sleep(3)
            section_obl = d.find_element(By.ID, "sectionObligaciones")
            break
        except:
            d.get("https://pstcdi.clouda.sat.gob.mx/Declaracion/PerfilDeclaracion")  

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
    d.switch_to.window(d.window_handles[-1])
    time.sleep(3)
    año_sel = d.find_element(By.ID, "ejercicio")
    per_sel = d.find_element(By.ID, "periodicidad")

    año_sel_obj = Select(año_sel)                   # Seleccionar año
    año_sel_obj.select_by_visible_text(str(año))

    per_sel_obj = Select(per_sel)                   # Seleccionar periodicidad
    per_sel_obj.select_by_index(1)  

    # Obtener select del mes
    time.sleep(1)
    prs_sel = d.find_element(By.ID, "periodos")
    prs_sel_obj = Select(prs_sel) # Seleccionar el mes
    prs_sel_obj.select_by_index(mes) 

    # Obtener select del tipo de declaracion
    time.sleep(1)
    tde_sel = d.find_element(By.ID, "tipodeclaracion")
    tde_sel_obj = Select(tde_sel)  # Seleccionar el mes

    is_complementaria = False
    for option in tde_sel_obj.options:
        if option.accessible_name == "Complementaria": 
            is_complementaria = True
    if is_complementaria:
        tde_sel_obj.select_by_index(1) # 1: Complementaria, 2: Complementaria por correciion fiscal, 3: Complementaria por dictamen
        time.sleep(1)
        tdc_sel = d.find_element(By.ID, "tipocomplementaria")
        tdc_sel_obj = Select(tdc_sel)  # Seleccionar tipo de complementaria
        tdc_sel_obj.select_by_index(2) # 1: Dejar sin efecto, 2: Modificacion de declaracion, 3: Declaracion no presentada
    else:
        tde_sel_obj.select_by_index(1) # 1: Normal, 2: Normal por correccion fiscal

    # Picarle a siguente
    time.sleep(1)
    pag.press("tab")
    pag.press("enter")

    return d
