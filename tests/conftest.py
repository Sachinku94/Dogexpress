import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.config_reader import read_config


@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    base_url = read_config("URL", "base_url")

    # Set up Chrome options for headless execution in Docker
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Required for running in Docker
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome memory limitations
    chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
    chrome_options.add_argument(
        "--window-size=1920,1080"
    )  # Ensure consistent resolution

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open base URL
    driver.get(base_url)

    # Attach driver to test class
    request.cls.driver = driver

    yield driver  # Provide driver instance for tests

    driver.quit()  # Cleanup after tests
