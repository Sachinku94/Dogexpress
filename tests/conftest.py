# from Config.config_reader import read_config
# import pytest
# from selenium import webdriver
# @pytest.fixture(scope="class")
# def setup(request):
#     base_url = read_config("URL", "base_url")
#     driver = webdriver.Edge()
#     driver.get(base_url)
#     # Add other setup steps here...
#     request.cls.driver = driver
#     yield
#     driver.quit()




# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import pytest
# from Config.config_reader import read_config


# @pytest.fixture(scope="class")
# def setup(request):
#     base_url = read_config("URL", "base_url")

#     # Use WebDriverManager to automatically handle the Edge driver download and installation
#     driver = webdriver.Chrome(ChromeDriverManager(driver_version="131.0.6778.205").install())
#     driver.get(base_url)
#     request.cls.driver = driver
#     yield
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Config.config_reader import read_config

@pytest.fixture(scope="class")
def setup(request):
    # Read the base URL from the configuration file
    base_url = read_config("URL", "base_url")

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
    chrome_options.add_argument("--no-sandbox")  # Prevent sandboxing issues
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

    # Install the correct version of ChromeDriver using WebDriverManager
    driver_path = ChromeDriverManager(driver_version="131.0.6778.205").install()
    service = Service(driver_path)

    # Initialize WebDriver with the correct service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the base URL
    driver.get(base_url)

    # Attach the driver to the test class
    request.cls.driver = driver

    yield

    # Quit the driver after tests are done
    driver.quit()

