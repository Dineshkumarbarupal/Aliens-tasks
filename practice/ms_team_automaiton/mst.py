# Microsoft Graph api (Official Method)

import requests
import json

def send_teams_message():
    access_token = "your_access_token"
    team_id = "your_team_id"
    channel_id = "your_channel_id"
    
    url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    message_body = {
        "body": {
            "content": "Hello from Python! This is a test message to Teams."
        }
    }
    
    response = requests.post(url, headers=headers, json=message_body)
    
    if response.status_code == 201:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

send_teams_message()