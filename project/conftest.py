# coding=utf-8

import platform
import pytest

os_system = platform.system()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption("--contur", action="store", default="test",
                     help="name of test contur: test, preprod")


@pytest.fixture
def contur(request):
    return request.config.getoption("--contur")


@pytest.fixture()
def api_testing(request):
    contur = request.config.getoption("--contur")
    api_testing.API_URL_PREFICS = "httpbin.org"
    api_testing.API_TOKEN = ""
    if contur == "test":
        api_testing.API_URL_PREFICS = "httpbin.org"
        api_testing.API_TOKEN = ""
    elif contur == "preprod":
        api_testing.API_URL_PREFICS = ""
        api_testing.API_TOKEN = ""
    else:
        print("Неизвестный контур, используется контур по умолчанию")
    yield api_testing



