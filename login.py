from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("http://118.179.149.36:7891/login")
driver.maximize_window()
time.sleep(3)

try:
    # --- Enter username and password ---
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("cal@gmail.com ")        # Replace with valid username
    password_field.send_keys("123456789")     # Replace with valid password

    # --- Submit the form ---
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # --- Wait and check redirection ---
    WebDriverWait(driver, 10).until(EC.url_contains("/"))
    time.sleep(2)

    current_url = driver.current_url
    if "http://118.179.149.36:7891/dashboard" in current_url:
        print("✅ Login successful. Redirected to /dashboard.")
    else:
        print("❌ Login failed. Current URL:", current_url)

except Exception as e:
    print("❌ Test error:", e)

finally:
    driver.quit()
