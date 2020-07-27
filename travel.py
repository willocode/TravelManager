from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import storage


class Travel:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Management System")
        self.root.geometry("1350x700+0+0")

        # ------variables
        self.priority = StringVar()
        self.name = StringVar()
        self.country = StringVar()
        self.climate = StringVar()
        self.travel_mode = StringVar()
        self.stay = StringVar()

        self.search_drop = StringVar()
        self.search_text = StringVar()

        title = Label(self.root, text="Travel Manager", bd=5, font=("times new roman", 40, "italic"), bg="light yellow")
        title.pack(side=TOP, fill=X)

        Form_Box = Frame(self.root, bd=4, relief=RIDGE, bg="light yellow")
        Form_Box.place(x=20, y=100, width=450, height=700)
        f_title = Label(Form_Box, text="Add Destination", font=("times new roman", 30, "italic"), bg="light yellow")
        f_title.grid(row=0, columnspan=2, pady=20)

        dest_priority = Label(Form_Box, text="Priority:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_priority.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_priority = Entry(Form_Box, textvariable=self.priority, font=("times new roman", 19, "italic"), bd=5,
                             relief=GROOVE)
        txt_priority.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        dest_title = Label(Form_Box, text="Name:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_title.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_title = Entry(Form_Box, textvariable=self.name, font=("times new roman", 19, "italic"), bd=5, relief=GROOVE)
        txt_title.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        dest_country = Label(Form_Box, text="Country:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_country.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_country = Entry(Form_Box, textvariable=self.country, font=("times new roman", 19, "italic"), bd=5,
                            relief=GROOVE)
        txt_country.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        dest_climate = Label(Form_Box, text="Climate:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_climate.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        txt_climate = Entry(Form_Box, textvariable=self.climate, font=("times new roman", 19, "italic"), bd=5,
                            relief=GROOVE)
        txt_climate.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        dest_activity = Label(Form_Box, text="Activities:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_activity.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        self.txt_activity = Text(Form_Box, width=20, height=4, font=("times new roman", 19, "italic"), bd=5,
                                 relief=GROOVE)
        self.txt_activity.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        dest_travel = Label(Form_Box, text="Trvl Mode:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_travel.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        drop_travel = ttk.Combobox(Form_Box, textvariable=self.travel_mode, font=("times new roman", 19, "italic"))
        drop_travel["values"] = ("Plane", "Car", "Boat", "Train")
        drop_travel.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        dest_stay = Label(Form_Box, text="Stay:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_stay.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        drop_stay = ttk.Combobox(Form_Box, textvariable=self.stay, font=("times new roman", 19, "italic"))
        drop_stay["values"] = ("1 week", "10 days", "2 weeks", "3 weeks+")
        drop_stay.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        # -------------------Buttons

        Button_Box = Frame(Form_Box, bg="light yellow")
        Button_Box.place(x=10, y=600, width=430)

        btn_add = Button(Button_Box, text="Add", height=2, width=10, command=self.add_travels).grid(row=0, column=0,
                                                                                                    padx=5, pady=20)
        btn_update = Button(Button_Box, text="Update", height=2, width=10, command=self.update_data).grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=5,
                                                                                                          pady=20)
        btn_delete = Button(Button_Box, text="Delete", height=2, width=10, command=self.delete_data).grid(row=0,
                                                                                                          column=2,
                                                                                                          padx=5,
                                                                                                          pady=20)
        btn_clear = Button(Button_Box, text="Clear", height=2, width=10, command=self.clear_it).grid(row=0, column=3,
                                                                                                     padx=5, pady=20)

        # -------------------Display box
        Display_Box = Frame(self.root, bd=4, relief=RIDGE, bg="light yellow")
        Display_Box.place(x=500, y=100, width=900, height=700)

        dest_search = Label(Display_Box, text="Search By:", font=("times new roman", 30, "italic"), bg="light yellow")
        dest_search.grid(row=0, column=0, pady=15, padx=10, sticky="w")

        drop_search = ttk.Combobox(Display_Box, textvariable=self.search_drop, font=("times new roman", 19, "italic"))
        drop_search["values"] = ("Priority", "Name", "Country", "Climate", "Activity", "Stay")
        drop_search.grid(row=0, column=1, pady=15, padx=10, sticky="w")

        txt_search = Entry(Display_Box, textvariable=self.search_text, font=("times new roman", 19, "italic"), bd=5,
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=15, padx=10, sticky="w")
        btn_search = Button(Display_Box, command=self.search_all, text="Search", height=2, width=10).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=5,
                                                                                                          pady=20)
        btn_showall = Button(Display_Box, command=self.fetch_all, text="Show All", height=2, width=10).grid(row=0,
                                                                                                            column=4,
                                                                                                            padx=5,
                                                                                                            pady=20)

        # -----------------Display Table
        Display_Table = Frame(Display_Box, bd=2, relief=RIDGE, bg="light yellow")
        Display_Table.place(x=10, y=70, width=870, height=600)

        scroll_side = Scrollbar(Display_Table, orient=HORIZONTAL)
        scroll_down = Scrollbar(Display_Table, orient=VERTICAL)
        self.travel_table = ttk.Treeview(Display_Table, columns=(
            "priority", "name", "country", "climate", "activities", "travel mode", "stay"),
                                         xscrollcommand=scroll_side.set,
                                         yscrollcommand=scroll_down.set)
        scroll_side.pack(side=BOTTOM, fill=X)
        scroll_down.pack(side=RIGHT, fill=Y)
        scroll_side.config(command=self.travel_table.xview)
        scroll_down.config(command=self.travel_table.yview)
        self.travel_table.heading("priority", text="Priority")
        self.travel_table.heading("name", text="Name")
        self.travel_table.heading("country", text="Country")
        self.travel_table.heading("climate", text="Climate")
        self.travel_table.heading("activities", text="Activities")
        self.travel_table.heading("travel mode", text="Travel Mode")
        self.travel_table.heading("stay", text="Stay")
        self.travel_table['show'] = 'headings'
        self.travel_table.column("priority", width=100)
        self.travel_table.column("name", width=100)
        self.travel_table.column("country", width=100)
        self.travel_table.column("climate", width=100)
        self.travel_table.column("activities", width=150)
        self.travel_table.column("travel mode", width=100)
        self.travel_table.column("stay", width=150)
        self.travel_table.pack(fill=BOTH, expand=1)
        self.travel_table.bind("<ButtonRelease-1>", self.find_cursor)
        self.fetch_all()

    def add_travels(self):
        if self.priority.get() == "" or self.name.get() == "":
            messagebox.showerror("Error", "Priority and Name cannot be blank")
        else:
            con = storage.connect()
            cur = con.cursor()
            cur.execute("insert into destinations values(%s, %s, %s, %s, %s, %s, %s)", (
                self.priority.get(),
                self.name.get(),
                self.country.get(),
                self.climate.get(),
                self.txt_activity.get('1.0', END),
                self.travel_mode.get(),
                self.stay.get()
            ))
        con.commit()
        self.fetch_all()
        self.clear_it()
        con.close()
        messagebox.showinfo("Congrats", "New destination entered.  You better start saving $$$!")

    def fetch_all(self):
        con = storage.connect()
        cur = con.cursor()
        cur.execute("select * from destinations")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.travel_table.delete(*self.travel_table.get_children())
            for x in rows:
                self.travel_table.insert('', END, values=x)
        con.commit()
        con.close()

    def clear_it(self):
        self.priority.set("")
        self.name.set("")
        self.country.set("")
        self.climate.set("")
        self.txt_activity.delete('1.0', END)
        self.travel_mode.set("")
        self.stay.set("")

    def find_cursor(self, ev):
        cursor_location = self.travel_table.focus()
        contents = self.travel_table.item(cursor_location)
        row = contents['values']
        print(row)
        self.priority.set(row[0])
        self.name.set(row[1])
        self.country.set(row[2])
        self.climate.set(row[3])
        self.txt_activity.delete('1.0', END)
        self.txt_activity.insert(END, row[4])
        self.travel_mode.set(row[5])
        self.stay.set(row[6])

    def update_data(self):
        con = storage.connect()
        cur = con.cursor()
        cur.execute(
            "update destinations set name=%s, country=%s, climate=%s, activities=%s, travel_mode=%s, stay=%s where "
            "priority=%s",
            (
                self.name.get(),
                self.country.get(),
                self.climate.get(),
                self.txt_activity.get('1.0', END),
                self.travel_mode.get(),
                self.stay.get(),
                self.priority.get()
            ))
        con.commit()
        self.fetch_all()
        self.clear_it()
        con.close()

    def delete_data(self):
        con = storage.connect()
        cur = con.cursor()
        cur.execute("delete from destinations where priority=%s", self.priority.get())
        rows = cur.fetchall()
        con.commit()
        con.close()
        self.fetch_all()
        self.clear_it()

    def search_all(self):
        con = storage.connect()
        cur = con.cursor()
        cur.execute("select * from destinations where " + str(self.search_drop.get()) + " LIKE '%" + str(
            self.search_text.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.travel_table.delete(*self.travel_table.get_children())
            for x in rows:
                self.travel_table.insert('', END, values=x)
        con.commit()
        con.close()


root = Tk()
ob = Travel(root)
root.mainloop()
