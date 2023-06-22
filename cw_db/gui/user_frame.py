import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller

import crud.read

def create_user_frame(db_session: orm.Session, notebook: ttk.Notebook):
    user_frame = ttk.Frame(master=notebook)
    notebook.add(user_frame, text="USER")

    user_frame.columnconfigure(index=0, weight=1)
    user_frame.rowconfigure(index=0, weight=1)

    user_columns = ("id", "login", "password", "access_level")

    global user_table
    user_table = ttk.Treeview(columns=user_columns,
                              show="headings", master=user_frame)

    user_table.grid(row=0, column=0, sticky=tk.NSEW)

    user_table.heading("id", text="ID", anchor=tk.W)
    user_table.heading("login", text="Логин", anchor=tk.W)
    user_table.heading("password", text="Пароль", anchor=tk.W)
    user_table.heading("access_level", text="Уровень доступа", anchor=tk.W)

    user_table.column("#1", width=50, minwidth=50)
    user_table.column("#2", width=100, minwidth=50)
    user_table.column("#3", width=200, minwidth=50)
    user_table.column("#4", width=100, minwidth=50)

    user_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=user_table.yview, master=user_frame)
    user_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    user_table.configure(yscrollcommand=user_table_scrollbar.set)

    read_user_table(db_session)


    user_table.bind("<<TreeviewSelect>>", lambda event: controller.get_selected_object_from_table(user_table))

def read_user_table(db_session):
    user_to_append = crud.read.get_all_records_from_table(db_session, model.User)


    for i in user_table.get_children():
        user_table.delete(i)

    user_list = list()
    for u in user_to_append:
        user_list.append((u.id, u.login, u.password, u.access_level))
    for u in user_list:
        user_table.insert("", tk.END, values=u)
