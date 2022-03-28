import Tkinter
import sqlite3
import TkTreectrl
from xlsxwriter.workbook import Workbook
import tkMessageBox
import re

class Visitorlog_app(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent 
        self.label_entry()
        self.button()
        self.multilistbox_scrollbar()
        self.create_db()
   
    def label_entry(self):
        self.grid()        
        self.names = ["Date(dd/mm/yyyy)", "Name", "Email ID", "Address", "Phone Number(USA format)", "Person Visiting", "TimeIn", "TimeOut"]
        self.entry = {}
        self.label = {}
        i = 0

        for name in self.names:
            e = Tkinter.Entry(self)
            e.grid(column = 1,columnspan = 2, sticky = "EW")
            self.entry[name] = e

            lb = Tkinter.Label(self, text = name, )
            lb.grid(row = i, column = 0, sticky = "W")
            self.label[name] = lb
            i += 1

    def button(self):
        Button1 = Tkinter.Button (self, text = u"Submit", command = self.OnSubmitClick)
        Button1.grid(row = 10, column = 0, sticky = "W")

        Button2 = Tkinter.Button (self, text = u"Export.xlsx", command = self.OnExport_XLSXclick)
        Button2.grid(row = 10, column = 2, sticky = "W")

        Button3 = Tkinter.Button (self, text = u"Delete", command = self.OnDeleteClick)
        Button3.grid(row = 10, column = 1, sticky = "W")
       
    def multilistbox_scrollbar(self):   
        self.scrollbarv = Tkinter.Scrollbar(self, orient=Tkinter.VERTICAL)
        self.scrollbarv.grid(row=14,column=3,sticky="NS")
        self.scrollbarh = Tkinter.Scrollbar(self, orient=Tkinter.HORIZONTAL)
        self.scrollbarh.grid(row=20,columnspan=3,sticky="EW")
        
        self.lbox = TkTreectrl.MultiListbox(self,width=500,height=400,selectmode=Tkinter.SINGLE)
        self.lbox.grid(row = 14, columnspan = 3, padx = 5,pady = 5)
        self.lbox.config(columns=('Date','Name','Email ID','Address','Phone Number','Person Visiting','TimeIn','TimeOut'))
        self.lbox.config(yscrollcommand=self.scrollbarv.set)
        self.scrollbarv.config(command=self.lbox.yview)
        self.lbox.config(xscrollcommand=self.scrollbarh.set)
        self.scrollbarh.config(command=self.lbox.xview)

    def create_db(self):
        self.connector = sqlite3.connect("guestbook.db")
        self.cursor = self.connector.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS guestbook(DATE TEXT,Name TEXT, EmailID TEXT,Address TEXT,Phone Number TEXT, PersonVisiting TEXT,TIMEIN TEXT,TIMEOUT TEXT)")
        self.connector.commit()

    def select_update(self):
        Data = self.cursor.execute("SELECT  * FROM guestbook")
        self.lbox.delete(0,Tkinter.END)

        for row in Data:
            display_list = self.lbox.insert(Tkinter.END,*map(unicode,row))
        
    def OnSubmitClick(self):
        entry_value =[]                
        d = re.compile('^((0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d)$')
        n = re.compile('^[a-zA-Z]+$')
        eID = re.compile('\w+@\w+\.(?:com|in)')
        p = re.compile('^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$')

        for name in self.names:
            if not self.entry[name].get():
                tkMessageBox.showerror("Unexpected Error", "Please enter all information")
                return None
            else:
                entry_value.append(self.entry[name].get())

        if d.match(entry_value[0])== None or p.match(entry_value[4])== None:
            tkMessageBox.showerror("Date and Ph-no Error", "Input whole numbers and not characters in Date and Phone number box or Check for appropriate format")

        elif n.match(entry_value[1])== None:
            tkMessageBox.showerror("Name Error", "Please check only characters allowed as input in Name box")
       
        elif eID.match(entry_value[2]) == None:
            tkMessageBox.showerror("email ID", "Please input EmailID in appropriate format")

        else:
            self.cursor.execute("INSERT INTO guestbook values (?,?,?,?,?,?,?,?)",entry_value)
            self.connector.commit()
            self.select_update()
                        
    def OnDeleteClick(self):
        self.cursor = self.connector.cursor()
        person = self.lbox.get(self.lbox.curselection()[0])
        person1 = map(list,person)
##        print person1[0]
        
        self.cursor.execute("DELETE FROM guestbook WHERE DATE=? AND Name=? AND EmailID=? AND Address=? AND Phone=? AND PersonVisiting=? AND TIMEIN=? AND TIMEOUT=?",(person1[0]))
        self.connector.commit()
        self.select_update()
        
    def OnExport_XLSXclick(self):
        workbook = Workbook('guestlist.xlsx')
        worksheet = workbook.add_worksheet()

        conn=sqlite3.connect('guestbook.db')
        c= conn.cursor()
        c.execute("SELECT * from guestbook")
        mysel=c.execute("SELECT * from guestbook")
        for i,row in enumerate(mysel):
            for j,column in enumerate(row):
                worksheet.write(i,j,column)
        workbook.close()


if __name__== "__main__":
    parent = "None"
    app = Visitorlog_app(parent)
    app.title('Visitor Log')
    app.mainloop()