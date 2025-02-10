import smtplib
import random

def send_email():
    my_email = "juanclavel44@gmail.com"
    password = "yqcw zoiz rjrx xpsm"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        quote=random.choice(quotes)
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f"Subject: Hello22\n\n    {quote}"
        connection.sendmail(from_addr=my_email, to_addrs="juanitoclavel@gmail.com", msg=message)

with open("quotes.txt", "r") as file:
    quotes = file.readlines()
import datetime as dt

date = dt.datetime.now()
current_weekday = date.weekday()
print(current_weekday)
if current_weekday == 6:
    send_email()
    print("email sent")
else:
    print("no email sent")