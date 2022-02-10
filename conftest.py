import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import pytest
from selenium import webdriver
from selenium.webdriver import Remote


def pytest_addoption(parser):
    """ Parse pytest --option variables from shell """
    parser.addoption('--browser',
                     help='Which test browser?',
                     default='chrome')


@pytest.fixture(scope='session')
def test_browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def remote_browser(test_browser) -> Remote:
    """ Select configuration depends on browser """
    if test_browser == 'firefox':
        driver = webdriver.Remote(
            options=webdriver.FirefoxOptions(),
            command_executor='http://selenium__standalone-firefox:4444/wd/hub'
        )
        return driver

    elif test_browser == 'chrome':
        driver = webdriver.Remote(
            options=webdriver.ChromeOptions(),
            command_executor='http://selenium__standalone-chrome:4444/wd/hub'
        )
        return driver

    else:
        raise ValueError(f'--browser={test_browser} is not chrome or firefox')