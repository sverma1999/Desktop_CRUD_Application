from tkinter import *
from backEndScript import Database


database= Database("dbname='SomeCompanyDatabase' user='postgres' password='inner123' host='localhost' port='5432' ")




class Window(object):
    """
    This Program stores Employees information:
    EmployeeName, Comapany
    Position, Salary

    User can:

    View all the stored employees
    Search an Employee
    Add entry
    Update entry
    Delete 
    Close
    """

    def get_selected_row(self, event):
        try:
            #global selected_tuple
            index= self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.empName.delete(0, END)
            self.empName.insert(END, self.selected_tuple[1])
            self.cmpName.delete(0, END)
            self.cmpName.insert(END, self.selected_tuple[2])
            self.position.delete(0, END)
            self.position.insert(END, self.selected_tuple[3])
            self.salary.delete(0, END)
            self.salary.insert(END, self.selected_tuple[4])
        except IndexError:
            pass
            
        

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.empName_text.get(), self.cmpName_text.get(),self. position_text.get(), self.salary_Value.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.empName_text.get(), self.cmpName_text.get(), self.position_text.get(), self.salary_Value.get())
        self.list1.delete(0,END)
        self.list1.insert(END, (self.empName_text.get(), self.cmpName_text.get(), self.position_text.get(), self.salary_Value.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.empName_text.get(), self.cmpName_text.get(), self.position_text.get(), self.salary_Value.get())




    def __init__(self, window):

        #Windows settings
        self.window=window
        self.window.geometry("800x450")
        self.window.resizable(width=False, height=False)
        self.window.wm_title("Some Company Employees")

        #labels
        lbl1 = Label(window, text="Full Name", width=12, height=3)
        lbl1.grid(row=0, column=0)

        lbl2 = Label(window, text="Comapany", width=12, height=3)
        lbl2.grid(row=0, column=2)

        lbl3 = Label(window, text="Position", width=12, height=3)
        lbl3.grid(row=1, column=0)

        lbl4 = Label(window, text="Salary", width=12, height=3)
        lbl4.grid(row=1, column=2)


        #entries
        self.empName_text = StringVar()
        self.empName = Entry(window, textvariable = self.empName_text, width=30)
        self.empName.grid(row=0, column=1)

        self.cmpName_text = StringVar()
        self.cmpName = Entry(window, textvariable = self.cmpName_text, width=30)
        self.cmpName.grid(row=0, column=3)

        self.position_text = StringVar()
        self.position = Entry(window, textvariable = self.position_text, width=30)
        self.position.grid(row=1, column=1)

        self.salary_Value = StringVar()
        self.salary = Entry(window, textvariable = self.salary_Value, width=30)
        self.salary.grid(row=1, column=3)


        #list of records
        self.list1 = Listbox(window, height=15, width=40)
        self.list1.grid(row=2,column=0, rowspan=7, columnspan=2)

        list_scrollbar1 = Scrollbar(window)
        list_scrollbar1.grid(row=2,column=2, rowspan=10)

        self.list1.configure(yscrollcommand=list_scrollbar1.set)
        list_scrollbar1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #buttons
        btn1 = Button(window, text="View All", width=12, height=3, command=self.view_command)
        btn1.grid(row=2, column=3)

        btn1 = Button(window, text="Search Employee", width=12, height=3, command=self.search_command)
        btn1.grid(row=3, column=3)

        btn1 = Button(window, text="Add Employee", width=12, height=3, command=self.add_command)
        btn1.grid(row=4, column=3)

        btn1 = Button(window, text="Update Employee", width=12, height=3, command=self.update_command)
        btn1.grid(row=5, column=3)

        btn1 = Button(window, text="Delete Employee", width=12, height=3, command=self.delete_command)
        btn1.grid(row=6, column=3)

        btn1 = Button(window, text="Close Window", width=12, height=3, command=window.destroy)
        btn1.grid(row=7, column=3)

window = Tk()
Window(window)
window.mainloop()
