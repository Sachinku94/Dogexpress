import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from Config.config_reader import read_config

@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    base_url = read_config("URL", "base_url")
    
    # URL of the Selenium Grid Hub (change the URL if it's hosted on a different machine or port)
    selenium_grid_url = "http://localhost:4444/wd/hub"  # Change this if using a remote Selenium Grid
    
    # Set up Edge options (you can replace this with ChromeOptions if using Chrome)
    edge_options = Options()
    edge_options.add_argument("--headless")  # Optional: Run headlessly for CI environments
    edge_options.add_argument("--disable-gpu")  # Optional: Disable GPU rendering
    edge_options.add_argument("--no-sandbox")  # Optional: Prevent sandboxing issues
    edge_options.add_argument("--disable-dev-shm-usage")  # Optional: Resolve shared memory issues
    
    # Connect to the Selenium Grid using the Remote WebDriver
    driver = webdriver.Remote(
        command_executor=selenium_grid_url,  # Grid URL
        options=edge_options  # Pass the browser options
    )
    
    driver.get(base_url)
    
    # Attach driver to the test class
    request.cls.driver = driver
    
    # Yield to run tests
    yield
    
    # Quit the driver after tests complete
    driver.quit()
