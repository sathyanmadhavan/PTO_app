import requests

BASIC_URL = "http://127.0.0.1:6464/"

class PTO_app():
    def test_get_status_code_equals_200():
        url = BASIC_URL
        response = requests.get(url)
        assert response.status_code == 200, print("Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))


    def test_failed_get_status_code_equals_201():   
        url = BASIC_URL
        response = requests.get(url)
        assert response.status_code == 201, print("Got wrong status code, expected is: {}, actual is {}".format("201", response.status_code))


    def test_check_content_type_headers():
        url = BASIC_URL
        response = requests.get(url)
        assert response.headers["Content-Type"] == "text/html; charset=utf-8",print(
        "Got wrong content type in headers, expected is: {}, actual is {}".format("application/json; charset=utf-8",
                                                                                  response.headers["Content-Type"]))
    

app=PTO_app()
PTO_app.test_check_content_type_headers()
PTO_app.test_failed_get_status_code_equals_201()
PTO_app.test_get_status_code_equals_200()