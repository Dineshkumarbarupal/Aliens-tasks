# First install: pip install emails
import emails

def send_email_emails():
    message = emails.html(
        html="<h1>Test Email</h1><p>This is a test email</p>",
        subject="Test Email",
        mail_from="your_email@gmail.com"
    )
    
    response = message.send(
        to="receiver@gmail.com",
        smtp={
            "host": "smtp.gmail.com",
            "port": 587,
            "timeout": 5,
            "user": "your_email@gmail.com",
            "password": "your_app_password",
            "tls": True
        }
    )
    
    if response.status_code == 250:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email: {response}")

send_email_emails()