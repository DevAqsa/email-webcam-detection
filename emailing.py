import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "lyuu ovlb vzyz dops"
SENDER_EMAIL = "aqsafreelancedeveloper@gmail.com"
RECEIVER_EMAIL = "aqsafreelancedeveloper@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "a new customer showed up"
    email_message.set_content("hey we just sarw a email customer")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content,maintype="image", subtype=imghdr.what(None, content))


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER_EMAIL, PASSWORD)
    gmail.sendmail(SENDER_EMAIL ,RECEIVER_EMAIL. email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")

