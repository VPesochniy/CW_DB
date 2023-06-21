import tkinter as tk
from tkinter import ttk
import model
import sqlalchemy.orm as orm
import controller


def create_schedule_frame(db_session: orm.Session, notebook: ttk.Notebook):
    schedule_frame = ttk.Frame(master=notebook)
    notebook.add(schedule_frame, text="SCHEDULE")

    schedule_frame.columnconfigure(index=0, weight=1)
    schedule_frame.rowconfigure(index=0, weight=1)

    schedule_columns = ("id", "date", "description", "start_of_shift", "end_of_shift",
                        "courier_id")

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

    schedule_to_append = controller.get_object_from_table(
        db_session, model.Schedule)

    schedule_list = list()
    for s in schedule_to_append:
        schedule_list.append((s.id, s.date, s.description,
                             s.start_of_shift, s.end_of_shift, s.courier_id))
    for s in schedule_list:
        schedule_table.insert("", tk.END, values=s)
