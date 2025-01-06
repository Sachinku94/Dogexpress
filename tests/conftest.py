from Config.config_reader import read_config
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    base_url = read_config("URL", "base_url")
    driver = webdriver.Chrome()
    driver.get(base_url)
    # Add other setup steps here...
    request.cls.driver = driver
    yield
    driver.quit()
