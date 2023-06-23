import hashlib
import sqlalchemy.orm as orm
import tkinter as tk
from tkinter import ttk
import model

import crud.create
import gui.address_frame
import gui.courier_frame
import gui.customer_frame
import gui.item_frame
import gui.order_frame
import gui.schedule_frame
import gui.user_frame


def _send_user_data(db_session: orm.Session, choice: model.Base, dialog: tk.Tk, *args):
    crud.create.create_entry_in_table(db_session, choice, *args)
    dialog.destroy()
    match choice:
        case model.Address:
            gui.address_frame.read_address_table(db_session)
        case model.Courier:
            gui.courier_frame.read_courier_table(db_session)
        case model.Customer:
            gui.customer_frame.read_customer_table(db_session)
        case model.Item:
            gui.item_frame.read_item_table(db_session)
        case model.Order:
            gui.order_frame.read_order_table(db_session)
        case model.Schedule:
            gui.schedule_frame.read_schedule_table(db_session)
        case model.User:
            gui.user_frame.read_user_table(db_session)


def create_dialog(db_session: orm.Session, choice: model.Base):
    dialog = tk.Tk()
    dialog.geometry("500x600")
    dialog.resizable(False, False)
    frame_on_dialog = ttk.Frame(master=dialog)
    match choice:
        case model.Address:
            dialog.title("ADDRESS ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=150)

            input_name = tk.StringVar()
            input_address = tk.StringVar()
            input_customer_id = tk.IntVar()

            name_label = ttk.Label(master=frame_on_dialog, text="NAME")
            name_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_name)

            address_label = ttk.Label(master=frame_on_dialog, text="ADDRESS")
            address_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_address)

            customer_id_label = ttk.Label(
                master=frame_on_dialog, text="CUSTOMER")
            customer_id_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_customer_id)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, name_entry.get(), address_entry.get(), customer_id_entry.get()))

            name_label.pack(anchor=tk.W, expand=True, padx=5)
            name_entry.pack(anchor=tk.CENTER, expand=True,
                            fill=tk.X, ipady=4, pady=4)

            address_label.pack(anchor=tk.W, expand=True, padx=5)
            address_entry.pack(anchor=tk.CENTER, expand=True,
                               fill=tk.X, ipady=4, pady=4)

            customer_id_label.pack(anchor=tk.W, expand=True, padx=5)
            customer_id_entry.pack(anchor=tk.CENTER, expand=True,
                                   fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.Courier:
            dialog.title("COURIER ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=100)

            input_login = tk.StringVar()
            input_password = tk.StringVar()
            input_full_name = tk.StringVar()
            input_status = tk.StringVar()

            login_label = ttk.Label(master=frame_on_dialog, text="LOGIN")
            login_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_login)

            password_label = ttk.Label(master=frame_on_dialog, text="PASSWORD")
            password_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_password, show="*")

            full_name_label = ttk.Label(
                master=frame_on_dialog, text="FULL NAME")
            full_name_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_full_name)

            status_label = ttk.Label(master=frame_on_dialog, text="STATUS")
            status_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_status)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, login_entry.get(), (hashlib.sha256(password_entry.get().encode("UTF-8")).hexdigest()), full_name_entry.get(), status_entry.get()))

            login_label.pack(anchor=tk.W, expand=True, padx=5)
            login_entry.pack(anchor=tk.CENTER, expand=True,
                             fill=tk.X, ipady=4, pady=4)

            password_label.pack(anchor=tk.W, expand=True, padx=5)
            password_entry.pack(anchor=tk.CENTER, expand=True,
                                fill=tk.X, ipady=4, pady=4)

            full_name_label.pack(anchor=tk.W, expand=True, padx=5)
            full_name_entry.pack(anchor=tk.CENTER, expand=True,
                                 fill=tk.X, ipady=4, pady=4)

            status_label.pack(anchor=tk.W, expand=True, padx=5)
            status_entry.pack(anchor=tk.CENTER, expand=True,
                              fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.Customer:
            dialog.title("CUSTOMER ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=200)

            input_full_name = tk.StringVar()
            input_phone_number = tk.StringVar()

            full_name_label = ttk.Label(
                master=frame_on_dialog, text="FULL NAME")
            full_name_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_full_name)

            phone_number_label = ttk.Label(
                master=frame_on_dialog, text="PHONE NUMBER")
            phone_number_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_phone_number)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, full_name_entry.get(), phone_number_entry.get()))

            full_name_label.pack(anchor=tk.W, expand=True, padx=5)
            full_name_entry.pack(anchor=tk.CENTER, expand=True,
                                 fill=tk.X, ipady=4, pady=4)

            phone_number_label.pack(anchor=tk.W, expand=True, padx=5)
            phone_number_entry.pack(anchor=tk.CENTER, expand=True,
                                    fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.Item:
            dialog.title("ITEM ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=100)

            input_item = tk.StringVar()
            input_price = tk.DoubleVar()
            input_quantity = tk.IntVar()
            input_description = tk.StringVar()

            item_label = ttk.Label(master=frame_on_dialog, text="ITEM")
            item_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_item)

            price_label = ttk.Label(master=frame_on_dialog, text="PRICE")
            price_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_price)

            quantity_label = ttk.Label(master=frame_on_dialog, text="QUANTITY")
            quantity_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_quantity)

            description_label = ttk.Label(
                master=frame_on_dialog, text="DESCRIPTION")
            description_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_description)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, item_entry.get(), price_entry.get(), quantity_entry.get(), description_entry.get()))

            item_label.pack(anchor=tk.W, expand=True, padx=5)
            item_entry.pack(anchor=tk.CENTER, expand=True,
                            fill=tk.X, ipady=4, pady=4)

            price_label.pack(anchor=tk.W, expand=True, padx=5)
            price_entry.pack(anchor=tk.CENTER, expand=True,
                             fill=tk.X, ipady=4, pady=4)

            quantity_label.pack(anchor=tk.W, expand=True, padx=5)
            quantity_entry.pack(anchor=tk.CENTER, expand=True,
                                fill=tk.X, ipady=4, pady=4)

            description_label.pack(anchor=tk.W, expand=True, padx=5)
            description_entry.pack(anchor=tk.CENTER, expand=True,
                                   fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.Order:
            dialog.title("ORDER ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=50)

            input_items_quantity = tk.IntVar()
            input_discount = tk.DoubleVar()
            input_cost = tk.DoubleVar()
            input_status = tk.StringVar()
            input_courier_id = tk.IntVar()
            input_customer_id = tk.IntVar()

            items_quantity_label = ttk.Label(
                master=frame_on_dialog, text="ITEMS QUANTITY")
            items_quantity_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_items_quantity)

            discount_label = ttk.Label(master=frame_on_dialog, text="DISCOUNT")
            discount_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_discount)

            cost_label = ttk.Label(master=frame_on_dialog, text="COST")
            cost_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_cost)

            status_label = ttk.Label(master=frame_on_dialog, text="STATUS")
            status_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_status)

            courier_id_label = ttk.Label(
                master=frame_on_dialog, text="COURIER ID")
            courier_id_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_courier_id)

            customer_id_label = ttk.Label(
                master=frame_on_dialog, text="CUSTOMER ID")
            customer_id_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_customer_id)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, items_quantity_entry.get(), discount_entry.get(), cost_entry.get(), status_entry.get(), courier_id_entry.get(), customer_id_entry.get()))

            items_quantity_label.pack(anchor=tk.W, expand=True, padx=5)
            items_quantity_entry.pack(anchor=tk.CENTER, expand=True,
                                      fill=tk.X, ipady=4, pady=4)

            discount_label.pack(anchor=tk.W, expand=True, padx=5)
            discount_entry.pack(anchor=tk.CENTER, expand=True,
                                fill=tk.X, ipady=4, pady=4)

            cost_label.pack(anchor=tk.W, expand=True, padx=5)
            cost_entry.pack(anchor=tk.CENTER, expand=True,
                            fill=tk.X, ipady=4, pady=4)

            status_label.pack(anchor=tk.W, expand=True, padx=5)
            status_entry.pack(anchor=tk.CENTER, expand=True,
                              fill=tk.X, ipady=4, pady=4)

            courier_id_label.pack(anchor=tk.W, expand=True, padx=5)
            courier_id_entry.pack(anchor=tk.CENTER, expand=True,
                                  fill=tk.X, ipady=4, pady=4)

            customer_id_label.pack(anchor=tk.W, expand=True, padx=5)
            customer_id_entry.pack(anchor=tk.CENTER, expand=True,
                                   fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.Schedule:
            dialog.title("SCHEDULE ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=200)

            input_description = tk.StringVar()
            input_courier_id = tk.IntVar()

            description_label = ttk.Label(
                master=frame_on_dialog, text="DESCRIPTION")
            description_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_description)

            courier_id_label = ttk.Label(
                master=frame_on_dialog, text="COURIER ID")
            courier_id_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_courier_id)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, description_entry.get(), courier_id_entry.get()))

            description_label.pack(anchor=tk.W, expand=True, padx=5)
            description_entry.pack(anchor=tk.CENTER, expand=True,
                                   fill=tk.X, ipady=4, pady=4)

            courier_id_label.pack(anchor=tk.W, expand=True, padx=5)
            courier_id_entry.pack(anchor=tk.CENTER, expand=True,
                                  fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)
        case model.User:
            dialog.title("USER ENTITY")
            frame_on_dialog.pack(expand=True, fill=tk.BOTH, padx=100, pady=150)

            input_login = tk.StringVar()
            input_password = tk.StringVar()
            input_access_level = tk.StringVar()

            login_label = ttk.Label(master=frame_on_dialog, text="LOGIN")
            login_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_login)

            password_label = ttk.Label(master=frame_on_dialog, text="PASSWORD")
            password_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_password, show="*")

            access_level_label = ttk.Label(
                master=frame_on_dialog, text="ACCESS LEVEL")
            access_level_entry = ttk.Entry(
                master=frame_on_dialog, textvariable=input_access_level)

            confirm_button = ttk.Button(
                master=frame_on_dialog, text="CREATE", command=lambda: _send_user_data(db_session, choice, dialog, login_entry.get(), (hashlib.sha256(password_entry.get().encode("UTF-8")).hexdigest()), access_level_entry.get()))

            login_label.pack(anchor=tk.W, expand=True, padx=5)
            login_entry.pack(anchor=tk.CENTER, expand=True,
                             fill=tk.X, ipady=4, pady=4)

            password_label.pack(anchor=tk.W, expand=True, padx=5)
            password_entry.pack(anchor=tk.CENTER, expand=True,
                                fill=tk.X, ipady=4, pady=4)

            access_level_label.pack(anchor=tk.W, expand=True, padx=5)
            access_level_entry.pack(anchor=tk.CENTER, expand=True,
                                    fill=tk.X, ipady=4, pady=4)

            confirm_button.pack(anchor=tk.CENTER, expand=True,
                                ipadx=24, ipady=8, pady=4)

    dialog.mainloop()
