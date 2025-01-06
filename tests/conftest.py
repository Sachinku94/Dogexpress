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




from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Config.config_reader import read_config


@pytest.fixture(scope="class")
def setup(request):
    base_url = read_config("URL", "base_url")

    # Use WebDriverManager to automatically handle the Edge driver download and installation
    driver = webdriver.Chrome(ChromeDriverManager(driver_version="131.0.6778.204").install())
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()


# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import pytest
# from Config.config_reader import read_config

# @pytest.fixture(scope="class")
# def setup(request):
#     # Read base URL from config
#     base_url = read_config("URL", "base_url")

#     # Set up Edge options
#     edge_options = Options()
#     edge_options.add_argument("--headless")  # Run headlessly for CI environments
#     edge_options.add_argument("--disable-gpu")  # Disable GPU rendering
#     edge_options.add_argument("--no-sandbox")  # Prevent sandboxing issues
#     edge_options.add_argument("--disable-dev-shm-usage")  # Resolve shared memory issues

#     # Use WebDriverManager to install the correct version of EdgeDriver
#     driver_path = EdgeChromiumDriverManager().install()
#     service = Service(driver_path)

#     # Start Edge WebDriver
#     driver = webdriver.Edge(service=service, options=edge_options)
#     driver.get(base_url)

#     # Attach driver to the test class
#     request.cls.driver = driver
#     yield
#     driver.quit()



