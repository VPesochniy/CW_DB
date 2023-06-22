import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
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

def _get_opened_note(db_session: orm.Session, notebook: ttk.Notebook):
    match notebook.index(notebook.select()):
        case 0:
            controller.export_table_in_csv(db_session, model.Address)
        case 1:
            controller.export_table_in_csv(db_session, model.Courier)
        case 2:
            controller.export_table_in_csv(db_session, model.Customer)
        case 3:
            controller.export_table_in_csv(db_session, model.Item)
        case 4:
            controller.export_table_in_csv(db_session, model.Order)
        case 5:
            controller.export_table_in_csv(db_session, model.Schedule)
        case 6:
            controller.export_table_in_csv(db_session, model.User)


def run_app(db_session: orm.Session):
    global root
    root = tk.Tk()
    root.title("Panel")
    root.geometry("1200x800")
    root.resizable(False, False)

    notebook_frame = ttk.Frame(master=root)
    bottom_frame = ttk.Frame(master=root)

    notebook_frame.pack(expand=True, fill=tk.BOTH)
    bottom_frame.pack(fill=tk.X)

    create_button = ttk.Button(master=bottom_frame, text="СОЗДАТЬ")
    delete_button = ttk.Button(master=bottom_frame, text="УДАЛИТЬ")
    update_button = ttk.Button(master=bottom_frame, text="ИЗМЕНИТЬ")
    export_button = ttk.Button(master=bottom_frame, text="ВЫГРУЗИТЬ ТАБЛИЦУ", command=lambda: _get_opened_note(db_session, notebook))

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
