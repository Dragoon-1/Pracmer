from tkinter import *
import tkinter
from tkinter import ttk
from time import sleep
from tkinter import filedialog as fd
import os
import messagebox
import shutil
#logic

def otime():
    if not os.path.exists("pracmerf"):
        os.mkdir("pracmerf")
        print("Directory 'pracmerf' created.")
    else:
        print("Directory 'pracmerf' already exists.")

def adddfile(filename,content):
    with open(f"pracmerf/{filename}",'w+') as f:
        f.write(content)

def seeefile(filename):
    with open(f"pracmerf/{filename}",'r') as f:
        content=f.read()
        return content
def find_folder(folder_name, search_path="C:\\"):
    result = []
    for root, dirs, files in os.walk(search_path):
        if folder_name in dirs:
            result.append(os.path.join(root, folder_name))
    return result

#___________________________________________________________________________________________________________________________________________________
# tkinter screen
#2 remaining 
def addfile():
    def badd():
        etb.place_forget()
        fn.place_forget()
        bbtn.place_forget()
        fnen.place_forget()
        #sfbtn.place_forget()
        afbtn.place_forget()
        mainwsee()

#os.copy error
    def sfpc():
        file=fd.askopenfilename()
        if file:
            fn = os.path.basename(file)
            destination_dir = find_folder("pracmer")
        
        # Ensure the destination directory exists
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
        
        print(fn)
        print(find_folder("pracmer"))
        shutil.copy(file, f"{find_folder("pracmer")}/{fn}")
        messagebox.showinfo("success","File Created Successfully")
        
    def gfs():
        #get the filename from entry and save the text from text box
        a=fnen.get()
        content=etb.get(1.0,END)
        with open(f"pracmerf/{a}",'w+') as f:
            content=etb.get(1.0,END)
            f.write(content)
        messagebox.showinfo("success","File Created Successfully")
        etb.delete(1.0,END)
        fnen.delete(0,END)
        
        
    mainwdes()
    etb=Text(t,font=("Cursive", 18),bg='white',fg='black',border=2,width=40, height=16)
    etb.place(x=50,y=80)
    bbtn=Button(t,text="<=Back",font=("Arial",18),bg="antiquewhite3",fg="blue2",border=1,command=lambda:badd())
    bbtn.place(x=40,y=10)
    fn=Label(t, text="Enter filename :\n(with extention eg-.txt,.py)", font=("Cursive", 20),bg='black',fg='Orange',border=2)
    fn.place(x=600,y=65)
    fnen=Entry(t,font=("Cursive", 22),bg='black',fg='cyan',border=2,cursor="xterm")
    fnen.place(x=880,y=65)
    #sfbtn=Button(t,text="Select file",font=("Cursive", 20),bg='black',fg='Orange',border=2,command=lambda:sfpc())
    #sfbtn.place(x=600,y=150)
    afbtn=Button(t,text="add file",font=("Cursive", 20),bg='black',fg='Orange',border=2,command=lambda:gfs())
    afbtn.place(x=1000,y=150)
    
    

#remaining
def seefile():
    mainwdes()
        
    def sescf():
        def bttn():
            shtext.place_forget()
            bbttn.place_forget()
            try:
                seefile()
            except:
                pass
        a=monthchoosen.get()
        with open(f"pracmerf/{a}",'r') as f:
            con=f.read()
        
        monthchoosen.place_forget()
        gbtn.place_forget()
        bbtn.place_forget()
        sl.place_forget()
        bbttn=Button(t,text="<=Back",font=("Arial",18),bg="antiquewhite3",fg="blue2",border=1,command=lambda:bttn())
        bbttn.place(x=40,y=10)
        shtext=Text(t,font=("Cursive", 18),bg='white',fg='black',border=2,width=40, height=16,)
        shtext.place(x=50,y=80)
        shtext.insert(END,con)
    
    def bttn():
        monthchoosen.place_forget()
        gbtn.place_forget()
        bbtn.place_forget()
        sl.place_forget()
        mainwsee()
   
    sl=Label(t, text="Select file:", font=("Cursive", 20),bg='black',fg='Orange',border=2)
    sl.place(x=50,y=100)
    n=tkinter.StringVar()
    monthchoosen = ttk.Combobox(t, width = 50,font=("Cursive", 14), textvariable = n) 
    
    monthchoosen['values'] = os.listdir("pracmerf")
    monthchoosen.place(x=190,y=100)
    gbtn=Button(t,text="See File",font=("Arial",18),bg="firebrick1",fg="black",border=1,command=lambda:sescf())
    gbtn.place(x=850,y=300)
    bbtn=Button(t,text="<=Back",font=("Arial",18),bg="antiquewhite3",fg="blue2",border=1,command=lambda:bttn())
    bbtn.place(x=40,y=10)
    


