import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
def save():
    print("saving...")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill all fields")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                # Load existing data
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                # If file doesn't exist, initialize data as empty dictionary
                data = {}

            # Update data and save back to file
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            # Clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title="Success", message="Password saved successfully")

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas for Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")  # Replace with your logo file path
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 20))  # Added space below the logo

# Labels
website_label = Label(text="Website:", anchor="w")
website_label.grid(row=1, column=0, sticky="E", padx=5, pady=5)

email_label = Label(text="Email/Username:", anchor="w")
email_label.grid(row=2, column=0, sticky="E", padx=5, pady=5)

password_label = Label(text="Password:", anchor="w")
password_label.grid(row=3, column=0, sticky="E", padx=5, pady=5)

# Entries
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="W")
email_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="W")

# Buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2, padx=5, pady=5,sticky="W")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5, sticky="W")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
