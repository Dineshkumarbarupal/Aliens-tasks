# First install: pip install pymsteams
import pymsteams

def send_teams_pymsteams():
    webhook_url = "your_teams_webhook_url"
    
    teams_message = pymsteams.ConnectorCard(webhook_url)
    teams_message.title("Python Notification")
    teams_message.text("This message is sent using pymsteams library")
    
    # Add button/link
    teams_message.addLinkButton("Visit Python", "https://python.org")
    
    teams_message.send()
    print("Message sent using pymsteams!")

send_teams_pymsteams()