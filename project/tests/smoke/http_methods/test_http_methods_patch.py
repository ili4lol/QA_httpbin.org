# coding=utf-8

import allure
from utils.api import *
import json


@allure.feature('Test API http methods')
@allure.story('1.Patch. PATCH /patch')
def test_http_methods_patch(api_testing):
    endpoint = "https://{}/patch".format(api_testing.API_URL_PREFICS)
    with allure.step('Step 1. Correct patch request'):
        data = json.dumps({"test": string})
        response = send_patch_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        assert string == response.json()["json"]["test"]
        print(response.json())
        print(response.elapsed.total_seconds())
