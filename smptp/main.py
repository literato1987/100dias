import datetime
import pandas as pd

# Get today's date
today = (datetime.datetime.now().month, datetime.datetime.now().day)
print(today)

# Load CSV file
df_birthdays = pd.read_csv("C:\Users\juani\OneDrive\Escritorio\Python\smptp\birthdays.csv")

# Ensure column names are clean
df_birthdays.columns = df_birthdays.columns.str.strip()

# Convert 'month' and 'day' columns to integers
df_birthdays['month'] = df_birthdays['month'].astype(int)
df_birthdays['day'] = df_birthdays['day'].astype(int)

# Create dictionary
birthdays_dict = {(row['month'], row['day']): row.to_dict() for (index, row) in df_birthdays.iterrows()}

print(birthdays_dict)

# Check if today is in the dictionary
if today in birthdays_dict:
    print("Yes, it's someone's birthday!")
    print(birthdays_dict[today])




#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:


# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



