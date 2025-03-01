from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui as pag
import time
import pyperclip as pc
from acciones_sel.login import get_cer_path, get_key_path, get_password

# Procedimiento para copiar y pegar un texto
def candp(text):
    pc.copy(text)
    pag.hotkey('ctrl', 'v')
    pc.copy('')

def declarar_cero(d, rfc=None, es_moral=False):
    # Esperar el select
    existe_select = False
    select_obj = None
    while not existe_select:
        try:
            #d = d.switch_to(d.window_handles[0])
            selects = d.find_elements(By.TAG_NAME, "select")
            for select in selects:
                if existe_select: break
                select_obj_i = Select(select)
                options = select_obj_i.options
                for option in options:
                    if existe_select: break
                    if option.accessible_name == "La presenta sin operaciones":
                        select_obj = select_obj_i
                        existe_select = True
                        break
        except: 
            pag.press("f5")
            time.sleep(5)

    select_obj.select_by_visible_text("Sin selección")
    select_obj.select_by_visible_text("La presenta sin operaciones")
    
    time.sleep(3)
    pag.press("tab")
    pag.press("enter")

    li_totales = [li for li in d.find_elements(By.TAG_NAME, "li") if li.text == "Totales"][0]
    li_totales.click()

    time.sleep(3)
    pag.press("tab")
    pag.press("enter")

     # Si datos adicionales tiene un 1 en rojo
    time.sleep(3)
    for a in d.find_elements(By.TAG_NAME, "a"):
        if a.text == "Datos adicionales1":
            a.click()

            time.sleep(3)
            pag.scroll(100)
            time.sleep(1)

            sel = [se for se in d.find_elements(By.TAG_NAME, "select") if se.is_displayed()][0]
            sel_obj_da = Select(sel)
            sel_obj_da.select_by_visible_text('No')

            pag.scroll(-300)

    time.sleep(3)
    d.find_element(By.ID, "btnEnviaDec").click()

    time.sleep(10)
    pag.press("enter")

    # Si es moral, debo de cargar otra vez las credenciales
    time.sleep(10)
    d.find_element(By.ID, "btnCert").click()
    time.sleep(3)
    candp(get_cer_path(rfc))
    time.sleep(3)
    pag.press("enter")
    time.sleep(3)

    d.find_element(By.ID, "btnPrivateKey").click()
    time.sleep(3)
    candp(get_key_path(rfc))
    time.sleep(3)
    pag.press("enter")
    time.sleep(3)

    pag.press("tab")
    time.sleep(3)
    candp(get_password(rfc))
    time.sleep(3)
    pag.press("enter")
    time.sleep(3)

    pag.press("tab")
    pag.press("tab")
    pag.press("enter")


    time.sleep(5)
    matches = [a.text for a in d.find_elements(By.CLASS_NAME, "modal-header") if a.text == 'Intente nuevamente.']
    if len(matches) > 0:
        return "Error. No se pudo descargar."

    while True:
        try:
            d.find_element(By.ID, "linkDescargaPDF").click()
            break
        except: None

    time.sleep(10)
    return d
