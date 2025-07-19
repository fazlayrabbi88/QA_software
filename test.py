from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    """Sets up and returns a Chrome WebDriver instance."""
    return webdriver.Chrome(ChromeDriverManager().install())

# 1. Automate a Login Form - Successful & Failed
def test_login_form():
    driver = setup_driver()
    try:
        print("\n--- Test Case 1: Login Form Automation ---")
        driver.get("https://the-internet.herokuapp.com/login")

        # Successful Login
        print("Attempting successful login...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login button")

        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()

        # Assert successful login
        WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
        success_message = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in success_message
        print(f"Login successful! Message: {success_message.strip()}")

        # Log out
        logout_button = driver.find_element(By.CSS_SELECTOR, ".button.secondary.radius")
        logout_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        print("Logged out successfully.")

        # Failed Login
        print("Attempting failed login with incorrect password...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login button")

        username_field.send_keys("tomsmith")
        password_field.send_keys("IncorrectPassword!") # Incorrect password
        login_button.click()

        # Assert failed login
        error_message = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in error_message or "Your password is invalid!" in error_message
        print(f"Login failed as expected! Message: {error_message.strip()}")

    except Exception as e:
        print(f"An error occurred during login form test: {e}")
    finally:
        driver.quit()

# 2. Interact with Checkboxes
def test_checkboxes():
    driver = setup_driver()
    try:
        print("\n--- Test Case 2: Checkboxes Interaction ---")
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(1) # Give a moment for elements to load

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkbox1 = checkboxes[0]
        checkbox2 = checkboxes[1]

        # Check status of the first checkbox and assert it's unchecked
        assert not checkbox1.is_selected()
        print(f"Checkbox 1 initial status: {'Checked' if checkbox1.is_selected() else 'Unchecked'} (as expected)")

        # Click the first checkbox to check it
        checkbox1.click()
        print("Clicked Checkbox 1.")
        time.sleep(0.5) # Allow click to register

        # Assert that the first checkbox is now checked
        assert checkbox1.is_selected()
        print(f"Checkbox 1 status after click: {'Checked' if checkbox1.is_selected() else 'Unchecked'} (as expected)")

        # Check status of the second checkbox and assert it's already checked
        assert checkbox2.is_selected()
        print(f"Checkbox 2 initial status: {'Checked' if checkbox2.is_selected() else 'Unchecked'} (as expected)")

    except Exception as e:
        print(f"An error occurred during checkboxes test: {e}")
    finally:
        driver.quit()

# 3. Select from a Dropdown Menu
def test_dropdown_menu():
    driver = setup_driver()
    try:
        print("\n--- Test Case 3: Dropdown Menu Selection ---")
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(1)

        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)

        # Use the Select class to choose "Option 2" by its visible text
        select.select_by_visible_text("Option 2")
        print("Selected 'Option 2' from the dropdown.")
        time.sleep(0.5)

        # Assert that "Option 2" is now the selected option
        selected_option = select.first_selected_option
        assert selected_option.text == "Option 2"
        print(f"Currently selected option: {selected_option.text} (as expected)")

    except Exception as e:
        print(f"An error occurred during dropdown test: {e}")
    finally:
        driver.quit()

# 4. Handle a JavaScript Alert
def test_javascript_alert():
    driver = setup_driver()
    try:
        print("\n--- Test Case 4: JavaScript Alert Handling ---")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(1)

        # Click the button labeled "Click for JS Alert"
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        print("Clicked 'Click for JS Alert' button.")

        # Switch focus from the main window to the alert pop-up
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Assert that the text within the alert is "I am a JS Alert"
        alert_text = alert.text
        assert alert_text == "I am a JS Alert"
        print(f"Alert text: '{alert_text}' (as expected)")

        # Accept the alert
        alert.accept()
        print("Accepted the alert.")
        time.sleep(0.5)

        # Assert that the result text on the main page says "You successfully clicked an alert"
        result_text = driver.find_element(By.ID, "result").text
        assert result_text == "You successfully clicked an alert"
        print(f"Result text: '{result_text}' (as expected)")

    except Exception as e:
        print(f"An error occurred during JavaScript alert test: {e}")
    finally:
        driver.quit()

# 5. Verify Dynamic Content
def test_dynamic_content():
    driver = setup_driver()
    try:
        print("\n--- Test Case 5: Verify Dynamic Content ---")
        driver.get("https://the-internet.herokuapp.com/dynamic_content")
        time.sleep(2) # Give time for content to load initially

        # Locate one of the text blocks below the images and store its content
        # There are 3 rows, each with an image and text. Let's target the second text block for example.
        initial_text_element = driver.find_element(By.XPATH, "(//div[@class='large-10 columns'])[2]")
        initial_content = initial_text_element.text
        print(f"Initial content of the second text block: \n'{initial_content}'")

        # Refresh the page
        print("Refreshing the page...")
        driver.navigate().refresh()
        time.sleep(2) # Give time for new content to load

        # Locate the same text block again
        refreshed_text_element = driver.find_element(By.XPATH, "(//div[@class='large-10 columns'])[2]")
        refreshed_content = refreshed_text_element.text
        print(f"Content of the second text block after refresh: \n'{refreshed_content}'")

        # Assert that the new text content is not the same as the original text
        assert initial_content != refreshed_content
        print("Dynamic content verified: Text content changed after refresh (as expected).")

    except Exception as e:
        print(f"An error occurred during dynamic content test: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_form()
    test_checkboxes()
    test_dropdown_menu()
    test_javascript_alert()
    test_dynamic_content()