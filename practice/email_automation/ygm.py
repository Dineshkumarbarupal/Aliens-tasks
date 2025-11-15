# First install: pip install yagmail
import yagmail

def send_email_yagmail():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "your_app_password"
    
    yag = yagmail.SMTP(sender_email, password)
    
    subject = "Test Email"
    body = "This is a test email sent using yagmail."
    
    yag.send(
        to=receiver_email,
        subject=subject,
        contents=body
    )
    print("Email sent successfully!")

send_email_yagmail()