from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui as pag
import time

def declarar_cero(d):
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

    # li_totales = [li for li in d.find_elements(By.TAG_NAME, "li") if li.text == "Totales"][0]
    # li_totales.click()

    time.sleep(3)
    pag.press("tab")
    pag.press("enter")

    time.sleep(3)
    d.find_element(By.ID, "btnEnviaDec").click()

    time.sleep(10)
    pag.press("enter")

    time.sleep(10)
    d.find_element(By.ID, "linkDescargaPDF").click()

    time.sleep(10)
