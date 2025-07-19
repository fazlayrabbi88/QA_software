from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(1)

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")
selected = dropdown.first_selected_option.text

assert selected == "Option 2"
print("✅ Dropdown 'Option 2' selected successfully.")

driver.quit()