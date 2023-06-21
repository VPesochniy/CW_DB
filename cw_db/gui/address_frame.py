import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_address_frame(db_session: orm.Session, notebook: ttk.Notebook):
    address_frame = ttk.Frame(master=notebook)
    notebook.add(address_frame, text="ADDRESS")
    
    address_frame.columnconfigure(index=0, weight=1)
    address_frame.rowconfigure(index=0, weight=1)

    address_columns = ("id", "name", "address", "customer_id")

    address_table = ttk.Treeview(
        columns=address_columns, show="headings", master=address_frame)

    address_table.grid(row=0, column=0, sticky=tk.NSEW)

    address_table.heading("id", text="ID", anchor=tk.W)
    address_table.heading("name", text="Наименование", anchor=tk.W)
    address_table.heading("address", text="Адрес", anchor=tk.W)
    address_table.heading("customer_id", text="ID клиента", anchor=tk.W)

    address_table.column("#1", width=50, minwidth=50)
    address_table.column("#2", width=100, minwidth=50)
    address_table.column("#3", width=600, minwidth=50)
    address_table.column("#4", width=50, minwidth=50)

    address_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=address_table.yview, master=address_frame)
    address_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    address_table.configure(yscrollcommand=address_table_scrollbar.set)

    address_to_append = controller.get_object_from_table(
        db_session, model.Address)

    address_list = list()
    for a in address_to_append:
        address_list.append((a.id, a.name, a.address, a.customer_id))
    for a in address_list:
        address_table.insert("", tk.END, values=a)