#del file , add filees path     
def delfile():
    mainwdes()
    def bttn():
        monthchoosen.place_forget()
        gbtn.place_forget()
        bbtn.place_forget()
        sl.place_forget()
        mainwsee()
    def df():
        a=monthchoosen.get()
        l=os.listdir("pracmerf")
        if a in l:
            os.remove(f"pracmerf/{a}")
            messagebox.showinfo("success","File Deleted Successfully")
            
        else:
            messagebox.showerror("error","File Not Found😭")
            
    sl=Label(t, text="Select file:", font=("Cursive", 20),bg='black',fg='Orange',border=2)
    sl.place(x=50,y=100)
    n=tkinter.StringVar()
    monthchoosen = ttk.Combobox(t, width = 50,font=("Cursive", 14), textvariable = n) 
    
    monthchoosen['values'] = os.listdir("pracmerf")
    
    monthchoosen.place(x=190,y=100)
    gbtn=Button(t,text="Delete File",font=("Arial",18),bg="firebrick1",fg="black",border=1,command=lambda:df())
    gbtn.place(x=850,y=300)
    bbtn=Button(t,text="<=Back",font=("Arial",18),bg="antiquewhite3",fg="blue2",border=1,command=lambda:bttn())
    bbtn.place(x=40,y=10)



def mainwdes():
    addbtn.place_forget()
    seebtn.place_forget()
    delbtn.place_forget()
def mainwsee():
    addbtn.place(x=550,y=100)
    seebtn.place(x=550,y=250)
    delbtn.place(x=550,y=400)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == "__main__":
    otime()
    t1=tkinter.Tk()
    t1.title('loading')
    window_width = 500
    window_height = 300
    screen_width = t1.winfo_screenwidth()
    screen_height = t1.winfo_screenheight()

    # Calculate the position to center the window
    x_ = (screen_width // 2) - (window_width // 2)
    y_ = (screen_height // 2) - (window_height // 2)

    # Set the geometry with the calculated position
    t1.geometry(f"{window_width}x{window_height}+{x_}+{y_}")
    t1.configure(bg='black')
    
    Label(t1, text="Welcome to \nPractical manager", font=("Cursive", 30),bg='black',fg='Orange',border=2).place(x=x_//2-90,y=y_//2-50)
    
    t1.update() 
    sleep(2)
    t1.destroy()


    t = tkinter.Tk()
    t.title('Pracmer')
    sw=t.winfo_screenwidth()
    sh=t.winfo_screenheight()
    t.geometry("%dx%d" % (sw,sh))
    t.configure(bg='black')
    
    addbtn=Button(t,text="Add file",font=("Cursive", 30),bg='black',fg='Orange',border=2,command=lambda: addfile())
    addbtn.place(x=550,y=100)
    
    seebtn=Button(t,text="see file",font=("Cursive", 30),bg='black',fg='Orange',border=2,command=lambda: seefile())
    seebtn.place(x=550,y=250)
    
    delbtn=Button(t,text="Delete file",font=("Cursive", 30),bg='black',fg='Orange',border=2,command=lambda: delfile())
    delbtn.place(x=550,y=400)
    t.mainloop()