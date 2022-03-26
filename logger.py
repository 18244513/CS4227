import tkinter as tk
from tkinter import tkmessagebox
import sqlite3
import sys
from tkinter import *
import re
import pygame
import tkTreectrl
from xlsxwriter.workbook import Workbook


class Visitorlog_app(tkinter.tk):

    def __init__(self,parent):
        t.Tk.__init__(self,parent)
        self.parent = parent 
        self.label_entry()
        self.button()
        self.multilistbox_scrollbar()
        self.create_db()
   
    def label_entry(self):
        self.grid()        
        self.names = ["Name",]
        self.entry = {}
        self.label = {}
        i = 0

        for name in self.names:
            e = t.Entry(self)
            e.grid(column = 1,columnspan = 2, sticky = "EW")
            self.entry[name] = e

            lb = t.Label(self, text = name, )
            lb.grid(row = i, column = 0, sticky = "W")
            self.label[name] = lb
            i += 1

    def button(self):
        Button1 = t.Button (self, text = u"Submit", command = self.OnSubmitClick)
        Button1.grid(row = 10, column = 0, sticky = "W")

        Button2 = t.Button (self, text = u"Export.xlsx", command = self.OnExport_XLSXclick)
        Button2.grid(row = 10, column = 2, sticky = "W")

        Button3 = t.Button (self, text = u"Delete", command = self.OnDeleteClick)
        Button3.grid(row = 10, column = 1, sticky = "W")
       
    def multilistbox_scrollbar(self):   
        self.scrollbarv = t.Scrollbar(self, orient=t.VERTICAL)
        self.scrollbarv.grid(row=14,column=3,sticky="NS")
        self.scrollbarh = t.Scrollbar(self, orient=t.HORIZONTAL)
        self.scrollbarh.grid(row=20,columnspan=3,sticky="EW")
        
        self.lbox = tkTreectrl.MultiListbox(self,width=500,height=400,selectmode=t.SINGLE)
        self.lbox.grid(row = 14, columnspan = 3, padx = 5,pady = 5)
        self.lbox.config(columns=('Name', 'Score'))
        self.lbox.config(yscrollcommand=self.scrollbarv.set)
        self.scrollbarv.config(command=self.lbox.yview)
        self.lbox.config(xscrollcommand=self.scrollbarh.set)
        self.scrollbarh.config(command=self.lbox.xview)

    def create_db(self):
        self.connector = sqlite3.connect("scoreboard.db")
        self.cursor = self.connector.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scoreboard(Name TEXT)")
        self.connector.commit()

    def select_update(self):
        Data = self.cursor.execute("SELECT  * FROM scoreboard")
        self.lbox.delete(0,t.END)

        for row in Data:
            display_list = self.lbox.insert(t.END,*map(unicode,row))
        
    def OnSubmitClick(self):
        entry_value =[]
        n = re.compile('^[a-zA-Z]+$')

        for name in self.names:
            if not self.entry[name].get():
                tkMessageBox.showerror("Unexpected Error", "Please enter all information")
                return None
            else:
                entry_value.append(self.entry[name].get())

        else :match(entry_value[1])== None
        tkMessageBox.showerror("Name Error", "Please check only characters allowed as input in Name box")
       
        else:
            self.cursor.execute("INSERT INTO scoreboard values (?)",entry_value)
            self.connector.commit()
            self.select_update()
                        
        def OnDeleteClick(self):
        self.cursor = self.connector.cursor()
        person = self.lbox.get(self.lbox.curselection()[0])
        person1 = map(list,person)
##        print person1[0]
        
        self.cursor.execute("DELETE FROM scoreboard WHERE Name=?",(person1[0]))
        self.connector.commit()
        self.select_update()
        
    def OnExport_XLSXclick(self):
        workbook = Workbook('guestlist.xlsx')
        worksheet = workbook.add_worksheet()

        conn=sqlite3.connect('scoreboard.db')
        c= conn.cursor()
        c.execute("SELECT * from scoreboard")
        mysel=c.execute("SELECT * from scoreboard")
        for i,row in enumerate(mysel):
            for j,column in enumerate(row):
                worksheet.write(i,j,column)
        workbook.close()


    if __name__== "__main__":
    parent = "None"
    app = Visitorlog_app(parent)
    app.title('Visitor Log')
    app.mainloop()