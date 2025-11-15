# First install: pip install Office365-REST-Python-Client
from office365.graph_client import GraphClient

def send_teams_office365():
    client = GraphClient(access_token="your_access_token")
    
    team = client.teams["your_team_id"]
    channel = team.channels["your_channel_id"]
    
    message = channel.messages.add(
        body="Hello from Office365 Python Client!"
    )
    client.execute_query()
    print("Message sent!")

send_teams_office365()