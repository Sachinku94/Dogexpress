# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# import time
# import subprocess


# @pytest.fixture(scope="class")
# def setup(request):

#     driver = webdriver.Chrome()

#     driver.get("https://dogexpress.in/")

#     window_size = driver.get_window_size()
#     if window_size["width"] > 767:
#         driver.maximize_window()
#         try:
#             driver.find_element(By.CSS_SELECTOR, ".skip svg").click()
#         except:
#             Exception
#     else:
#         pass

#     driver.execute_script("window.scrollTo(0,500);")
#     request.cls.driver = driver
#     yield
#     driver.quit()
from Config.config_reader import read_config
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="class")
def setup(request):
    # Read configurations for URL and Selenium Grid URL
    base_url = read_config("URL", "base_url")
    selenium_grid_url = read_config("URL", "selenium_grid_url")

    # Set up desired capabilities for the browser (can be customized for other browsers like Chrome, Edge, etc.)
    capabilities = DesiredCapabilities.CHROME.copy()

    # Create a remote WebDriver instance
    driver = webdriver.Remote(
        command_executor=selenium_grid_url, desired_capabilities=capabilities
    )

    driver.get(base_url)

    # Set the driver as an attribute of the test class
    request.cls.driver = driver

    yield

    # Clean up after the test class
    driver.quit()
