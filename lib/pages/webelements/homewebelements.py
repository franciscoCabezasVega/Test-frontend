from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, 'h2.AQWr-mod-margin-bottom-xlarge.c0qPo')
    signin_button = (By.CSS_SELECTOR, "div[aria-label='Abrir navegación principal']")
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    name_tag_input = (By.CSS_SELECTOR, "div[aria-label='Tipo de viaje Ida y vuelta']")
    name_dropdown_column_input = (By.CSS_SELECTOR, "div.c15uy.c15uy-mod-variant-default")
    search_tag_input = (By.CSS_SELECTOR, "button.RxNS.RxNS-mod-stretch")
    cancel_button = (By.CSS_SELECTOR, "div.c_neb-item-button")
    create_column_disabled_button = (By.CSS_SELECTOR, "span.J-sA-label")