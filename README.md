# invite-to-github
running this script adds the usernames in a list to a specified electrium team

# setup 
- confirm that you have python
- here are the dependencies needed to run the script:
```
  python-dotenv==1.0.1
  Requests==2.32.3
```

- to access the Github API, you need to create and set up a .env file with the API token. Place the .env file in the repo folder.
```
  GITHUB_TOKEN=XXXXENTERTOKENHEREXXXXX
```

# running the script
1. fill the list in the main method with the usernames of the people you want to add to the team
2. run the python script 
