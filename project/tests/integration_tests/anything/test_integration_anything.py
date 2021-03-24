# coding=utf-8

import allure
from utils.api import *
import json
new_name_field = "testing_rename"


@allure.feature('Test API anything integration')
@allure.story('1.Test anything integration /anything')
def test_integration_anything(api_testing):
    endpoint = "https://{}/anything/".format(api_testing.API_URL_PREFICS)

    with allure.step('Step 1. Correct post request'):
        data = json.dumps({"test": string})
        response = send_post_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        data = response.json()
        assert string == data["json"]["test"]
        # здесь можно было бы сделать получение id, если возможно, например так
        # global id_anything
        # id_anything = data["id"]
        print(response.json())
        print(response.elapsed.total_seconds())

    with allure.step('Step 2. Correct get request'):
        endpoint = "https://{}/anything/{}".format(api_testing.API_URL_PREFICS, id_anything)
        response = send_get_request_to_api(endpoint, api_testing.API_TOKEN)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        # и проверить, что объект создался
        # assert data["id"] == id_anything
        print(response.json())
        print(response.elapsed.total_seconds())

    with allure.step('Step 3. Correct patch request'):
        data = json.dumps({"test": new_name_field})
        endpoint = "https://{}/anything/{}".format(api_testing.API_URL_PREFICS, id_anything)
        response = send_patch_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        # assert data["id"] == id_anything
        assert new_name_field == response.json()["json"]["test"]
        print(response.json())
        print(response.elapsed.total_seconds())

    with allure.step('Step 4. Correct put request'):
        endpoint = "https://{}/anything/{}".format(api_testing.API_URL_PREFICS, id_anything)
        data = json.dumps({"test": string})
        response = send_put_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        # assert data["id"] == id_anything
        assert string == response.json()["json"]["test"]
        print(response.json())
        print(response.elapsed.total_seconds())

    with allure.step('Step 5. Correct delete request'):
        endpoint = "https://{}/anything/{}".format(api_testing.API_URL_PREFICS, id_anything)
        data = json.dumps({"test": string})
        response = send_delete_request_to_api(endpoint, api_testing.API_TOKEN, data)
        assert (response.status_code == 200), create_error_message(response, endpoint)
        print(response.json())
        print(response.elapsed.total_seconds())

    with allure.step('Step 6. Correct get request not found id'):
        endpoint = "https://{}/anything/{}".format(api_testing.API_URL_PREFICS, id_anything)
        response = send_get_request_to_api(endpoint, api_testing.API_TOKEN)
        # 404 проверяем что объект удалился
        assert (response.status_code == 404), create_error_message(response, endpoint)
        print(response.json())
        print(response.elapsed.total_seconds())
