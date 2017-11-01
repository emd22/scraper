import urllib
try:
    from bs4 import BeautifulSoup
    from Tkinter import *
except ImportError:
    print(
''' This application Requires:
        - Python 2.x
        - BeautifulSoup 4
        - Tkinter
        - Ttk''')

import ttk

from testing import *

class Window:
    def __init__(self, master, testing_boxes):
        self.master = master
        master.title("Webscraper Tool")

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        master.geometry("600x320+440+191")
        master.configure(cursor="arrow")

        self.WebsiteEntry = Entry(master)
        self.WebsiteEntry.place(relx=0.03, rely=0.78, relheight=0.06
                , relwidth=0.68)
        self.WebsiteEntry.configure(background="white")
        self.WebsiteEntry.configure(font="TkFixedFont")
        self.WebsiteEntry.configure(width=406)

        self.DownloadButton = Button(master)
        self.DownloadButton.place(relx=0.73, rely=0.78, height=26, width=137)
        self.DownloadButton.configure(activebackground="#d9d9d9", text='Download', width=137, command=self.download)

        self.HrefCheck = Checkbutton(master)
        self.HrefCheck.place(relx=0.03, rely=0.28, relheight=0.06, relwidth=0.08)

        self.HrefCheck.configure(activebackground="#d9d9d9")
        self.HrefCheck.configure(justify=LEFT)
        self.HrefCheck.configure(text='''href''')
        self.HrefCheck.configure(width=49)

        self.ProgressBar = ttk.Progressbar(master)
        self.ProgressBar.place(relx=0.03, rely=0.91, relwidth=0.93, relheight=0.0
                , height=19)
        self.ProgressBar.configure(length="560")

        self.TagLabel = Message(master)
        self.TagLabel.place(relx=0.03, rely=0.22, relheight=0.06, relwidth=0.18)
        self.TagLabel.configure(text='''Tags(split by ','):''')
        self.TagLabel.configure(width=106)

        self.menubar = Menu(master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.TagsBox = Text(master)
        self.TagsBox.place(relx=0.03, rely=0.38, relheight=0.38, relwidth=0.19)
        self.TagsBox.configure(background="white")
        self.TagsBox.configure(font="TkFixedFont")
        self.TagsBox.configure(width=116)

        self.Checkbutton2 = Checkbutton(master)
        self.Checkbutton2.place(relx=0.02, rely=0.03, relheight=0.06
                , relwidth=0.18)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Output to file''')

        self.FilePathInput = Entry(master)
        self.FilePathInput.place(relx=0.02, rely=0.09, relheight=0.06, relwidth=0.21)
        self.FilePathInput.configure(background="white")
        self.FilePathInput.configure(font="TkFixedFont")
        self.FilePathInput.configure(width=126)
    
    def download(self):
        website_link = self.WebsiteEntry.get()
        testing_output = False
        page_info = []

        if website_link == "":
            page = testing_boxes.TestingInput.get("1.0", 'end-1c')
            testing_output = True
        else:
            page = urllib.urlopen(website_link).read()
        soup = BeautifulSoup(page, "lxml")

        for tag in self.TagsBox.get("1.0", 'end-1c').split(','):
            page_info.append(soup.find(tag))

        page_text = ""

        for i in range(0, len(page_info)):
            page_text += page_info[i].getText()
        
        if testing_output == True:
            testing_boxes.TestingOutput.delete('1.0', END)
            testing_boxes.TestingOutput.insert(END, page_text)
        else:
            print(page_text)  

root = Tk()
#root.resizable(width=False, height=False)
#root.geometry('1028x680')
testing_boxes = TestingBoxes(root);
window = Window(root, testing_boxes)

root.mainloop()

# page = urllib.urlopen('https://en.wikipedia.org/wiki/Cheese').read()
# soup = BeautifulSoup(page, "lxml")
# page_info = soup.find_all('p')
# page_text = ""

# for i in range(0, len(page_info)):
#     page_text += page_info[i].getText()
# print(page_text)