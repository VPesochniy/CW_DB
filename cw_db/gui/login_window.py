import tkinter as tk
from tkinter import ttk
import controller
import sqlalchemy.orm as orm


def _send_user_data(db_session: orm.Session, input_login: tk.StringVar, input_password: tk.StringVar):
    controller.verify_user(
        db_session, input_login.get(), input_password.get())


def run_app(db_session: orm.Session):

    global root
    root = tk.Tk()
    root.title("БД ПР5")
    root.geometry("500x600")
    root.resizable(False, False)

    frame = ttk.Frame()
    frame.pack(expand=True, fill=tk.BOTH, padx=100, pady=200)

    input_login = tk.StringVar()
    input_password = tk.StringVar()
    username_label = ttk.Label(master=frame, text="USERNAME")
    login_entry = ttk.Entry(master=frame, textvariable=input_login)
    password_label = ttk.Label(master=frame, text="PASSWORD")
    password_entry = ttk.Entry(
        master=frame, textvariable=input_password, show="*")
    confirm_button = ttk.Button(
        master=frame, text="LOGIN", command=lambda: _send_user_data(db_session, input_login, input_password))

    username_label.pack(anchor=tk.W, expand=True, padx=5)
    login_entry.pack(anchor=tk.CENTER, expand=True, fill=tk.X, ipady=4, pady=4)
    password_label.pack(anchor=tk.W, expand=True, padx=5)
    password_entry.pack(anchor=tk.CENTER, expand=True,
                        fill=tk.X, ipady=4, pady=4)
    confirm_button.pack(anchor=tk.CENTER, expand=True,
                        ipadx=24, ipady=8, pady=4)

    root.mainloop()
