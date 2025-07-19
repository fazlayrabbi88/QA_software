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

    username_field.send_keys("cal@gmail.com ")
    password_field.send_keys("123456789")

    # --- Submit the form ---
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # --- Wait and check redirection ---
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    time.sleep(2) # Give it a moment to fully load

    current_url = driver.current_url
    if "http://118.179.149.36:7891/dashboard" in current_url:
        print("✅ Login successful. Redirected to /dashboard.")

        # --- Add Logout Functionality ---
        print("Attempting to log out...")
        try:
            # Step 1: Click the element that opens the dropdown menu
            # YOU NEED TO REPLACE THIS LOCATOR with the actual locator for the profile picture/name that you click
            # to open the dropdown. Inspect the "Crown Agro Ltd 1" or the profile picture itself.
            # Example: It might be a div, a button, an img, or an anchor tag.
            # Try to find a unique ID, or a specific class.
            
            # Placeholder: You MUST replace this with the actual locator
            # E.g., if the clickable area has an ID like "userProfileArea":
            # profile_dropdown_trigger = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.ID, "userProfileArea"))
            # )
            # Or if it's based on the text "Crown Agro Ltd 1":
            profile_dropdown_trigger = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Crown Agro Ltd 1')]"))
            )
            
            profile_dropdown_trigger.click()
            print("Profile dropdown trigger clicked.")
            
            # Step 2: Wait for the dropdown menu container to be visible
            # Using the CSS selector you provided
            dropdown_container = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".absolute.min-w-[200px].bottom-0.right-0.top-[70px].z-50.bg-gray-200.h-fit.py-4.w-full.rounded-md.shadow-lg"))
            )
            print("Dropdown container is visible.")
            time.sleep(1) # Give a short moment for elements inside to become interactive

            # Step 3: Click the "Logout" option within the dropdown
            # This is reliable as long as 'Logout' is the exact text inside the li
            logout_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li[text()='Logout']"))
            )
            logout_element.click()
            print("Logout element clicked.")

            # Step 4: Wait for the URL to change back to login page after logout
            WebDriverWait(driver, 10).until(EC.url_contains("/login"))
            time.sleep(2) # Give it a moment to fully load the new page

            if "http://118.179.149.36:7891/login" in driver.current_url:
                print("✅ Logout successful. Redirected back to login page.")
            else:
                print(f"❌ Logout seemed successful, but not redirected to login. Current URL: {driver.current_url}")

        except Exception as logout_e:
            print(f"❌ Logout failed or element not found: {logout_e}")
            print("Action required: Please correctly identify and set the locator for the profile dropdown trigger (the element you click to open the menu).")
            print("Also, ensure the 'Logout' text inside the dropdown is consistently 'Logout'.")

    else:
        print(f"❌ Login failed. Current URL: {current_url}")

except Exception as e:
    print(f"❌ Test error during login or initial setup: {e}")

finally:
    print("Closing browser...")
    driver.quit()