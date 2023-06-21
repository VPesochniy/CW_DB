import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_customer_frame(db_session: orm.Session, notebook: ttk.Notebook):
    customer_frame = ttk.Frame(master=notebook)
    notebook.add(customer_frame, text="CUSTOMER")

    customer_frame.columnconfigure(index=0, weight=1)
    customer_frame.rowconfigure(index=0, weight=1)

    customer_columns = ("id", "full_name", "phone_number")

    customer_table = ttk.Treeview(
        columns=customer_columns, show="headings", master=customer_frame)

    customer_table.grid(row=0, column=0, sticky=tk.NSEW)

    customer_table.heading("id", text="ID", anchor=tk.W)
    customer_table.heading("full_name", text="ФИО", anchor=tk.W)
    customer_table.heading("phone_number", text="Номер телефона", anchor=tk.W)

    customer_table.column("#1", width=50, minwidth=50)
    customer_table.column("#2", width=500, minwidth=50)
    customer_table.column("#3", width=200, minwidth=50)

    customer_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=customer_table.yview, master=customer_frame)
    customer_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    customer_table.configure(yscrollcommand=customer_table_scrollbar.set)

    customer_to_append = controller.get_object_from_table(
        db_session, model.Customer)

    customer_list = list()
    for c in customer_to_append:
        customer_list.append((c.id, c.full_name, c.phone_number))
    for c in customer_list:
        customer_table.insert("", tk.END, values=c)
