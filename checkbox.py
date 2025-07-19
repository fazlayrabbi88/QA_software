from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(1)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checkbox1 = checkboxes[0]
checkbox2 = checkboxes[1]

assert not checkbox1.is_selected()
checkbox1.click()
assert checkbox1.is_selected()
print("✅ Checkbox 1 checked successfully.")

assert checkbox2.is_selected()
print("✅ Checkbox 2 was already checked.")

driver.quit()