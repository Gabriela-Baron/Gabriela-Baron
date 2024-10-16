import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el navegador Chrome
driver = webdriver.Chrome()

# Abrir una página web (Google)
driver.get("https://www.google.com")
print(driver.title)  # Imprimir el título de la página para confirmar que se cargó

# Abrir la página de login
driver.get("https://practicetestautomation.com/practice-test-login/")

# Esperar a que el campo Username esté disponible y escribir en él
username_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "username"))
)
username_field.click()
username_field.send_keys("student")

# Esperar a que el campo Password esté disponible y escribir en él
password_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)
password_field.click()
password_field.send_keys("Password123")

# Esperar a que el botón Submit esté disponible y hacer clic en él
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
submit_button.click()

# Esperar hasta que se cargue la página después de iniciar sesión
WebDriverWait(driver, 10).until(
    EC.title_contains("Practice")  # Cambia esto según el título esperado de la página
)

# Abrir la página "Practice"
driver.get("https://practicetestautomation.com/practice/")

# Abrir la página "Test Exceptions"
driver.get("https://practicetestautomation.com/practice-test-exceptions/")

# Esperar a que el botón "Add" esté visible y hacer clic en él
add_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "add_btn"))
)
add_button.click()  # Hacer clic en el botón "Add"

# Esperar hasta que el campo de texto esté habilitado
text_field = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@class='input-field' and not(@disabled)]"))
)

# Escribir "hamburguesas" en el campo de texto
text_field.click()
text_field.clear()
text_field.send_keys("hamburguesas")

# Esperar a que el botón save esté disponible y hacer clic
save_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.id, "save_btn"))
)
save_button.click()

# Esperar a que el botón remove esté disponible y hacer clic
remove_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "remove_btn"))
)
remove_button.click()

# Abrir la página "Courses"
driver.get("https://practicetestautomation.com/courses/")

# Esperar unos segundos para ver el resultado
time.sleep(10)

# Pausa para ver el resultado antes de cerrar
# Cerrar el navegador
##driver.quit()