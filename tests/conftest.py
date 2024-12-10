import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    #     or webdriver.Edge()
    #     or webdriver.ChromiumEdge()
    #     or webdriver.Safari()
    # )

    driver.get("https://dogexpress.in/")

    window_size = driver.get_window_size()
    if window_size["width"] > 767:
        driver.maximize_window()
        try:
            driver.find_element(By.CSS_SELECTOR, ".skip svg").click()
        except:
            Exception
    else:
        pass

    driver.execute_script("window.scrollTo(0,500);")
    request.cls.driver = driver
    yield
    driver.quit()
