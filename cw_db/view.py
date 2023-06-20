import tkinter as tk
from tkinter import ttk
import controller
import sqlalchemy.orm as orm


def run_app(db_session: orm.Session):

    def send_user_data():
        controller.verify_user(db_session, input_login.get(), input_password.get())


    root = tk.Tk()
    root.title("БД ПР5")
    root.geometry("500x600")
    # icon = tk.PhotoImage("database.png")
    # root.iconphoto(True, icon)
    root.resizable(False, False)

    for c in range(1):
        root.columnconfigure(index=c, weight=1)
    for r in range(3):
        root.rowconfigure(index=r, weight=1)

    frame_list = list()

    for r in range(3):
        for c in range(1):
            frame = ttk.Frame(padding=40)
            frame.grid(row=r, column=c, sticky=tk.NSEW)
            frame_list.append(frame)

    input_login = tk.StringVar()
    input_password = tk.StringVar()
    login_label = ttk.Label(master=frame_list[1], text="Login")
    login_entry = ttk.Entry(master=frame_list[1], textvariable=input_login)
    password_label = ttk.Label(master=frame_list[1], text="Password")
    password_entry = ttk.Entry(
        master=frame_list[1], textvariable=input_password)
    confirm_button = ttk.Button(
        master=frame_list[1], text="Sign in", command=send_user_data)

    login_label.pack(anchor=tk.CENTER, expand=True)
    login_entry.pack(anchor=tk.CENTER, expand=True, fill=tk.X, ipady=5)
    password_label.pack(anchor=tk.CENTER, expand=True)
    password_entry.pack(anchor=tk.CENTER, expand=True, fill=tk.X, ipady=5)
    confirm_button.pack(anchor=tk.CENTER, expand=True, ipadx=50, ipady=20)

    root.mainloop()

