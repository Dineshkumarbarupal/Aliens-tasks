# Install: pip install pywhatkit
import pywhatkit

def send_whatsapp_pywhatkit():
    phone_number = "+91637781395"  # with country code
    message = "Hello from pywhatkit! This is an automated message."
    hour = 15  # 24-hour format
    minute = 30
    
    # Send instantly (requires web.whatsapp.com open in browser)
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    
    # Or schedule for specific time
    # pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    
    print("Message sent!")

send_whatsapp_pywhatkit()