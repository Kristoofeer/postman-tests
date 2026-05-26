import requests
import allure

BASE_GET_URL = "https://postman-echo.com/get"
BASE_POST_URL = "https://postman-echo.com/post"


@allure.feature("GET Requests")
@allure.story("Basic GET")
@allure.title("Простой GET-запрос — проверка поля url")
@allure.description("Тест проверяет, что GET-запрос к /get возвращает статус 200 и правильное поле url в ответе.")
def test_get_url_field():
    with allure.step("Отправить GET-запрос"):
        response = requests.get(BASE_GET_URL)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить поле url в JSON-ответе"):
        response_json = response.json()
        assert response_json["url"] == BASE_GET_URL


@allure.feature("GET Requests")
@allure.story("GET with params")
@allure.title("GET-запрос с параметрами — проверка поля args")
@allure.description("Тест проверяет, что переданные query-параметры возвращаются в поле args ответа.")
def test_get_query_params():
    params = {"foo": "bar1"}

    with allure.step("Отправить GET-запрос с параметром foo=bar1"):
        response = requests.get(BASE_GET_URL, params=params)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что параметры вернулись в поле args"):
        response_json = response.json()
        assert response_json["args"] == params


@allure.feature("POST Requests")
@allure.story("POST with JSON")
@allure.title("POST-запрос с JSON-телом — проверка поля json")
@allure.description("Тест проверяет, что отправленный JSON возвращается в поле json ответа.")
def test_post_json_data():
    payload = {"name": "Alex", "skill": "tester"}

    with allure.step("Отправить POST-запрос с JSON-данными"):
        response = requests.post(BASE_POST_URL, json=payload)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что отправленный JSON вернулся в поле json"):
        response_json = response.json()
        assert response_json["json"] == payload


@allure.feature("POST Requests")
@allure.story("POST data field")
@allure.title("POST-запрос — проверка поля data")
@allure.description("Тест проверяет, что отправленные данные возвращаются в поле data ответа.")
def test_post_data_is_string():
    payload = {"name": "Kris", "skill": "engineer"}

    with allure.step("Отправить POST-запрос с данными"):
        response = requests.post(BASE_POST_URL, json=payload)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что данные вернулись в поле data"):
        response_json = response.json()
        assert response_json["data"] == payload


@allure.feature("Headers")
@allure.story("Content-Type check")
@allure.title("Проверка заголовка Content-Type в ответе")
@allure.description("Тест проверяет, что успешный ответ содержит заголовок Content-Type со значением application/json.")
def test_content_type_header():
    with allure.step("Отправить GET-запрос"):
        response = requests.get(BASE_GET_URL)

    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверить заголовок Content-Type"):
        content_type = response.headers.get("Content-Type")
        assert content_type is not None
        assert "application/json" in content_type