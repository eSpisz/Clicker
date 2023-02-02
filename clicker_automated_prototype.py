# UWAGI dawac time.sleep(), szczegolnie w przejsciach na stronie żeby strony mogly sie zaladowac, inaczej moze wywalac bledy o nieistniejacych elementach strony (nie zdaza sie zaladowac)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# obiekt przegladarki
browser = webdriver.Firefox()
#*********tu wpisac urzadzenia*********
devices=[] 
deparments=["WwP/TEF-MFD","WwP/TEF1-IB","WwP/TEF4","WwP/MOE1.6"]
wait=WebDriverWait(browser,5)
counter=0

#*********blok elementow wraz z id*********
applications_id="WIN_0_304316340"
ciname_id="arid_WIN_1_200000020"
buisness_service_id="arid_WIN_1_536870914"
search_button_id="WIN_1_300001100"
ci_search_results_id="WIN_1_300460300"
view_button_id="WIN_1_400000024"
logout_button_id="WIN_0_300000044"
table_devices="T300460300"
add_button_id="WIN_2_350100005"
#*********koniec bloku*********

# funkcja ladujaca strone
def Load_website():
    global original_window
    browser.get("https://rb-smt.de.bosch.com")
    time.sleep(2)
    original_window = browser.window_handles[0]

# szukanie urzadzen
def Device_search():
    browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div/div/div[4]/div[57]/div[2]/div/div[2]/table/tbody/tr[zmienna]/td[3]')
    
#wybieranie w menu linii, ci type itp
def Search(device):
    """arg: aktualne urzadzenie"""
    global counter
    #wejscie w menu z boku ci advanced search
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="WIN_0_304316340"]')))
    browser.find_element(By.XPATH,'//*[@id="WIN_0_304316340"]').click()
    browser.find_element(By.LINK_TEXT,'Asset Management').click()
    browser.find_element(By.LINK_TEXT,"CI Advanced Search").click()
    
    #wpisanie aktualnej linii
    time.sleep(1)
    browser.find_element(By.XPATH,'//*[@id="arid_WIN_1_200000020"]').clear()
    browser.find_element(By.XPATH,'//*[@id="arid_WIN_1_200000020"]').send_keys(device)
    time.sleep(1)
    
    #chowa pasek aplication, bo zostaje wysuniety i nie da sie search button wcisnac, smieszna sprawa, jesli ponizszy if zwaraca falsz, uruchamia try except w main, wiec tu tez musi byc oblusga bledow : )
    try:
        if counter!=0:
            browser.find_element(By.XPATH, '//*[@id="WIN_0_304316350"]').click()
    except:
        pass
    
    # klikanie buisness service
    browser.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/div/div/div[4]/div[13]/a').click()
    time.sleep(1)
    if counter==0:
        browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[3]/td[1]').click()
    else:
        browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/table/tbody/tr[3]/td[1]').click()
    counter =+ 1
    time.sleep(2)

    #klikanie search button
    browser.find_element(By.ID,search_button_id).click()

    # focus na urzadzenie
    time.sleep(1)
    browser.find_element(By.ID,view_button_id).click()
    
    wait.until(ec.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div[19]/div[2]/div[2]/div/dl/dd[4]/span[2]/a")))
    browser.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div[19]/div[2]/div[2]/div/dl/dd[4]/span[2]/a").click()
    
    # wywalenie dariusza
    time.sleep(1)
    browser.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div[19]/fieldset[4]/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]").click()
    time.sleep(1)
    browser.find_element(By.XPATH,'//*[@id="WIN_2_350500020"]').click()
    time.sleep(1)
    popup=browser.window_handles[1]
    Change_focus(popup)
    
    #potwierdzenie usuniecia w okienku
    time.sleep(1)
    browser.find_element(By.XPATH,'//*[@id="WIN_0_302180500"]').click()
    time.sleep(1)
    Change_focus(original_window)

    #wejscie w related people
    time.sleep(1)
    wait.until(ec.element_to_be_clickable((By.ID,add_button_id)))
    browser.find_element(By.ID,add_button_id).click()
    

