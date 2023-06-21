import tkinter as tk
from tkinter import ttk
import controller
import sqlalchemy.orm as orm
import model
import gui.address_frame
import gui.courier_frame
import gui.customer_frame
import gui.item_frame
import gui.order_frame
import gui.schedule_frame
import gui.user_frame


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

    gui.address_frame.create_address_frame(db_session, notebook)
    gui.courier_frame.create_courier_frame(db_session, notebook)
    gui.customer_frame.create_customer_frame(db_session, notebook)
    gui.item_frame.create_item_frame(db_session, notebook)
    gui.order_frame.create_order_frame(db_session, notebook)
    gui.schedule_frame.create_schedule_frame(db_session, notebook)
    gui.user_frame.create_user_frame(db_session, notebook)

    root.mainloop()
