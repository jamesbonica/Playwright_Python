from playwright.sync_api._generated import Playwright

def test_api_get(playwright: Playwright):
    request = playwright.request.new_context(
        extra_http_headers={'X-Api-Key':'reqres-free-v123',
                            'Accept': 'application/json'}
    )
    response = request.get('https://reqres.in/api/users?page=2')

    assert response.status == 200

    json_data = response.json()

    print(json_data)

    assert json_data['data'][3]['last_name'] == 'Fields'

    request.dispose()