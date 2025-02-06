from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, 'h2.AQWr-mod-margin-bottom-xlarge.c0qPo')
    signin_button = (By.CSS_SELECTOR, "div[aria-label='Abrir navegación principal']")
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')