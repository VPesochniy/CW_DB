import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_item_frame(db_session: orm.Session, notebook: ttk.Notebook):
    item_frame = ttk.Frame(master=notebook)
    notebook.add(item_frame, text="ITEM")

    item_frame.columnconfigure(index=0, weight=1)
    item_frame.rowconfigure(index=0, weight=1)

    item_columns = ("id", "name", "price", "quantity", "description")

    item_table = ttk.Treeview(columns=item_columns,
                              show="headings", master=item_frame)

    item_table.grid(row=0, column=0, sticky=tk.NSEW)

    item_table.heading("id", text="ID", anchor=tk.W)
    item_table.heading("name", text="Наименование", anchor=tk.W)
    item_table.heading("price", text="Цена", anchor=tk.W)
    item_table.heading("quantity", text="Количество", anchor=tk.W)
    item_table.heading("description", text="Описание", anchor=tk.W)

    item_table.column("#1", width=50, minwidth=50)
    item_table.column("#2", width=200, minwidth=50)
    item_table.column("#3", width=50, minwidth=50)
    item_table.column("#4", width=50, minwidth=50)
    item_table.column("#5", width=100, minwidth=50)

    item_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=item_table.yview, master=item_frame)
    item_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    item_table.configure(yscrollcommand=item_table_scrollbar.set)

    item_to_append = controller.get_object_from_table(db_session, model.Item)

    item_list = list()
    for i in item_to_append:
        item_list.append((i.id, i.name, i.price, i.quantity, i.description if i.description != None else ""))
    for i in item_list:
        item_table.insert("", tk.END, values=i)