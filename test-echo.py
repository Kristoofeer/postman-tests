import requests

BASE_GET_URL = "https://postman-echo.com/get"
BASE_POST_URL = "https://postman-echo.com/post"

def test_get_url_field():
    # Тест 1: Простой GET-запрос. Проверяем, что поле 'url' в ответе совпадает с запрошенным URL.
    response = requests.get(BASE_GET_URL)
    assert response.status_code == 200 
    response_json = response.json()
    assert response_json["url"] == BASE_GET_URL


def test_get_query_params():
    # Тест 2: GET-запрос с параметром запроса. Проверяем, что параметр пришёл в ответе.
    params = {"one": "val1"}
    response = requests.get(BASE_GET_URL, params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["args"] == params

def test_post_json_data():
    # Тест 3: POST-запрос с JSON-телом. Проверяем, что отправленный JSON вернулся в поле 'json'.
    payload = {"name": "Kris", "skill": "engineer"}
    response = requests.post(BASE_POST_URL, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["json"] == payload

def test_post_data_is_string():
    # Тест 4: POST-запрос с телом. Проверяем, что в поле 'data' наши данные лежат как строка.
    payload = {"name": "Kris", "skill": "engineer"}
    response = requests.post(BASE_POST_URL, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    import json
    assert response_json["data"] == payload

def test_content_type_header():
    # Тест 5: Проверяем, что в ответе на GET-запрос есть правильный заголовок Content-Type.
    response = requests.get(BASE_GET_URL)
    assert response.status_code == 200
    content_type = response.headers.get("Content-Type")
    assert content_type is not None
    assert "application/json" in content_type