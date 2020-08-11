from Tkinter import *
from PIL import ImageTk, Image
import ttk
from test_emotions import start_test
from record import record_input
import tkMessageBox

from play import start_play
import os

sourcepath="Test/"

window = Tk()
window.title("emotion identifier")
window.geometry("1000x1000")
window.configure(background='Black')


def display(input_t):
    T.insert(END, input_t)
    return



def refresh():
    listbox.delete(0, END)
    for f in os.listdir(sourcepath):
        #os.path.join(sourcepath, f)
        if f.endswith(".wav"):
            print(f)
            listbox.insert(END, f)
    return


def startplay():
    sel=listbox.curselection()
    print(sel.__len__())
    if(sel.__len__()<=0):
        tkMessageBox.showerror("Error", "Select any one audio file in the list.")
        return
    value=listbox.get(sel)
    print(value)
    start_play(file_play=value)
    return


def record():
    T.insert(END, "\nEnter the name of the Speaker and press \"Start\" button:\n")
    start_btn['state']='normal'
    return


def start():
    input = T.get("1.0",'end-1c')
    input = input.split("\n")[-1]
    print("FILE:"+input)
    record_input(name=input,T=T)
    T.insert(END,"\nFile saved as "+input+".wav\n")
    start_btn['state']='disabled'
    refresh()
    return


def test():
    sel=listbox.curselection()
    print(sel.__len__())
    if(sel.__len__()<=0):
        tkMessageBox.showerror("Error", "Select any one audio file in the list.")
        return
    value=listbox.get(sel)
    print(value)
    start_test(input_test=value,T=T)
    return



start_btn=Button(window, text="Start Record",command=start, disabledforeground = window.cget('bg'))
start_btn.config(height=2,width=10)
start_btn.place(x=800,y=300)

start_btn=Button(window, text="refresh",command=refresh, disabledforeground = window.cget('bg'))
start_btn.config(height=2,width=10)
start_btn.place(x=800,y=400)


record_img = Image.open('record_1.png')
rec_btn = Button(window, text="Record", command=record)
record_resized =record_img.resize((70,70),Image.ANTIALIAS)
rec_image = ImageTk.PhotoImage(record_resized)
rec_btn.config(image=rec_image,width="80",height="80",activebackground="blue",bg="grey", bd=0,highlightcolor="white")
rec_btn.place(x = 800, y = 172)


play_img = Image.open('play.png')
play_btn = Button(window, text="Play", command=startplay)
play_resized =play_img.resize((70,70),Image.ANTIALIAS)
pla_image = ImageTk.PhotoImage(play_resized)
play_btn.config(image=pla_image,width="80",height="80",activebackground="blue",bg="grey", bd=0,highlightcolor="white")
play_btn.place(x = 900, y = 172)


test_btn = Button(window, text="show emotion", command=test)
test_btn.place(x=900,y=300)
test_btn.config(height=2,width=10)

menu_bar = Menu(window,background='#000099',foreground='white',activebackground='red', activeforeground='white')

# create a pulldown menu, and add it to the menu bar
file_menu = Menu(menu_bar, tearoff=1)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu = menu_bar)
file_menu.entryconfig(1,foreground='red',background="white")

listbox=Listbox(window, background="#210c66", fg="White",selectbackground="red",highlightbackground="#37d3ff",highlightcolor="blue")
listbox.place(x =5, y = 5)
listbox.config(height=30, width=50)



for f in os.listdir(sourcepath):
    #os.path.join(sourcepath, f)
    if f.endswith(".wav"):
        print(f)
        listbox.insert(END, f)


T = Text(window, height=30, width=50)
T.place(x=300,y=5)
T.config(background="#ffffff")


window.mainloop()
