

import smtplib
from email.mime.text import MIMEText

# Your email credentials
sender_email = "ravipractice10@gmail.com"
app_password = "Pass@2327" 
receiver_email = "ravikasabe1010@gmail.com"

# Creating the message
message = MIMEText("This is a test email sent using Python.")
message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email

try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e}")
finally:
    server.quit()
