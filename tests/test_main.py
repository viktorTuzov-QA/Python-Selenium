# импортируем модули и отдельные классы



from selenium.webdriver.common.by import By


# каждый тест должен начинаться с test_
def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
	
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    browser.get(url=url)
		# ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")

    
    element.click()
		# ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    items_class = '[class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'
    elements = browser.find_elements(By.CSS_SELECTOR, value=items_class)
    elements[0].click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"