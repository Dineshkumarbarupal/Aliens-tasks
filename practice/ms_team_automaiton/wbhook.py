import requests
import json

def send_teams_webhook():
    webhook_url = "your_teams_webhook_url"
    
    message = {
        "text": "Hello from Python! This message is sent via webhook.",
        "title": "Python Notification"
    }
    
    response = requests.post(
        webhook_url,
        json=message,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 200:
        print("Message sent via webhook!")
    else:
        print(f"Error: {response.status_code}")

send_teams_webhook()