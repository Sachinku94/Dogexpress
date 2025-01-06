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
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(base_url)
#     request.cls.driver = driver
#     yield
#     driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Config.config_reader import read_config
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # Read the base URL from the configuration file
    base_url = read_config("URL", "base_url")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for CI environments
    chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
    chrome_options.add_argument("--no-sandbox")  # Prevent sandbox issues in CI/CD pipelines
    chrome_options.add_argument("--disable-dev-shm-usage")  # Resolve shared memory issues

    # Use WebDriverManager with Service and Chrome Options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the base URL
    driver.get(base_url)

    # Attach the driver to the test class
    request.cls.driver = driver

    yield

    # Quit the browser
    driver.quit()
