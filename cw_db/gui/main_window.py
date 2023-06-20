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

    notebook = ttk.Notebook(master=root)
    notebook.pack(expand=True, fill=tk.BOTH)

    # создаем пару фреймвов
    frame1 = ttk.Frame(master=notebook)
    frame2 = ttk.Frame(master=notebook)
    frame3 = ttk.Frame(master=notebook)
    frame4 = ttk.Frame(master=notebook)
    frame5 = ttk.Frame(master=notebook)
    frame6 = ttk.Frame(master=notebook)
    frame7 = ttk.Frame(master=notebook)

    # frame1.pack(fill=tk.BOTH, expand=True)
    frame2.pack(fill=tk.BOTH, expand=True)
    frame3.pack(fill=tk.BOTH, expand=True)
    frame4.pack(fill=tk.BOTH, expand=True)
    frame5.pack(fill=tk.BOTH, expand=True)
    frame6.pack(fill=tk.BOTH, expand=True)
    frame7.pack(fill=tk.BOTH, expand=True)

    # добавляем фреймы в качестве вкладок
    notebook.add(frame1, text="ADDRESS")
    notebook.add(frame2, text="COURIER")
    notebook.add(frame3, text="CUSTOMER")
    notebook.add(frame4, text="ITEM")
    notebook.add(frame5, text="ORDER")
    notebook.add(frame6, text="SCHEDULE")
    notebook.add(frame7, text="USER")

    # определяем данные для отображения

    # определяем столбцы
    frame1.rowconfigure(index=0, weight=1)
    frame1.columnconfigure(index=0, weight=1)

    
    columns = ("id", "name", "address", "customer_id")

    tree = ttk.Treeview(columns=columns, show="headings", master=frame1)
    # tree.pack(fill=tk.BOTH, expand=True)
   
    tree.grid(row=0, column=0, sticky="news")

    # определяем заголовки
    tree.heading("id", text="id", anchor=tk.W)
    tree.heading("name", text="name", anchor=tk.W)
    tree.heading("address", text="address", anchor=tk.W)
    tree.heading("customer_id", text="customer_id", anchor=tk.W)


    tree.column("#1", width=100)
    tree.column("#2", width=200)
    tree.column("#3", minwidth=400, width=600)
    tree.column("#4", width=100)

    address_to_append = controller.get_from_table(db_session, model.Address)

    address_list = list()
    # # добавляем данные
    for a in address_to_append:
        address_list.append((a.id, a.name, a.address, a.customer_id))
    for a in address_list:
        tree.insert("", tk.END, values=a)

    # scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
    # tree.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky="ns")
    
    scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview, master=frame1)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    # scroll= tk.Scrollbar(master=frame1, orient="vertical", command=tree.yview)
    # scroll.grid(row=0,column=1,sticky="ns")
    # tree['yscrollcommand'] = scroll.set
    root.mainloop()
    
