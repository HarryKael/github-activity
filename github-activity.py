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
        last_event = None
        last_repo = None
        amount = 0
        # ! Going through the list
        for l in listed:
            # ! Getting the event and the repo
            event_type = l['type']
            repo = l['repo']['name']
            # ? Knowing if the event_type has changed or if the repo_name has changed too
            if last_event == None or (last_event == event_type and (last_repo == None or last_repo == repo)):
                amount = amount + 1
            else:
                # ! Printing the event and the amount of it
                print(f'{last_event} - {amount} to {last_repo}')
                amount = 1
            # ! Saving the last events and repo's names
            last_event = event_type
            last_repo = repo
        # ! Printing the last one
        print(f'{last_event} - {amount} to {last_repo}')

if __name__ == '__main__':
    main()