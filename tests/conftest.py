import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import subprocess


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


# subprocess.run(["python", "-m", "pytest", "--alluredir=allure-results"], check=True)

# # Serve the Allure report (opens in browser)
# subprocess.run(["allure", "serve", "allure-results"], check=True)
# C:\Users\<YourUsername>\scoop\apps\allure\current\bin
