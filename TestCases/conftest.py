from selenium import webdriver
import pytest
import time

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver


##################### pytest html report
def pytest_configure(config):
    config._metadata['Poject Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Ankit'

@pytest.mark.optionalhook
def config_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_collection(session):
#     collect_timeout = 5
#     collect_begin_time = time.time()
#     yield
#     collect_end_time = time.time()
#     c_time = collect_end_time - collect_begin_time
#     if c_time > collect_timeout:
#         raise Exception('Collection timeout.')