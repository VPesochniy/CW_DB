from random import randint
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

import crud.delete
import crud.read


def _get_opened_note_to_export(db_session: orm.Session, notebook: ttk.Notebook):
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


def _get_opened_note_to_create(db_session: orm.Session, notebook: ttk.Notebook):
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


def _get_opened_note_to_update(db_session: orm.Session, notebook: ttk.Notebook):
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


def _get_opened_note_to_delete(db_session: orm.Session, notebook: ttk.Notebook):
    match notebook.index(notebook.select()):
        case 0:
            selected_address_id = controller.get_selected_object_from_table(
                gui.address_frame.address_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Address, selected_address_id)
            gui.address_frame.read_address_table(db_session)

        case 1:
            selected_courier_id = controller.get_selected_object_from_table(
                gui.courier_frame.courier_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Courier, selected_courier_id)
            gui.courier_frame.read_courier_table(db_session)
        case 2:
            selected_customer_id = controller.get_selected_object_from_table(
                gui.customer_frame.customer_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Customer, selected_customer_id)
            gui.customer_frame.read_customer_table(db_session)
        case 3:
            selected_item_id = controller.get_selected_object_from_table(
                gui.item_frame.item_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Item, selected_item_id)
            gui.item_frame.read_item_table(db_session)
        case 4:
            selected_order_id = controller.get_selected_object_from_table(
                gui.order_frame.order_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Order, selected_order_id)
            gui.order_frame.read_order_table(db_session)
        case 5:
            selected_schedule_id = controller.get_selected_object_from_table(
                gui.schedule_frame.schedule_table)
            crud.delete.delete_entry_from_table(
                db_session, model.Schedule, selected_schedule_id)
            gui.schedule_frame.read_schedule_table(db_session)
        case 6:
            selected_user_id = controller.get_selected_object_from_table(
                gui.user_frame.user_table)
            crud.delete.delete_entry_from_table(
                db_session, model.User, selected_user_id)
            gui.user_frame.read_user_table(db_session)


def run_app(db_session: orm.Session):

    global root
    root = tk.Tk()
    root.title("БД КП")
    root.geometry("1200x800")
    root.resizable(False, False)

    notebook_frame = ttk.Frame(master=root)
    bottom_frame = ttk.Frame(master=root)

    notebook_frame.pack(expand=True, fill=tk.BOTH)
    bottom_frame.pack(fill=tk.X)

    create_button = ttk.Button(master=bottom_frame, text="СОЗДАТЬ",
                               command=lambda: _get_opened_note_to_create(db_session, notebook))
    delete_button = ttk.Button(master=bottom_frame, text="УДАЛИТЬ",
                               command=lambda: _get_opened_note_to_delete(db_session, notebook))
    update_button = ttk.Button(master=bottom_frame, text="ИЗМЕНИТЬ",
                               command=lambda: _get_opened_note_to_update(db_session, notebook))
    export_button = ttk.Button(master=bottom_frame, text="ВЫГРУЗИТЬ ТАБЛИЦУ",
                               command=lambda: _get_opened_note_to_export(db_session, notebook))

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
