import requests
import json

def get_data_as_list(data):
    result = json.loads(data)
    return result

def get_activities(username:str) -> list[dict]:
    """Function which calls the api and return the result"""
    github_url = f'https://api.github.com/users/{username}/events'
    result = requests.get(github_url)
    if result.status_code == 200:
        return get_data_as_list(result.text)
    else:
        data = get_data_as_list(result.text)
        raise Exception(f'\nError: {data['message']}.\nStatus\' Code: {data['status']}.\nDocumentation URL: {data['documentation_url']}')