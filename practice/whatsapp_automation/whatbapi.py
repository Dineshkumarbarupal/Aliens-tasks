import requests
import json

def send_whatsapp_api():
    # WhatsApp Business API credentials
    phone_number_id = "your_phone_number_id"
    access_token = "your_access_token"
    to_number = "recipient_phone_number"  # with country code
    
    url = f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "text": {"body": "Hello from Python! This is an automated WhatsApp message."}
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("WhatsApp message sent successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

send_whatsapp_api()