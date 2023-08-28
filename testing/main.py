from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import random

def wait(driver:webdriver.Chrome,amount:float):
    driver.implicitly_wait(amount)
    time.sleep(amount)


def init_driver():
    web = "https://pruscitest.onrender.com/"
    driver = webdriver.Chrome()
    driver.get(web)
    wait(driver,1)
    registerTester(driver,"mine@gmail.com","mine1234")
    driver.get(web)
    wait(driver,1)
    registerTester(driver)
    driver.get(web)
    wait(driver,1)
    loginTester(driver,"nashee@gmail.com","12345678910")
    driver.get(web)
    wait(driver,1)
    loginTester(driver)
    

def registerTester(driver, name="mono@gmail.com",psw="12345678910"):
    email = driver.find_element(by=By.ID, value="email_input")
    password = driver.find_element(by=By.ID, value="password_input")
    submit_button = driver.find_element(by=By.ID, value="sumbit_button")
    email.send_keys(name)
    password.send_keys(psw)
    submit_button.click()
    time.sleep(2)
    find_error_msg(driver)

def find_error_msg(driver: webdriver.Chrome):
    try:
        element = driver.find_element(By.ID, "error-message")
        print(element.text)
        time.sleep(5)
        return True
    except:
        print("No hubo error")
        return False

def loginTester(driver:webdriver.Chrome,name="mine@gmail.com",psw="mine1234"): # terminar de implementar
    switch_button = driver.find_element(by=By.ID, value="switch_button")
    switch_button.click()
    driver.implicitly_wait(1)
    time.sleep(1)
    username = driver.find_element(by=By.ID, value="email_input")
    password = driver.find_element(by=By.ID, value="password_input")
    submit_button = driver.find_element(by=By.ID, value="sumbit_button")

    username.send_keys(name)
    password.send_keys(psw)
    submit_button.click()
    wait(driver,2)
    if(find_error_msg(driver)):
        return
    homeTester(driver)
    
    #  try:
    #   message = driver.find_element(by=By.CLASS_NAME, value="error-container")
    #   value = message.text
    #   assert value == "Logged in!"
    #   print("ELEMENT FOUND")
    #except:
    #   print("ELEMENT NOT FOUND")



   

def homeTester(driver: webdriver.Chrome):
    armas=[ driver.find_element(by=By.ID, value="rifle"), driver.find_element(by=By.ID, value="subfusil"), driver.find_element(by=By.ID, value="explosivo") ]
    selector_arma= driver.find_element(by=By.ID, value="selector_arma")
    direccion= driver.find_element(by=By.ID, value="direccion")
    box= driver.find_element(by=By.ID, value="box")
    submit= driver.find_element(by=By.ID, value="submit")
    direccion.send_keys("La casa de leto")
    for x in armas:
        x.click()
    if( random.randint(0,1)==0):
        box.click()
        
    time.sleep(3)
    submit.click()
    time.sleep(3)
    print(Alert(driver).text)
    time.sleep(3)
    Alert(driver).accept()
    time.sleep(2)
    driver.quit()


init_driver()
