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
    assert (str(context.result.status_code) == status_code)


@step(u"the source result {key} is {value}")
def the_source_result(context, key, value):
    response = context.result.json()
    assert (key in response)
    assert (response[key] == value)


@step(u"create list with fields {abstract_url} and {first_url} in {related_topics}")
def create_list_with_fields(context, abstract_url, first_url, related_topics):
    response = context.result.json()
    assert (abstract_url in response)
    assert (related_topics in response)
    related_topics_value = response[related_topics]
    first_value = related_topics_value[0]
    assert (first_url in first_value)
    result_list = [response[abstract_url], first_value[first_url]]
    assert (len(result_list) > 0)
