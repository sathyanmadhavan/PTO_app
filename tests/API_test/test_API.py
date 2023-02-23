import requests
import json
import jsonpath

BASIC_URL = "https://practice-testing-ai-ml.qxf2.com/is-pto"


def test_get_status_code_equals_200():
    url = BASIC_URL
    response = requests.get(url)
    assert response.status_code == 200 
    print(response)

def test_check_content_type_headers():
    url = BASIC_URL
    response = requests.get(url)
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    print(response.headers)



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
test_response()