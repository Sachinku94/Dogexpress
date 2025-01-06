from Config.config_reader import read_config
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    base_url = read_config("URL", "base_url")
    driver = webdriver.Chrome()
    driver.get(base_url)
    # Add other setup steps here...
    request.cls.driver = driver
    yield
    driver.quit()


# from Config.config_reader import read_config
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="class")
# def setup(request):
#     # Read the base URL from your configuration
#     base_url = read_config("URL", "base_url")

#     # Initialize the Chrome driver using webdriver-manager
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get(base_url)

#     # Assign the driver instance to the test class
#     request.cls.driver = driver

#     yield
#     driver.quit()
