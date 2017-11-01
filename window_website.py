from Tkinter import *
import ttk

class WebsiteBoxes:
    def __init__(self, master):
        self.WebsiteEntry = Entry(master)
        self.WebsiteEntry.place(relx=0.03, rely=0.78, relheight=0.06
                , relwidth=0.68)
        self.WebsiteEntry.configure(background="white")
        self.WebsiteEntry.configure(font="TkFixedFont")
        self.WebsiteEntry.configure(width=406)

        self.HrefCheckVal = BooleanVar()
        self.HrefCheck = Checkbutton(master)
        self.HrefCheck.place(relx=0.03, rely=0.28, relheight=0.06, relwidth=0.08)

        self.HrefCheck.configure(activebackground="#d9d9d9")
        self.HrefCheck.configure(justify=LEFT)
        self.HrefCheck.configure(text='''href''')
        self.HrefCheck.configure(width=49, variable=self.HrefCheckVal)


        self.ProgressBar = ttk.Progressbar(master)
        self.ProgressBar.place(relx=0.03, rely=0.91, relwidth=0.93, relheight=0.0
                , height=19)
        self.ProgressBar.configure(length=560)

        self.TagLabel = Message(master)
        self.TagLabel.place(relx=0.03, rely=0.22, relheight=0.06, relwidth=0.18)
        self.TagLabel.configure(text="Tags(split by ','):", width=106)

        self.TagsBox = Text(master)
        self.TagsBox.place(relx=0.03, rely=0.38, relheight=0.38, relwidth=0.19)
        self.TagsBox.configure(background="white", font="TkFixedFont", width=116)
        self.TagsBox.insert(END, "p,a")