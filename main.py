import os
from dotenv import load_dotenv
import requests 

load_dotenv() # using .env file for github token 

webdevInviteDetails = {
    "GITHUB_API": "https://api.github.com",
    "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
    "ORG_NAME": "Electrium-Mobility",
    "TEAM_ID": "webdev"  
}


def invite_users_to_team(details, usernames, role="member"):
    url = f"{details['GITHUB_API']}/orgs/{details['ORG_NAME']}/teams/{details['TEAM_ID']}/memberships/"
    body = {"role": role}
    headers = {
        "Authorization": f"Bearer {details['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json"
    }
    for user in usernames: 
        response = requests.put(url + user, headers=headers, json=body)
        if (response.status_code == 200 or response.status_code == 201):
            print (f"{user} added as {role} to team")
            print (response.json())
        else: 
            print (f"Error adding { user } to the team. Response status code: {response.status_code}")
            if (response.status_code == 403): 
                    return # rate limiting error, preventing further requests

def main():
    usernamesList = [] # add usernames to this list 
    invite_users_to_team(webdevInviteDetails, usernamesList)

if (__name__ == "__main__"):
    main()


