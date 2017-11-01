from Tkinter import *

class TestingBoxes:
    def __init__(self, master):
        self.TestingHTML = LabelFrame(master)
        self.TestingHTML.place(relx=0.25, rely=0.03, relheight=0.73, relwidth=0.37)

        self.TestingHTML.configure(relief=GROOVE)
        self.TestingHTML.configure(text='''Testing HTML''')
        self.TestingHTML.configure(width=220)

        self.TestingInput = Text(self.TestingHTML)
        self.TestingInput.place(relx=0.05, rely=0.09, relheight=0.85, relwidth=0.89)
        self.TestingInput.configure(background="white", width=196, font="TkFixedFont", wrap = NONE)
        self.TestingInput.insert(END, 
        '<html>\n\t<a href="https://www.example.com">this is a link</a>\n\t<p>This is text</p>\n</html>')

        self.Labelframe2 = LabelFrame(master)
        self.Labelframe2.place(relx=0.62, rely=0.03, relheight=0.73
                , relwidth=0.37)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(text="Output")
        self.Labelframe2.configure(width=220)

        self.TestingOutput = Text(self.Labelframe2)
        self.TestingOutput.place(relx=0.05, rely=0.09, relheight=0.86
                , relwidth=0.89)
        self.TestingOutput.configure(background="white")
        self.TestingOutput.configure(font="TkTextFont")
        self.TestingOutput.configure(selectbackground="#c4c4c4")
        self.TestingOutput.configure(width=196)
        self.TestingOutput.configure(wrap=WORD)
