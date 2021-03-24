# coding=utf-8

import allure
from utils.api import *


@allure.feature('Test API Anything')
@allure.story('1.Anything. GET /anything')
def test_anything_get(api_testing):
    endpoint = "https://{}/anything".format(api_testing.API_URL_PREFICS)
    with allure.step('Step 1. Correct get request'):
        response = send_get_request_to_api(endpoint, api_testing.API_TOKEN)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        print(response.json())
        print(response.elapsed.total_seconds())
