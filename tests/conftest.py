import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config_reader import read_config
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    base_url = read_config("URL", "base_url")
    CHROMEDRIVER_VERSION = "131.0.6778.205"

    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument(
        "--disable-gpu"
    )  # Disable GPU (useful for headless mode)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource issues
    chrome_options.add_argument(
        "--remote-debugging-port=9222"
    )  # Avoid DevToolsActivePort issues

    # Uncomment this line if you want to run in headless mode
    # chrome_options.add_argument("--headless")  # Run browser in headless mode

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(
        ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install,
        options=chrome_options,
    )

    # Open the base URL
    driver.get(base_url)

    # Attach the driver to the test class
    request.cls.driver = driver

    # Yield the driver for use in tests
    yield driver

    # Quit the driver after the tests are complete
    driver.quit()
