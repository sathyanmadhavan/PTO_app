import requests
import json
import jsonpath

BASIC_URL = "http://127.0.0.1:6464/"


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

def test_check_page_title():
    url = BASIC_URL
    response = requests.get(url)
    if response.status_code != 204 and response.headers["Content-Type"].startswith("application/json"):
        json_data = response.json()
        assert "title" in json_data
        assert json_data["title"] == "Practice testing AI/ML based applications"

def test_check_page_body():
    url = BASIC_URL
    response = requests.get(url)
    if response.status_code != 204 and response.headers["Content-Type"].startswith("application/json"):
        json_data = response.json()
        assert "body" in json_data
        assert json_data["body"] == "We would love to hear from you!"

def test_check_page_date():
    url = BASIC_URL
    response = requests.get(url)
    if response.status_code != 204 and response.headers["Content-Type"].startswith("application/json"):
        json_data = response.json()
        assert "date" in json_data
        assert json_data["date"] == "2020-08-13"

def test_check_page_tags():
    url = BASIC_URL
    response = requests.get(url)
    if response.status_code != 204 and response.headers["Content-Type"].startswith("application/json"):
        json_data = response.json()
        assert "tags" in json_data
        assert json_data["tags"] == ["testing", "ai", "ml"]



test_get_status_code_equals_200()
test_check_content_type_headers()
test_check_page_title()
test_check_page_body()
