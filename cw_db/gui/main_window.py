import tkinter as tk
from tkinter import ttk
import controller
import sqlalchemy.orm as orm
import model


def run_app(db_session: orm.Session):
    global root
    root = tk.Tk()
    root.title("Panel")
    root.geometry("1200x800")
    root.resizable(False, False)

    root.columnconfigure(index=0, weight=1)
    root.rowconfigure(index=0, weight=1)

    notebook_frame = ttk.Frame(master=root)
    bottom_frame = ttk.Frame(master=root)

    notebook_frame.grid(row=0, column=0, sticky=tk.NSEW)
    bottom_frame.grid(row=1, column=0, sticky=tk.EW)

    create_button = ttk.Button(master=bottom_frame, text="СОЗДАТЬ")
    delete_button = ttk.Button(master=bottom_frame, text="УДАЛИТЬ")
    update_button = ttk.Button(master=bottom_frame, text="ОБНОВИТЬ")
    export_button = ttk.Button(master=bottom_frame, text="ВЫГРУЗИТЬ ТАБЛИЦУ")

    create_button.pack(side=tk.LEFT, padx=4, ipadx=4)
    delete_button.pack(side=tk.LEFT, padx=4, ipadx=4)
    update_button.pack(side=tk.LEFT, padx=4, ipadx=4)
    export_button.pack(side=tk.RIGHT, padx=4, ipadx=4)

    notebook = ttk.Notebook(master=notebook_frame)
    notebook.pack(expand=True, fill=tk.BOTH)

    address_frame = ttk.Frame(master=notebook)
    courier_frame = ttk.Frame(master=notebook)
    customer_frame = ttk.Frame(master=notebook)
    item_frame = ttk.Frame(master=notebook)
    order_frame = ttk.Frame(master=notebook)
    schedule_frame = ttk.Frame(master=notebook)
    user_frame = ttk.Frame(master=notebook)

    address_frame.columnconfigure(index=0, weight=1)
    address_frame.rowconfigure(index=0, weight=1)

    courier_frame.columnconfigure(index=0, weight=1)
    courier_frame.rowconfigure(index=0, weight=1)

    customer_frame.columnconfigure(index=0, weight=1)
    customer_frame.rowconfigure(index=0, weight=1)

    item_frame.columnconfigure(index=0, weight=1)
    item_frame.rowconfigure(index=0, weight=1)

    order_frame.columnconfigure(index=0, weight=1)
    order_frame.rowconfigure(index=0, weight=1)

    schedule_frame.columnconfigure(index=0, weight=1)
    schedule_frame.rowconfigure(index=0, weight=1)

    user_frame.columnconfigure(index=0, weight=1)
    user_frame.rowconfigure(index=0, weight=1)

    notebook.add(address_frame, text="ADDRESS")
    notebook.add(courier_frame, text="COURIER")
    notebook.add(customer_frame, text="CUSTOMER")
    notebook.add(item_frame, text="ITEM")
    notebook.add(order_frame, text="ORDER")
    notebook.add(schedule_frame, text="SCHEDULE")
    notebook.add(user_frame, text="USER")

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

    order_columns = ("id", "date_of_creation", "date_of_completion", "cost",
                     "status", "discount", "courier_id", "customer_id", "items_quantity")

    order_table = ttk.Treeview(
        columns=order_columns, show="headings", master=order_frame)

    order_table.grid(row=0, column=0, sticky=tk.NSEW)

    order_table.heading("id", text="ID заказа", anchor=tk.W)
    order_table.heading(
        "items_quantity", text="Количество товаров", anchor=tk.W)
    order_table.heading("discount", text="Скидка", anchor=tk.W)
    order_table.heading("cost", text="Цена", anchor=tk.W)
    order_table.heading("status", text="Статус", anchor=tk.W)
    order_table.heading("date_of_creation", text="Дата создания", anchor=tk.W)
    order_table.heading("date_of_completion",
                        text="Дата завершения", anchor=tk.W)
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

    schedule_columns = ("id", "start_of_shift", "end_of_shift",
                        "date", "description", "courier_id")

    schedule_table = ttk.Treeview(
        columns=schedule_columns, show="headings", master=schedule_frame)

    schedule_table.grid(row=0, column=0, sticky=tk.NSEW)

    schedule_table.heading("id", text="ID", anchor=tk.W)
    schedule_table.heading("date", text="Дата", anchor=tk.W)
    schedule_table.heading("description", text="Описание", anchor=tk.W)
    schedule_table.heading(
        "start_of_shift", text="Открытие смены", anchor=tk.W)
    schedule_table.heading("end_of_shift", text="Закрытие смены", anchor=tk.W)
    schedule_table.heading("courier_id", text="ID курьера", anchor=tk.W)

    schedule_table.column("#1", width=50, minwidth=50)
    schedule_table.column("#2", width=100, minwidth=50)
    schedule_table.column("#3", width=200, minwidth=50)
    schedule_table.column("#4", width=100, minwidth=50)
    schedule_table.column("#5", width=100, minwidth=50)
    schedule_table.column("#6", width=50, minwidth=50)

    schedule_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=schedule_table.yview, master=schedule_frame)
    schedule_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    schedule_table.configure(yscrollcommand=schedule_table_scrollbar.set)

    user_columns = ("id", "login", "password", "access_level")

    user_table = ttk.Treeview(columns=user_columns,
                              show="headings", master=user_frame)

    user_table.grid(row=0, column=0, sticky=tk.NSEW)

    user_table.heading("id", text="ID", anchor=tk.W)
    user_table.heading("login", text="Наименование", anchor=tk.W)
    user_table.heading("password", text="Адрес", anchor=tk.W)
    user_table.heading("access_level", text="ID клиента", anchor=tk.W)

    user_table.column("#1", width=50, minwidth=50)
    user_table.column("#2", width=100, minwidth=50)
    user_table.column("#3", width=200, minwidth=50)
    user_table.column("#4", width=100, minwidth=50)

    user_table_scrollbar = ttk.Scrollbar(
        orient=tk.VERTICAL, command=user_table.yview, master=user_frame)
    user_table_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    user_table.configure(yscrollcommand=user_table_scrollbar.set)

    root.mainloop()
