import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_order_frame(db_session: orm.Session, notebook: ttk.Notebook):
    order_frame = ttk.Frame(master=notebook)
    notebook.add(order_frame, text="ORDER")

    order_frame.columnconfigure(index=0, weight=1)
    order_frame.rowconfigure(index=0, weight=1)

    order_columns = ("id", "items_quantity", "discount", "cost", "status",
                     "date_of_creation", "date_of_completion", "courier_id", "customer_id")

    order_table = ttk.Treeview(
        columns=order_columns, show="headings", master=order_frame)

    order_table.grid(row=0, column=0, sticky=tk.NSEW)

    order_table.heading("id", text="ID заказа", anchor=tk.W)
    order_table.heading(
        "items_quantity", text="Количество", anchor=tk.W)
    order_table.heading("discount", text="Скидка", anchor=tk.W)
    order_table.heading("cost", text="Цена", anchor=tk.W)
    order_table.heading("status", text="Статус", anchor=tk.W)
    order_table.heading("date_of_creation",
                        text="Дата и время создания", anchor=tk.W)
    order_table.heading("date_of_completion",
                        text="Дата и время завершения", anchor=tk.W)
    order_table.heading("courier_id", text="ID курьера", anchor=tk.W)
    order_table.heading("customer_id", text="ID клиента", anchor=tk.W)

    order_table.column("#1", width=50, minwidth=50)
    order_table.column("#2", width=50, minwidth=50)
    order_table.column("#3", width=50, minwidth=50)
    order_table.column("#4", width=100, minwidth=50)
    order_table.column("#5", width=100, minwidth=50)
    order_table.column("#6", width=200, minwidth=50)
    order_table.column("#7", width=200, minwidth=50)
    order_table.column("#8", width=50, minwidth=50)
    order_table.column("#9", width=50, minwidth=50)

    order_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=order_table.yview, master=order_frame)
    order_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    order_table.configure(yscrollcommand=order_table_scrollbar.set)

    order_to_append = controller.get_object_from_table(db_session, model.Order)

    order_list = list()
    for o in order_to_append:
        order_list.append((o.id, o.items_quantity, o.discount if o.discount != None else "", o.cost, o.status,
                          o.date_of_creation, o.date_of_completion if o.date_of_completion != None else "", o.courier_id, o.customer_id))
    for o in order_list:
        order_table.insert("", tk.END, values=o)
