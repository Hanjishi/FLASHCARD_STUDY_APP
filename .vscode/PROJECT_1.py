import tkinter as tk
from tkinter import font as tkFont
import sqlite3

root = tk.Tk()
root.title("Facebook Login")
root.geometry("900x400")
root.configure(bg="#F5F6F7")

facebook_font = tkFont.Font(family="Arial", size=36, weight="bold")
label_font = tkFont.Font(family="Arial", size=16)
entry_font = tkFont.Font(family="Arial", size=14)
button_font = tkFont.Font(family="Arial", size=14, weight="bold")

def Database():
    global conn, cursor
    conn = sqlite3.connect("fb.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def AddUser(username, password):
    cursor.execute("INSERT INTO `member` (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

Database()
AddUser("Hel", "Helqt")
AddUser("Dals", "Janjan")
AddUser("Peps", "Macadaya")
AddUser("Chin", "abcdef")
AddUser("Aloe", "Vera")
AddUser("Cy", "Press")
AddUser("Sirsia", "Shasha")

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()

def HomeWindow():
    global Home
    root.withdraw()
    Home = tk.Toplevel()
    Home.title("Facebook Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    lbl_home = tk.Label(Home, text="Successfully Logged In!", font=('times new roman', 20)).pack()
    btn_back = tk.Button(Home, text='Back', command=Back).pack(pady=20, fill=tk.X)

def Back():
    Home.destroy()
    root.deiconify()

def on_password_click(event):
    password_entry.config(show="*")
    if password_entry.get() == "Password":
        password_entry.delete(0, tk.END)
        password_entry.config(fg="black")

def on_email_click(event):
    email_entry.config(show="")
    if email_entry.get() == "Email or phone number":
        email_entry.delete(0, tk.END)
        email_entry.config(fg="black")

USERNAME = tk.StringVar()
PASSWORD = tk.StringVar()

facebook_label = tk.Label(root, text="facebook", font=facebook_font, fg="#1877F2", bg="#F5F6F7")
facebook_label.place(x=50, y=50)

recent_logins_label = tk.Label(root, text="Recent Logins", font=label_font, bg="#F5F6F7")
recent_logins_label.place(x=50, y=120)

instruction_label = tk.Label(root, text="Click your name or add an account.", font=entry_font, fg="#606770", bg="#F5F6F7")
instruction_label.place(x=50, y=150)

user_frame = tk.Frame(root, width=100, height=100, bg="#F5F6F7", bd=1, relief="solid")
user_frame.place(x=50, y=180)
user_label = tk.Label(user_frame, text="Group 3", font=entry_font, bg="#F5F6F7")
user_label.pack(side="bottom", pady=5)

add_account_frame = tk.Frame(root, width=100, height=100, bg="#F5F6F7", bd=1, relief="solid")
add_account_frame.place(x=200, y=180)
add_account_label = tk.Label(add_account_frame, text="Add Account", font=entry_font, fg="#1877F2", bg="#F5F6F7")
add_account_label.pack(side="bottom", pady=5)

email_entry = tk.Entry(root, textvariable=USERNAME, font=entry_font, width=30, bd=1, relief="solid")
email_entry.place(x=500, y=150)
email_entry.insert(0, "Email or phone number")
email_entry.bind("<FocusIn>", on_email_click)

password_entry = tk.Entry(root, textvariable=PASSWORD, font=entry_font, width=30, bd=1, relief="solid")
password_entry.place(x=500, y=200)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", on_password_click)

login_button = tk.Button(root, text="Log In", font=button_font, bg="#1877F2", fg="white", width=20, command=Login)
login_button.place(x=540, y=250)
login_button.bind('<Return>', Login)

forgot_password_label = tk.Label(root, text="  Forgot password?", font=entry_font, fg="#1877F2", bg="#F5F6F7")
forgot_password_label.place(x=580, y=290)

create_account_button = tk.Button(root, text="Create new account", font=button_font, bg="#42B72A", fg="white", width=20)
create_account_button.place(x=540, y=320)

lbl_text = tk.Label(root, font=entry_font, bg="#F5F6F7")
lbl_text.place(x=500, y=370)

root.mainloop()