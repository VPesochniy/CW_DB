import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_courier_frame(db_session: orm.Session, notebook: ttk.Notebook):
    courier_frame = ttk.Frame(master=notebook)
    notebook.add(courier_frame, text="COURIER")

    courier_frame.columnconfigure(index=0, weight=1)
    courier_frame.rowconfigure(index=0, weight=1)

    courier_columns = ("id", "login", "password", "full_name", "status")

    courier_table = ttk.Treeview(
        columns=courier_columns, show="headings", master=courier_frame)

    courier_table.grid(row=0, column=0, sticky=tk.NSEW)

    courier_table.heading("id", text="ID", anchor=tk.W)
    courier_table.heading("login", text="Логин", anchor=tk.W)
    courier_table.heading("password", text="Пароль", anchor=tk.W)
    courier_table.heading("full_name", text="ФИО", anchor=tk.W)
    courier_table.heading("status", text="Статус", anchor=tk.W)

    courier_table.column("#1", width=50, minwidth=50)
    courier_table.column("#2", width=100, minwidth=50)
    courier_table.column("#3", width=200, minwidth=50)
    courier_table.column("#4", width=500, minwidth=50)
    courier_table.column("#5", width=100, minwidth=50)

    courier_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=courier_table.yview, master=courier_frame)
    courier_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    courier_table.configure(yscrollcommand=courier_table_scrollbar.set)

    courier_to_append = controller.get_object_from_table(
        db_session, model.Courier)

    courier_list = list()
    for c in courier_to_append:
        courier_list.append((c.id, c.login, c.password, c.full_name, c.status))
    for c in courier_list:
        courier_table.insert("", tk.END, values=c)
