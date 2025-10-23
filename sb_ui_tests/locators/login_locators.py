from selenium.webdriver.common.by import By


EMAIL = (By.CSS_SELECTOR, "form .input input.input__textfield[type='text'], form input[name='name']")
PASSWORD = (By.CSS_SELECTOR, "form .input input.input__textfield[type='password']")
SUBMIT = (By.CSS_SELECTOR, "form button[type='submit'], form .button_button_type_primary__1O7Bx")
FORGOT_LINK = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
TOGGLE_PASSWORD = (By.CSS_SELECTOR, ".input__icon.input__icon-action, .input__icon-action")



