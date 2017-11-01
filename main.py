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

from window_testing import *
from window_website import *

class Window:
    def __init__(self, master, testing_boxes, website_boxes):
        self.master = master
        master.title("Webscraper Tool 01.11.17")

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')

        master.geometry("600x320+440+191")

        self.DownloadButton = Button(master)
        self.DownloadButton.place(relx=0.73, rely=0.78, height=26, width=137)
        self.DownloadButton.configure(activebackground="#d9d9d9", text='Download', width=137, command=self.download)


        self.Checkbutton2 = Checkbutton(master)
        self.Checkbutton2.place(relx=0.02, rely=0.03, relheight=0.06
                , relwidth=0.18)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text="Output to file")

        self.FilePathInput = Entry(master)
        self.FilePathInput.place(relx=0.02, rely=0.09, relheight=0.06, relwidth=0.21)
        self.FilePathInput.configure(background="white")
        self.FilePathInput.configure(font="TkFixedFont")
        self.FilePathInput.configure(width=126)
    
    def download(self):
        website_link = website_boxes.WebsiteEntry.get()
        testing_output = False
        page_info = []

        if website_link == "":
            page = testing_boxes.TestingInput.get("1.0", 'end-1c')
            testing_output = True
        else:
            page = urllib.urlopen(website_link).read()
        soup = BeautifulSoup(page, "html.parser")

        tags = website_boxes.TagsBox.get("1.0", 'end-1c').split(',')

        if website_boxes.HrefCheckVal.get():
            for wrapper in soup.find_all('a', href=True):
                page_info.append(wrapper['href'])
        else:
            for tag in tags:             
                for wrapper in soup.find_all(tag):
                    page_info.append(wrapper.text)
                

        page_text = ""

        for i in range(0, len(page_info)):
            page_text += page_info[i]+'\n'
        
        testing_boxes.TestingOutput.delete('1.0', END)
        testing_boxes.TestingOutput.insert(END, page_text)


root = Tk()
#root.resizable(width=False, height=False)
#root.geometry('1028x680')
testing_boxes = TestingBoxes(root)
website_boxes = WebsiteBoxes(root)
window = Window(root, testing_boxes, website_boxes)


root.mainloop()