from tkinter import*
from tkinter import font

class my_main:
    def __init__(self,rot):
        self.root=Toplevel(rot)
        self.root.title("Font configure")
        self.root.geometry("350x410")
        self.root.resizable(height=0,width=0)
        self.fam="Arial"
        self.siz='16'
        self.sty="Regular"

        self.my_text=Text(self.root,width=43,height=1)
        self.my_text.place(x=0,y=350)
        conf=self.fam+" "+self.siz+" "+self.sty
        self.my_text.insert(INSERT,conf)

        my_button=Button(self.root,text="Select",command=self.go)
        my_button.place(x=130,y=375)

        self.list_box=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=20,height=18)
        self.list_box.place(x=0,y=0)
        for f in font.families():
            self.list_box.insert("end",f)
        self.list_box.bind('<ButtonRelease-1>',self.font_chooser)

        self.list_box2=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=10,height=18)
        self.list_box2.place(x=240,y=0)
        style=["Regular","Bold","Italic","Bold/Italic","Underline","Strike","Regular","Bold","Italic","Bold/Italic","Underline","Strike","Regular","Bold","Italic","Bold/Italic","Underline","Strike"]
        for f in style:
            self.list_box2.insert("end",f)
        self.list_box2.bind('<ButtonRelease-1>',self.style_chooser)

        self.list_box1=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=3,height=18)
        self.list_box1.place(x=185,y=0)
        for f in range(8,49,2):
            self.list_box1.insert("end",f)
        self.list_box1.bind('<ButtonRelease-1>',self.size_chooser)   

    def font_chooser(self,e):
        faml=self.list_box.get(self.list_box.curselection())
        self.fam=faml
        conf=self.fam+" "+self.siz+" "+self.sty
        print(conf,e)
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
    
    def size_chooser(self,e):
        faml=self.list_box1.get(self.list_box1.curselection())
        self.siz=str(faml)
        conf=self.fam+" "+self.siz+" "+self.sty
        print(conf)
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
   
    def style_chooser(self,e):#e is mandatory
        faml=self.list_box2.get(self.list_box2.curselection())
        self.sty=faml
        conf=self.fam+" "+self.siz+" "+self.sty
        print(conf)
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
    
    def go(self):
        sum=self.fam+self.siz+self.sty
        self.new_sum.set(sum)
        #self.root.destroy()
    

