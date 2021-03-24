# coding=utf-8

import allure
from utils.api import *
import json


@allure.feature('Test API Anything')
@allure.story('1.Anything. POST /anything')
def test_anything_post(api_testing):
    endpoint = "https://{}/anything".format(api_testing.API_URL_PREFICS)
    with allure.step('Step 1. Correct post request'):
        data = json.dumps({"test": string})
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        assert string == response.json()["json"]["test"]
        print(response.json())
        print(response.elapsed.total_seconds())
