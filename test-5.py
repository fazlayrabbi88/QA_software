from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_form(driver):
    print("\n--- Test 1: Login Form ---")
    driver.get("https://the-internet.herokuapp.com/login")

    # Successful login
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "#login button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text
    print("✅ Successful login verified.")

    # Logout
    driver.find_element(By.CSS_SELECTOR, ".button.secondary.radius").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    # Failed login
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword!")
    driver.find_element(By.CSS_SELECTOR, "#login button").click()
    assert "Your username is invalid!" in driver.find_element(By.ID, "flash").text
    print("✅ Failed login verified.")

def test_checkboxes(driver):
    print("\n--- Test 2: Checkbox Interaction ---")
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(1)

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    checkbox1, checkbox2 = checkboxes[0], checkboxes[1]

    assert not checkbox1.is_selected()
    checkbox1.click()
    assert checkbox1.is_selected()
    print("✅ Checkbox 1 checked successfully.")

    assert checkbox2.is_selected()
    print("✅ Checkbox 2 was already checked.")

def test_dropdown_menu(driver):
    print("\n--- Test 3: Dropdown Selection ---")
    driver.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(1)

    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")
    selected = dropdown.first_selected_option.text

    assert selected == "Option 2"
    print("✅ Dropdown 'Option 2' selected successfully.")

def test_javascript_alert(driver):
    print("\n--- Test 4: JavaScript Alert Handling ---")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert"
    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert result == "You successfully clicked an alert"
    print("✅ JavaScript alert handled successfully.")

def test_dynamic_content(driver):
    print("\n--- Test 5: Dynamic Content ---")
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    time.sleep(2)

    old_text = driver.find_element(By.XPATH, "(//div[@class='large-10 columns'])[2]").text
    driver.refresh()
    time.sleep(2)
    new_text = driver.find_element(By.XPATH, "(//div[@class='large-10 columns'])[2]").text

    assert old_text != new_text
    print("✅ Dynamic content changed after refresh.")

def run_all_tests():
    driver = webdriver.Chrome()
    try:
        test_login_form(driver)
    except Exception as e:
        print(f"❌ Login Test Failed: {e}")

    try:
        test_checkboxes(driver)
    except Exception as e:
        print(f"❌ Checkbox Test Failed: {e}")

    try:
        test_dropdown_menu(driver)
    except Exception as e:
        print(f"❌ Dropdown Test Failed: {e}")

    try:
        test_javascript_alert(driver)
    except Exception as e:
        print(f"❌ Alert Test Failed: {e}")

    try:
        test_dynamic_content(driver)
    except Exception as e:
        print(f"❌ Dynamic Content Test Failed: {e}")

    driver.quit()
    print("\n✅ Test session completed.")

if __name__ == "__main__":
    run_all_tests()
