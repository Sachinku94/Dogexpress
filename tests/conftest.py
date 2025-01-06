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


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
from Config.config_reader import read_config

@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    base_url = read_config("URL", "base_url")
    
    # URL of the Selenium Grid Hub
    selenium_grid_url = "http://localhost:4444/wd/hub"  # Change this if using a remote Selenium Grid
    
    # Set up desired capabilities for Edge or Chrome
    # For Edge (change to DesiredCapabilities.CHROME for Chrome)
    capabilities = DesiredCapabilities.EDGE.copy()
    capabilities['platform'] = "LINUX"  # Or you can set your desired platform (e.g., Windows)

    # Set up the WebDriver to connect to the remote Selenium Grid
    driver = webdriver.Remote(
        command_executor=selenium_grid_url,  # Grid URL
        desired_capabilities=capabilities     # Desired capabilities (Edge or Chrome)
    )

    # Navigate to the base URL
    driver.get(base_url)

    # Attach driver to the test class
    request.cls.driver = driver
    
    # Yield to run tests
    yield
    
    # Quit the driver after tests complete
    driver.quit()






