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
#     driver = webdriver.Chrome(ChromeDriverManager(driver_version="131.0.6778.204").install())
#     driver.get(base_url)
#     request.cls.driver = driver
#     yield
#     driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # URL of the Selenium Grid Hub (use the address where Selenium Grid is running)
    selenium_grid_url = "http://localhost:4444/wd/hub"  # Change this to your Hub's URL if needed

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for CI environments
    chrome_options.add_argument("--no-sandbox")  # Avoid sandbox issues
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues in Docker
    
    # Set up WebDriver for Selenium Grid (using remote WebDriver)
    driver = webdriver.Remote(
        command_executor=selenium_grid_url,
        desired_capabilities=DesiredCapabilities.CHROME,
        options=chrome_options
    )

    # Access driver in tests via request.cls
    request.cls.driver = driver
    
    yield
    
    driver.quit()




