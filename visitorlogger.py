#Import all the necessary modules
import sys
import wx
import sqlite3
import xlwt
import re
import datetime
import wx.lib.scrolledpanel

#Class       : mainwindow
#Description : This class creates the first main window where the user enters data.
#Parameters  : Parent frame if exists, id for the frame
#Inheritance : wx.frame

class mainwindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Player Log', size=(550,550))
        self.initialize()

#This method customizes the window - the text boxes, the buttons, background color and binds the events to the buttons.
    def initialize(self):
        self.panel=wx.Panel(self)
        self.SetBackgroundColour(wx.Colour(100,100,100))
        custom = wx.StaticText(self.panel, -1, "PLAYERS DETAILS", (5,10), (520,-1), wx.ALIGN_CENTRE)
        customfont = wx.Font(25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        custom.SetFont(customfont)
        wx.StaticText(self.panel, -1, "Name : ", (5,110))
        self.namevalue = wx.TextCtrl(self.panel,-1,pos=(120,110),size=(250,20))
        wx.StaticText(self.panel, -1, "Visiting : ", (5,280))
        wx.StaticText(self.panel, -1, "[Person name]", (5,300))
        self.personvalue = wx.TextCtrl(self.panel,-1,pos=(120,280),size=(250,20))
        
#Customize the buttons to be displayed on the screen        
        submitbutton=wx.Button(self.panel,label="Submit",pos=(5,410),size=(60,60))
        cancelbutton=wx.Button(self.panel,label="Cancel",pos=(70,410),size=(60,60))
        viewlist=wx.Button(self.panel,label="Search Options",pos=(140,410),size=(120,60))
        self.t1 = wx.TextCtrl(self.panel, -1, pos=(5,480), size=(550,20),style=wx.BORDER_NONE)
        self.t1.SetBackgroundColour(wx.Colour(100,100,100))

#Bind the buttons to events - functions        
        self.Bind(wx.EVT_BUTTON, self.savevalues, submitbutton)
        self.Bind(wx.EVT_BUTTON, self.cancelvalues, cancelbutton)
        self.Bind(wx.EVT_BUTTON, self.Playerlist, viewlist)   
        self.Bind(wx.EVT_TEXT, self.changenamecolour, self.namevalue)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

#This method exists the program when the close event occurs
    def OnClose(self, event):
        sys.exit()

#The below methods change the font color of data entered in text box to black
        
    def changenamecolour(self,event):
        self.namevalue.SetForegroundColour('black')

#This method gets the values enter by the user and validates them    
    def savevalues(self,event):
        self.flag = False
        self.check1 = False
        self.check2 = False
        self.check3 = False
        self.check4 = False
        self.check5 = False
        self.name = self.namevalue.GetValue()
        self.validatename()
        if self.flag == False:
            self.t1.ChangeValue("")
            self.connectdatabase()
            self.namevalue.Clear()
        else: 
            self.t1.ChangeValue("Invalid entries are displayed in red.Fields cannot be blank.Please re-enter valid data.")    
                
#This method validates the Player's name entered     
    def validatename(self):   
        if (len(self.name) == 0):
            self.flag = True
            self.namevalue.ChangeValue('--empty--')
            self.namevalue.SetForegroundColour('red')
        else:
            match = re.match(r'^([a-zA-Z. ]+)$', self.name, re.M|re.I)
            if not(match):
                self.flag = True
                self.namevalue.ChangeValue(self.name)
                self.namevalue.SetForegroundColour('red')
            
#This method validates the phone number             
#     def validatephoneno(self):  
#         if (len(self.phone) == 0):
#             self.flag = True
#             self.phonevalue.ChangeValue('--empty--')
#             self.phonevalue.SetForegroundColour('red')
#         else:
#             match = re.match(r'^(\d{3})-(\d{3})-(\d{4})$', self.phone, re.M)
#             if not(match):
#                 self.flag = True
#                 self.phonevalue.ChangeValue(self.phone)
#                 self.phonevalue.SetForegroundColour('red')

#This method validates the visiting person's name    
    def validateperson(self):
        if (len(self.person) == 0):
            self.flag = True
            self.personvalue.ChangeValue('--empty--')
            self.personvalue.SetForegroundColour('red')
        else:
            match = re.match(r'^([a-zA-Z. ]+)$', self.person, re.M|re.I)
            if not(match):
                self.flag = True
                self.personvalue.ChangeValue(self.person)
                self.personvalue.SetForegroundColour('red')
            
#This method validates the date entered            
#     def validatedate(self):
#         if (len(self.date) == 0):
#             self.flag = True
#             self.datevalue.ChangeValue('--empty--')
#             self.datevalue.SetForegroundColour('red')
#         else:
#             match = re.match(r'^(\d{2})-(\d{2})-(\d{4})$', self.date, re.M)
#             if (not(match)) or (int(self.date[0:2]) > 12) or (int(self.date[3:5]) > 31) or (int(self.date[6:]) > 2017) :
#                 self.flag = True
#                 self.datevalue.ChangeValue(self.date)
#                 self.datevalue.SetForegroundColour('red')
            
#This method clears off the values entered and does not store it in database            
    def cancelvalues(self,event) :
        self.namevalue.Clear()
        self.emailvalue.Clear()
        self.phonevalue.Clear()
        self.personvalue.Clear()
        self.datevalue.Clear() 
        self.t1.ChangeValue("")     

#Displays a new window once the search option button is clicked
    def Playerlist(self,event) :
    	list=newwindow(parent=None,id=-1)
    	list.Show()
    	app.MainLoop()
    	
#Store the values into database if the inputs are valid       
    def connectdatabase(self):
        conn = sqlite3.connect('Player.db')
        c = conn.cursor()
        c.execute("create table if not exists Players (name text, email text, phone text, person text, entrydate text)")
        c.execute("insert into Players values (?);",(self.name))
        conn.commit()
        c.close()

#Class       : newwindow
#Description : This class creates the second window where the search options are provided.
#Parameters  : Parent frame if exists, id for the frame
#Inheritance : wx.Frame

class newwindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Search Options', size=(550,550))
        self.initialize()

#This method customizes the window - the text boxes, the buttons, background color and binds the events to the buttons.
    def initialize(self):
    	self.panel=wx.Panel(self, -1)
    	self.SetBackgroundColour(wx.Colour(100,100,100))
    	self.Centre()
    	self.Show()
    	custom = wx.StaticText(self.panel, -1, "SEARCH OPTIONS", (5,10), (520,-1), wx.ALIGN_CENTRE)
        customfont = wx.Font(25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        custom.SetFont(customfont)
        wx.StaticText(self.panel, -1, "View the list of all the Players: ", (15,80))
        search=wx.Button(self.panel,label="View",pos=(15,90),size=(120,60))
        self.Bind(wx.EVT_BUTTON, self.fetchlist, search)
        line = wx.StaticLine(self,-1,wx.Point(1,160), wx.Size(550,2),wx.LI_HORIZONTAL)
        wx.StaticText(self.panel, -1, "Player Name : ", (15,360))
        self.playername = wx.TextCtrl(self.panel,-1,pos=(110,360),size=(120,20))
        search2=wx.Button(self.panel,label="Search",pos=(15,380),size=(120,60))
        self.Bind(wx.EVT_BUTTON, self.detailsquery, search2)
        self.error = wx.TextCtrl(self.panel, -1, pos=(5,440), size=(550,20),style=wx.BORDER_NONE)
        self.error.SetBackgroundColour(wx.Colour(100,100,100)) 

#The below methods change the font color of data entered in text box to black        
    def changefromcolour(self,event):
        self.fromdate.SetForegroundColour('black')       

    def changetocolour(self,event):
        self.todate.SetForegroundColour('black')
        
#this method validates the date entered            
#     def checkdate(self,event):
#         self.start = self.fromdate.GetValue()
#         self.end = self.todate.GetValue()
#         self.flag = False
#         if (len(self.start) == 0):
#             self.flag = True
#             self.fromdate.ChangeValue('--empty--')
#             self.fromdate.SetForegroundColour('red')
#         else:
#             checkflag  = self.dateformatcheck(self.start)
#             if (checkflag) :
#                 self.flag = True
#                 self.fromdate.ChangeValue(self.start)
#                 self.fromdate.SetForegroundColour('red')
#         if (len(self.end) == 0):
#             self.flag = True
#             self.todate.ChangeValue('--empty--')
#             self.todate.SetForegroundColour('red')
#         else:
#             checkflag1  = self.dateformatcheck(self.end)
#             if (checkflag1) :
#                 self.flag = True
#                 self.todate.ChangeValue(self.end)
#                 self.todate.SetForegroundColour('red')
#         if not(self.flag):
#             self.datelist()
#         else:
#             self.error.ChangeValue("Invalid entries are displayed in red.Fields cannot be blank.Please re-enter valid data.")

#This method checks if the date is in the proper format                
#     def dateformatcheck(self,valuedate):
#         match = re.match(r'^(\d{2})-(\d{2})-(\d{4})$', valuedate, re.M)
#         if (not(match)) or (int(valuedate[0:2]) > 12) or (int(valuedate[3:5]) > 31) or (int(valuedate[6:]) > 2017) :
#             checkflag = True
#         else :
#             checkflag = False
#         return checkflag
            
#This method connects to database and fetch all the Players list    
    def fetchlist(self,event):
        self.error.ChangeValue("")
        self.conn = sqlite3.connect('player.db')
        self.c = self.conn.cursor() 
        self.c.execute("""SELECT name from players""") 
        self.calllistwindow()       
                            
#This method connects to database and fetch all the Players list based on the date range    
    def datelist(self):
        self.error.ChangeValue("")
        self.fromdate.Clear()
        self.todate.Clear()
        self.conn = sqlite3.connect('player.db')
        self.c = self.conn.cursor()
        startdate = datetime.datetime.strptime(self.start, '%m-%d-%Y').strftime('%Y%m%d')
        enddate = datetime.datetime.strptime(self.end, '%m-%d-%Y').strftime('%Y%m%d') 
        self.c.execute("""SELECT name from Players WHERE
                  substr(entrydate,7)||substr(entrydate,1,2)||substr(entrydate,4,2)
                  BETWEEN ? AND ?""",(startdate, enddate))  
        self.calllistwindow()       


#This method fetches the Players list baed on the name given in search option.
    def detailsquery(self,event):
        self.error.ChangeValue("")
        namequery = str(self.Playername.GetValue())
        self.conn = sqlite3.connect('player.db')
        self.c = self.conn.cursor()
        self.c.execute("""SELECT * from Players WHERE
                  name LIKE (?||'%')""", (namequery,))
        self.Playername.Clear()         
        self.calllistwindow()  

#This method closes the database connection and calls the third window that displays the result    	
    def calllistwindow(self):
        self.conn.commit()
        rows = self.c.fetchall()
        self.result = [row[0] for row in rows]
        self.conn.close()
        list1=listwindow(parent=None,id=-1,result=self.result)
    	list1.Show()
    	app.MainLoop()

#Class       : listwindow
#Description : This class creates the third window that displays the results of search.
#Parameters  : Parent frame if exists, id for the frame
#Inheritance : wx.Frame
         
class listwindow(wx.Frame):

    def __init__(self,parent,id,result):
        wx.Frame.__init__(self,parent,id,'Player list', size=(550,550))
        self.result = result
        self.initialize() 

#This method customizes the window - Download button, background color and binds the event to the button.        
    def initialize(self):
        self.panel = wx.ScrolledWindow(self, -1)
        self.SetBackgroundColour(wx.Colour(100,100,100))
        self.panel.SetScrollbars(1, 1, 0, 1000)
    	self.Centre()
    	self.Show()
    	custom = wx.StaticText(self.panel, -1, "LIST OF PlayerS", (5,10), (520,-1), wx.ALIGN_CENTRE)
        customfont = wx.Font(25, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        custom.SetFont(customfont)
        n = 50          
        for vname in self.result:
            n = n + 30
            position = (25,n)
            vname = ' '.join(word[0].upper() + word[1:] for word in vname.split())
            Players = wx.StaticText(self.panel, -1, str(vname), position)
            Playerfont = wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
            Players.SetFont(Playerfont)

#Displays the button to download the information into excel if there are values fetched from the search queries
        if (len(self.result) != 0):
            download=wx.Button(self.panel,label="Download",pos=(380,35),size=(120,60))
            self.Bind(wx.EVT_BUTTON, self.writetoexcel, download)
        
#This method writes the Players list into excel and saves the excel file.    
    def writetoexcel(self,event):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("Sheet1")
        style = xlwt.easyxf('font: bold 1')
        sheet.write(0,0,'Players list',style)
        n = 2
        for name in self.result:
            name = ' '.join(word[0].upper() + word[1:] for word in name.split())
            sheet.write(n,0,name)
            n = n + 1
 	    workbook.save("Playerlist.xls")
        	                    
#Main program starts here. It calls the first window.
     
if __name__=='__main__':
    app=wx.App()
    frame=mainwindow(parent=None,id=-1)
    frame.Show()
    app.MainLoop()