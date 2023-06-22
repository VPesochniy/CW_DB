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

    address_table.column("#1", width=50, minwidth=50,)
    address_table.column("#2", width=100, minwidth=50,)
    address_table.column("#3", width=600, minwidth=50,)
    address_table.column("#4", width=50, minwidth=50,)

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

    #     def item_selected(event):
    #         selected_people = ""
    #         for selected_item in address_table.selection():
    #             item = address_table.item(selected_item)
    #             person = item["values"]
    #             selected_people = f"{selected_people}{person}\n"
    #         print(selected_people)
 
    # address_table.bind("<<TreeviewSelect>>", item_selected)

#     for col in address_columns:
#         address_table.heading(col, text=col, command=lambda _col=col: treeview_sort_column(
#             address_table, _col, False))


# def treeview_sort_column(table, column, order):
#     l = [(table.set(k, column), k) for k in table.get_children("")]
#     l.sort(order=order)

#     # rearrange items in sorted positions
#     for index, (val, k) in enumerate(l):
#         table.move(k, "", index)

#     # order sort next time
#     table.heading(column, command=lambda:
#                treeview_sort_column(table, column, not order))
