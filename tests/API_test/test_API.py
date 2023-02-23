import requests
import json
import jsonpath

BASIC_URL = "https://practice-testing-ai-ml.qxf2.com/is-pto"


def test_get_status_code_equals_200():
    url = BASIC_URL
    response = requests.get(url)
    output = response.text
    print(output)


def test_check_content_type_headers():
    url = BASIC_URL
    response = requests.get(url)
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    print(response.headers)

def test_check_page_title():
    url = BASIC_URL
    response = requests.get(url)
    if response.status_code != 204 and response.headers["Content-Type"].startswith("text/html"):
        f = open('data.json')
        json_data = json.load(f)
        print(json_data)
        assert "title" in json_data
        if json_data["title"] == "Practice testing AI/ML based applications":
            print("Passed")
        else:
            print("Fail")

def test_response():
    url = BASIC_URL
    data = {'message': 'I am Sick out today!'}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        output = response.text
        print(output)
    else:
        print('Error: ', response.status_code)

test_get_status_code_equals_200()
test_check_content_type_headers()
test_check_page_title()
test_response()

