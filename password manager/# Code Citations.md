# Code Citations

## License: unknown
https://github.com/r-anandu-s/password_manager/tree/c2f29736acd0af5e849f5d5d1a056531424dacc4/main.py

```
.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message=
```


## License: unknown
https://github.com/golddust588/myPassGeneratorApp/tree/9df5e0bbf0c407e488ac25fe42c48dadd208324b/main.py

```
website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message
```


## License: unknown
https://github.com/dezlin77/20150701/tree/97bd01be5f87751daec4881084dad524d7ef214c/py2021/passwordManager/main.py

```
# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
```


## License: unknown
https://github.com/Kokkie999/Private/tree/1c982cfddc31b4bef1ffde01ddfbc48c9124ded0/PycharmProjects/pythonProject/100_days_of_code/day%2030%20improved%20password%20manager/main.py

```
)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image
```


## License: unknown
https://github.com/Bass-Ninja/Password-Manager/tree/44d0af46cbd2beb049488c0e3704ef56837aa7c8/main.py

```
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png"
```

## License: unknown
https://github.com/your-repo/your-project/main.py

```
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
def save():
    print("saving...")
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill all fields")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            print(f"Website: {website}, Email: {email}, Password: {password}")
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            password_entry.insert(0, "")
            messagebox.showinfo(title="Success", message="Password saved successfully")
        else:
            messagebox.showinfo(title="Error", message="Password not saved")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
```

