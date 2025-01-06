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
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
