import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeDriverManager
import pytest
from Config.config_reader import read_config


@pytest.fixture(scope="class")
def setup(request):
    base_url = read_config("URL", "base_url")

    # Use WebDriverManager to automatically handle the Edge driver download and installation
    driver = webdriver.Edge(EdgeDriverManager().install())
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
