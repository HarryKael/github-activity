import requests

def get_activities(username:str) -> str:
    """Function which calls the api and return the result"""
    github_url = f'https://api.github.com/users/{username}/events'
    result = requests.get(github_url)
    if result.status_code == 200:
        return result.text
    else:
        raise Exception(result.text)