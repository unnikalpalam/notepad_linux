from tkinter import*
from tkinter import filedialog,colorchooser
from tkinter import messagebox,font
#from font_box import*
from threading import*
class notepad:
    current_file="No-File"
#........................functions..................#
    #no need of lambda 
    #...............file_function................#
    def exit_file(self,event=""):
        s=self.txtarea.get(1.0,END)
        if not s.strip():
            quit()
        else:
            result=messagebox.askyesnocancel("Exit Message For Save","Do you want to Save file")
            if result==TRUE:
                self.save_file()
                quit()
            else:
                quit()
    def new_file(self,event=""):
        s=self.txtarea.get(1.0,END)
        if not s.strip(): 
            self.new1_file()
        else:
            result=messagebox.askyesnocancel("Create New File","Continue, lost the details")
            if result==TRUE:
                self.clear()
                self.new1_file()
            else:
                pass
    def new1_file(self):
        h=filedialog.asksaveasfilename(initialdir="/home/ack/Documents/project/python_notes",title="Create New File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
        f=open(h,mode="w")
        f.write(self.txtarea.get(1.0,END))
        self.current_file=h
        self.root.title(self.current_file) 
        f.close()
    def saveas_file(self):
        h=filedialog.asksaveasfilename(initialdir="/home/ack/Documents/project/python_notes",title="Save As File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
        f=open(h,mode="w")
        f.write(self.txtarea.get(1.0,END))
        self.current_file=h
        self.root.title(self.current_file) 
        f.close()
    def save_file(self,event=""):
        if self.current_file=="No-File":
            self.saveas_file() 
        else:
            f=open(self.current_file,mode="w")
            f.write(self.txtarea.get(1.0,END))
            f.close()
    def open_file(self,event=""):
        if  (self.txtarea.get(1.0,END)).strip():
            result=messagebox.askyesnocancel("Create New File","Do you want to save the details")
            if result==TRUE:
                self.save_file()
                self.clear()
                result=filedialog.askopenfile(initialdir="/home/ack/Documents/project/python_notes",title="Open File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
                for data in result:
                    self.txtarea.insert(INSERT,data)
                self.current_file=result.name
                self.root.title(self.current_file) 
            elif result==FALSE:
                self.clear()
                result=filedialog.askopenfile(initialdir="/home/ack/Documents/project/python_notes",title="Open File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
                for data in result:
                    self.txtarea.insert(INSERT,data)
                self.current_file=result.name
                self.root.title(self.current_file) 
            else:
                pass 
        else:
            result=filedialog.askopenfile(initialdir="/home/ack/Documents/project/python_notes",title="Open File",filetypes=(("Text File","*.txt"),("All Files","*.*")))
            for data in result:
                self.txtarea.insert(INSERT,data)
            self.current_file=result.name
            self.root.title(self.current_file)  

    #..........................edit_function............#
    def clear(self):
        self.txtarea.delete(1.0,END) 
   
    def clears(self):   
        if  (self.txtarea.get(1.0,END)).strip():
            result=messagebox.askyesnocancel("Clear Warning","Do you want to clear the details")
            if result==TRUE:
                self.clear()
            else:
                pass
    def copy_file(self):
        self.txtarea.clipboard_clear()
        self.txtarea.clipboard_append(self.txtarea.selection_get())
    def paste_file(self):
        self.txtarea.insert(INSERT,self.txtarea.clipboard_get())
    def cut_file(self):
        self.copy_file()
        self.txtarea.delete('sel.first','sel.last')
   
    #...........................beautify_function...........#
    def bg(self):
        c=colorchooser.askcolor()
        self.txtarea.configure(background=c[1])

    def fg(self):
        c=colorchooser.askcolor()
        self.txtarea.configure(foreground=c[1])
 
    def fonts(self):
        rot=self.root
        app=my_main(rot)
    def set_font(self,lis):
        self.txtarea.config(font=lis)
    #........................geometry................#
    def __init__(self,root):
        self.root=root
        self.root.title("My Notepad")
        self.root.geometry("600x500")
        self.txtarea=Text(self.root,wrap="word",undo=TRUE,selectbackground="pink")
        self.txtarea.pack(fill=BOTH,expand=1,padx=5,pady=5)
        photo = PhotoImage(file = "ic.png")
        self.root.iconphoto(True, photo)
        self.root.bind("<Control-o>",self.open_file)
        self.root.bind("<Control-s>",self.save_file)
        self.root.bind("<Control-n>",self.new_file)
        self.root.bind("<Control-x>",self.exit_file)

    #.....................menu..........................#
        self.main_menu=Menu()
        self.root.config(menu=self.main_menu)
        #............file...........#
        self.file=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="| File",menu=self.file)
        self.file.add_command(label="New",accelerator='ctrl+N',command=lambda:self.new_file())#lambda use pass an argument
        self.file.add_command(label="Open",accelerator='ctrl+O',command=self.open_file)
        self.file.add_separator()
        self.file.add_command(label="Save",accelerator='ctrl+s',command=self.save_file)
        self.file.add_command(label="Save AS",command=self.saveas_file)
        self.file.add_separator()
        self.file.add_command(label="Exit",accelerator='ctrl+x',command=self.exit_file)
        #...................edit............#
        self.edit=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="| Edit",menu=self.edit)
        self.edit.add_command(label="Undo",command=self.txtarea.edit_undo)
        self.edit.add_command(label="Redo",command=self.txtarea.edit_redo)
        self.edit.add_separator()
        self.edit.add_command(label="Cut",command=self.cut_file)
        self.edit.add_command(label="Copy",command=self.copy_file)
        self.edit.add_command(label="Paste",command=self.paste_file)
        self.edit.add_separator()
        self.edit.add_command(label="Clear",command=self.clears)
        #..................Beautify................#
        self.beaut=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="| Beautify",menu=self.beaut)
        self.beaut.add_command(label="BG color",command=self.bg)
        self.beaut.add_command(label="Font color",command=self.fg)
        self.beaut.add_command(label="Fonts tyle",command=lambda:self.fonts())


#.......................................class...........................................#
class my_main:
    def __init__(self,rot):
        self.root=Toplevel(rot)
        self.root.title("Font configure")
        self.root.geometry("350x320+500+200")
        self.root.resizable(False, False)
        self.fam="Arial"
        self.siz='16'
        self.sty="normal"
        
        self.my_text=Text(self.root,width=43,height=1)
        self.my_text.place(x=0,y=240)
        conf=self.fam+" "+self.siz+" "+self.sty
        self.my_text.insert(INSERT,conf)

        my_button=Button(self.root,text="Select",command=self.select)
        my_button.place(x=90,y=275)

        my_button=Button(self.root,text="Exit",command=self.exits)
        my_button.place(x=180,y=275)

        self.list_box=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=20,height=12)
        self.list_box.place(x=0,y=0)
        #for f in font.families():
        fnt=['Arial','Helvetica','CourierNew','Courier','ComicSansMS', 'Fixedsys','MSSansSerif', 'MSSerif', 'Symbol', 'System', 'TimesNewRoman', 'Verdana']
        for f in fnt:
            self.list_box.insert("end",f)
        self.list_box.bind('<ButtonRelease-1>',self.font_chooser)

        self.list_box2=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=10,height=12)
        self.list_box2.place(x=240,y=0)
        style=["normal","bold","italic","underline","overstrike","normal","bold","italic","underline","overstrike","normal","bold","italic","underline","overstrike"]
        for f in style:
            self.list_box2.insert("end",f)
        self.list_box2.bind('<ButtonRelease-1>',self.style_chooser)

        self.list_box1=Listbox(self.root,selectmode=SINGLE,selectbackground="pink",width=3,height=12)
        self.list_box1.place(x=185,y=0)
        for f in range(2,37,2):
            self.list_box1.insert("end",f)
        self.list_box1.bind('<ButtonRelease-1>',self.size_chooser)   

    def font_chooser(self,e):
        faml=self.list_box.get(self.list_box.curselection())
        self.fam=faml
        conf=self.fam+" "+self.siz+" "+self.sty
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
    
    def size_chooser(self,e):
        faml=self.list_box1.get(self.list_box1.curselection())
        self.siz=str(faml)
        conf=self.fam+" "+self.siz+" "+self.sty
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
   
    def style_chooser(self,e):#e is mandatory
        faml=self.list_box2.get(self.list_box2.curselection())
        self.sty=faml
        conf=self.fam+" "+self.siz+" "+self.sty
        self.my_text.delete(1.0,END)
        self.my_text.insert(INSERT,conf)
    
    def select(self):
        arg=self.my_text.get(1.0,END)
        app.set_font(arg)
        #app.fg()

    def exits(self):
        self.root.destroy()
        #exit()
        #quit() close complete program
    

 

root=Tk() 
app=notepad(root)
root.mainloop()