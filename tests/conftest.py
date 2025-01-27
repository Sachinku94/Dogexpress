import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.config_reader import read_config
import os


@pytest.fixture(scope="class")
def setup(request):

    CHROMEDRIVER_VERSION = "131.0.6778.205"
    base_url = read_config("URL", "base_url")

    os.environ["WDM_LOG_LEVEL"] = "0"
    os.environ["WDM_LOCAL"] = "1"
    os.environ["WDM_CACHE_DIR"] = "/tmp/wdm_cache"
    os.environ["WDM_RETRY"] = "5"

    path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(base_url)
    request.cls.driver = driver
    yield driver
    driver.quit()
    # # Read base URL from config
    # CHROMEDRIVER_VERSION = "131.0.6778.205"
    # base_url = read_config("URL", "base_url")

    # # Ensure necessary environment variables are set
    # os.environ["WDM_LOG_LEVEL"] = "0"  # Suppress webdriver-manager logs
    # os.environ["WDM_LOCAL"] = "1"  # Use local cache for chromedriver

    # # Install ChromeDriver using webdriver-manager
    # path = ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()

    # # Initialize Chrome options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode for Jenkins
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    # chrome_options.add_argument(
    #     "--disable-dev-shm-usage"
    # )  # Overcome shared memory issues
    # chrome_options.add_argument(
    #     "--disable-gpu"
    # )  # Disable GPU for headless environments
    # chrome_options.add_argument("--window-size=1920,1080")  # Set default window size

    # # Setup Service object using the chromedriver path from ChromeDriverManager
    # service = Service(path)

    # # Initialize the driver with the service and options
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # # Open the base URL in the browser
    # driver.get(base_url)

    # # Attach the driver to the test class (so tests can access it)
    # request.cls.driver = driver

    # # Yield the driver to run tests
    # yield driver

    # # Quit the driver after tests complete
    # driver.quit()
