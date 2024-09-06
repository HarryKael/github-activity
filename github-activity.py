#! /usr/local/bin/python3
import sys
from src.http_api_request import get_activities
from src.process_json import get_data_as_list

def main():
    arguments = sys.argv
    # ? Know if the user introduced the username
    if len(arguments) == 2:
        username = arguments[1]
        # ! Calling the api
        result = get_activities(username)
        # ! Formating the result
        listed = get_data_as_list(result)
        # ! Printing the results
        for l in listed:
            print(f'{l['type']} to {l['repo']['name']}')

if __name__ == '__main__':
    main()