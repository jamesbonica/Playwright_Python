import pytest_check as check
from playwright.sync_api._generated import Playwright

api_key = 'reqres-free-v1'

def test_api_get(playwright: Playwright):
    request = playwright.request.new_context(
        extra_http_headers={'X-Api-Key':api_key,
                            'Accept': 'application/json'}
    )


    response = request.get('https://reqres.in/api/users?page=2')

    assert response.status == 200

    json_data = response.json()

    print(json_data)

    assert json_data['data'][3]['last_name'] == 'Fields'

    request.dispose()

def test_api_post(playwright: Playwright):
    request = playwright.request.new_context(
        extra_http_headers={'X-Api-Key':api_key,
                            'Accept': 'application/json'}
                            )
    data = {
    "name": "joeyv",
    "job": "malingerer"
}
    response = request.post('https://reqres.in/api/users', data=data)

    assert response.status == 201

    json_data = response.json()

    # experimentation with soft assertion plug-in
    check.is_true(json_data['name'] == 'joeyv', 'You got the wrong name, bucko!')

    assert json_data['id'] is not None