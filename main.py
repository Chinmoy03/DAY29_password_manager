from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    letter_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2,4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    website = web_entry.get()
    w = len(website)
    email = email_entry.get()
    password = pass_entry.get()
    p = len(password)

    if w != 0 and p != 0:
        save_flag = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                  f"\nPassword: {password} \nIs it ok to save?")
        if save_flag:
            with open("data.txt", "a") as fin:
                info = f"{website} | {email} | {password}\n"
                fin.writelines(info)
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showerror(title="Empty Field(s)", message="One or more fields are empty. Please make sure all "
                                                             "fields are filled.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(pady=50, padx=50)
# window.minsize(500, 500)
window.title("Password Manager")

# Create the canvas and logo and put it in the window
pic = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
logo = canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

# To create an entry field for Website:
website_label = Label(text="Website: ", font=("Arial", 10))
website_label.grid(row=1, column=0)
web_entry = Entry(width=45)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")

# To create email entry field
email_label = Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(row=2, column=0)
email_entry = Entry(width=45)
email_entry.insert(END, "csahoo@ualberta.ca")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

# To create the password entry field
pass_label = Label(text="Password: ", font=("Arial", 10))
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=31)
pass_entry.grid(row=3, column=1, sticky="w")
generate_pass_button = Button(text="Generate Password", font=("Arial", 8), borderwidth=0, command=password_generator)
generate_pass_button.grid(row=3, column=2, )

# To create the add button
add_button = Button(text="Add", width=36, font=("Arial", 8), borderwidth=0, command=add_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
