# coding=utf-8

import allure
from utils.api import *


@allure.feature('Test API http methods')
@allure.story('1.Get. GET /get')
def test_http_methods_get(api_testing):
    endpoint = "https://{}/get".format(api_testing.API_URL_PREFICS)
    with allure.step('Step 1. Correct get request'):
        response = send_get_request_to_api(endpoint, api_testing.API_TOKEN)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        print(response.json())
        print(response.elapsed.total_seconds())
