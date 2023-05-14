from behave import *
import requests


@given(u"API duckduckgo")
def api_duckduckgo(context):
    context.uri = "https://api.duckduckgo.com/api/"
    print(context.uri)


@when(u"user search {city}")
def user_search(context, city):
    url = context.uri + "?q=" + city + "&format=json"
    context.result = requests.get(url)


@then(u"response code is {status_code}")
def response_code(context, status_code):
    assert str(context.result.status_code) == status_code, "Error the status code isn't correct"


@step(u"the source result {key} is {value}")
def the_source_result(context, key, value):
    response = context.result.json()
    if key not in response:
        raise Exception("Error the {} not exist ".format(key))
    assert (response[key] == value)


@step(u"create list with fields {abstract_url} and {first_url} in {related_topics}")
def create_list_with_fields(context, abstract_url, first_url, related_topics):
    response = context.result.json()
    if abstract_url not in response:
        raise Exception("Error the {} not exist".format(abstract_url))
    if related_topics not in response:
        raise Exception("Error the {} not exist".format(related_topics))
    related_topics_value = response[related_topics]
    first_value = related_topics_value[0]
    if first_url not in first_value:
        raise Exception("Error the {} not exist".format(first_url))
    result_list = [response[abstract_url], first_value[first_url]]
    assert (len(result_list) > 0)
