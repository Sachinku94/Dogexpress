import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.config_reader import read_config


@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    # CHROMEDRIVER_VERSION = "131.0.6778.205"
    # path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
    base_url = read_config("URL", "base_url")

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Maximize the window on start
    # Disable extensions

    # Setup Service object using the chromedriver path from ChromeDriverManager
    # service = Service(path)

    # Initialize the driver with the service and options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the base URL in the browser
    driver.get(base_url)

    # Attach the driver to the test class (so tests can access it)
    request.cls.driver = driver

    # Yield the driver to run tests
    yield driver

    # Quit the driver after tests complete
    driver.quit()
