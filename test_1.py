from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get("http://118.179.149.36:7891/login")
driver.maximize_window()
time.sleep(2)  # Wait for page to load

try:
    # --- Locate input fields ---
    username_input = driver.find_element(By.NAME, "username")  # Try By.ID or By.NAME based on actual page
    password_input = driver.find_element(By.NAME, "password")

    # --- Enter test credentials ---
    username_input.send_keys("cal@gmail.com")  # Replace with your test username
    password_input.send_keys("123456789")  # Replace with your test password

    # --- Click Login ---
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    

    current_url = driver.current_url
    if "/dashboard" in current_url:
        print("✅ Login successful. Redirected to /dashboard.")
    else:
        print("❌ Login failed. Current URL:", current_url)
            



    # Wait for redirect or response
    time.sleep(3)



finally:
    driver.quit()
