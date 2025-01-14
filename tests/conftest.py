# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from Config.config_reader import read_config


# @pytest.fixture(scope="class")
# def setup(request):
#     # Read base URL from config
#     CHROMEDRIVER_VERSION = "131.0.6778.205"
#     path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
#     base_url = read_config("URL", "base_url")

#     # Initialize Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     # Maximize the window on start
#     # Disable extensions

#     # Setup Service object using the chromedriver path from ChromeDriverManager
#     service = Service(path)

#     # Initialize the driver with the service and options
#     driver = webdriver.Remote(service=service, options=chrome_options)

#     # Open the base URL in the browser
#     driver.get(base_url)

#     # Attach the driver to the test class (so tests can access it)
#     request.cls.driver = driver

#     # Yield the driver to run tests
#     yield driver

#     # Quit the driver after tests complete
#     driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config_reader import read_config


@pytest.fixture(scope="class")
def setup(request):
    # Read base URL and Selenium Grid Hub URL from config
    base_url = read_config("URL", "base_url")
    remote_url = read_config(
        "SELENIUM_GRID", "selenium_grid_url"
    )  # Replace with your Selenium Grid URL

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        "--headless"
    )  # Add this if running in headless mode is required

    # Desired capabilities (optional, for remote browser specifics)
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",  # You can specify specific versions as well
        "enableVNC": True,  # For enabling visual feedback in some Selenium Grid setups
        "enableVideo": False,  # Disable video recording if not needed
    }

    # Initialize the Remote WebDriver
    driver = webdriver.Remote(
        command_executor=remote_url,
        options=chrome_options,
        desired_capabilities=capabilities,
    )

    # Open the base URL in the browser
    driver.get(base_url)

    # Attach the driver to the test class (so tests can access it)
    request.cls.driver = driver

    # Yield the driver to run tests
    yield driver

    # Quit the driver after tests complete
    driver.quit()