def people_organization():
    #zmiana focusu na nowe okno
    time.sleep(1)
    popup=browser.window_handles[1]
    Change_focus(popup)
    wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[1]/fieldset/div/div[1]/a")))

    #wybranie opcji "type" na people organization
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[1]/fieldset/div/div[1]/a").click()   
    browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]").click()

    #wybranie opcji "level"
    browser.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[1]/fieldset/div/div[2]/a").click()
    browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/table/tbody/tr[2]").click()

    #zmienianie focusu na okienko
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="arid_WIN_0_304370951"]')))
    
    #wpisanie w polu company
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_304370951"]').send_keys("CC")
    
    #wybranie rsa...
    browser.find_element(By.XPATH,'//*[@id="arid_WIN_0_810000000"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[5]/td[2]').click()
    
    
    for department in deparments:
        #wpisanie w polu organization
        browser.find_element(By.XPATH,'//*[@id="arid_WIN_0_301531200"]').clear()
        browser.find_element(By.XPATH,'//*[@id="arid_WIN_0_301531200"]').send_keys(department)
        
        #klikanie search
        browser.find_element(By.XPATH,'//*[@id="WIN_0_304289680"]').click()
        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]')))
        
        #focus na element w wynikach
        browser.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').click()
        wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="WIN_0_300073200"]')))
        
        #klikanie add
        browser.find_element(By.XPATH,'//*[@id="WIN_0_300073200"]').click()

def support_group():
    #wybranie opcji "type"
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[1]/fieldset/div/div[1]/a").click()   
    browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/table/tbody/tr[3]/td[1]").click()
    
    #wybranie w search support group
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_304372111"]').send_keys("BCI")
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_1000000014"]').send_keys("BCI")
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_1000000015"]').send_keys("RSA Operations CSG")
    
    #klikanie search
    browser.find_element(By.XPATH,'//*[@id="WIN_0_301304500"]').click()
    
    #focus na element w wynikach
    browser.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[2]/fieldset/div/div/div/div/div[2]/fieldset/div/div[5]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]').click()
    
    #klikanie select role -> supported by
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_301527000"]').clear()
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_301527000"]').send_keys("Supported by")
    
    #wybranie rsa...
    time.sleep(1)
    browser.find_element(By.XPATH,'//*[@id="arid_WIN_0_810000000"]').click()
    browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[10]/td[1]').click()
    
    #klikanie add
    browser.find_element(By.XPATH,'//*[@id="WIN_0_300073200"]').click()

def local_itm():
    #wybranie opcji "type"  
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[1]/fieldset/div/div[1]/a").click()
    browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[1]').click()
    
    #wpisanie imie i nazwiska
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_1000000019"]').send_keys("Andrzej")
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_1000000018"]').send_keys("Lapczynski")
    
    #klikanie search
    browser.find_element(By.XPATH, '//*[@id="WIN_0_301867800"]').click()
    
    #focus na element zwrocony po search
    browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[2]/fieldset/div/div/div/div/div[1]/fieldset/div/div[11]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]').click()
    
    #czyszczenie opcji przed wpisaniem
    browser.find_element(By.XPATH, '//*[@id="arid_WIN_0_301527000"]').clear()
    
    #ustawienie select role
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[3]/fieldset/div/div[3]/a').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[1]').click()
    
    #ustawienie role description
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[3]/div/div/div[1]/fieldset/div/div/div/div[3]/fieldset/div/div[2]/a').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[8]/td[1]').click()
    
    #klikanie add
    browser.find_element(By.XPATH, '//*[@id="WIN_0_300073200"]').click()
    
    #wyjscie z okna
    browser.find_element(By.XPATH, '//*[@id="WIN_0_300005000"]').click()

    #zmiana focusu okna
    Change_focus(original_window)

    #zapisanie
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="WIN_2_300000300"]').click()

# konczenie bota, wylogowanie i zamkniecie przegladarki
def Quit():
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="WIN_0_300000044"]').click()
    time.sleep(1)
    browser.quit()

def Change_focus(window):
    browser.switch_to.window(window)
    
def main():
    # zaladowanie strony
    Load_website()
    # obsluga bledu, wylogowanie przed zamknieciem przegladarki, ultra wazne, inaczej sesja nie wygasnie i trzeba czekac
    try:
        for device in devices:
            time.sleep(2)
            Search(device)
            # klikanie people organization
            people_organization()
            # klikanie support group
            support_group()
            # klikanie Local-ITM (people)
            local_itm()
                
    except:
        browser.find_element(By.XPATH, '//*[@id="WIN_0_300000044"]').click()
        time.sleep(2)
        browser.quit()
        quit()
    Quit()
if __name__=="__main__":
    main()
