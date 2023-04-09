from tkinter import *
from tkinter import ttk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from tkvideo import *
from PIL import Image,ImageTk
from threading import Timer
Switch_flag = 0
Open_flag = 0
Run_flag = 0
Curr_State = "OFF"
Open_State = "Door Closed"
Run_State = "Not Heating"
Enfa_State = "q0"
Door = None
img = None
Combo = None
fsm = None
def Photos():
    global Door,img,fsm
    Door=ImageTk.PhotoImage((Image.open("C:/ATC/Door_closed.jpg")).resize((710,400)))
    img=ImageTk.PhotoImage((Image.open("C:/ATC/Switch_off.jpg")).resize((710,400)))
    fsm=ImageTk.PhotoImage((Image.open("C:/ATC/nfa.jpeg")).resize((480,270)))
def Button_pack():
    frame = Frame(root)
    frame1 = Frame(root)
    frame2 = Frame(root)
    global Combo,Run_flag,Run_State,Enfa_State
    if Switch_flag == 0 and Open_flag == 0 and Run_flag == 0:
        Enfa_State = "q0"
    elif Switch_flag == 0 and Open_flag == 1 and Run_flag == 0:
        Enfa_State = "q1"
    elif Switch_flag == 1 and Open_flag == 0 and Run_flag == 0 and Enfa_State == "q4":
        Enfa_State = "q5"
    elif Switch_flag == 1 and Open_flag == 0 and Run_flag == 0:
        Enfa_State = "q2"
    elif Switch_flag == 1 and Open_flag == 1 and Run_flag == 0:
        Enfa_State = "q3"
    elif Switch_flag == 1 and Open_flag == 0 and Run_flag == 1:
        Enfa_State = "q4"
    State = Label(root,text = "Current State of Oven(" + Enfa_State + "): " + Curr_State + ", " + Open_State + ", " + Run_State,font = ("",10,"italic"))
    State.pack(pady = 5)
    Run_State = "Not Heating"
    Sym = Label(root,text = "Input Symbols:",font = ("",10,"bold"))
    Sym.pack()
    frame1.pack()
    if Switch_flag == 0:
        On = Button(frame1,text = "Switch On",command = Switch_On)
    else:
        On = Button(frame1,text = "Switch On",state = DISABLED)       
    On.pack(pady = 10,side = LEFT)
    if Switch_flag == 1:
        Off = Button(frame1,text = "Switch Off",command = Switch_Off)
    else:
        Off = Button(frame1,text = "Switch Off",state = DISABLED) 
    Off.pack(side = RIGHT,padx = 20)
    if Open_flag == 0 and Run_flag ==0:
        Open = Button(frame2,text = "Open Door",command = Open_Door)
    else:
        Open = Button(frame2,text = "Open Door",state = DISABLED)       
    frame2.pack()
    Open.pack(pady = 10,side = LEFT)
    if Open_flag == 1:
        Close = Button(frame2,text = "Close Door",command = Close_Door)
    else:
        Close = Button(frame2,text = "Close Door",state = DISABLED) 
    Close.pack(side = RIGHT,padx = 20)
    vlist = ["50°C, Top, 15 Min","100°C, Bottom, 15 Min","200°C, Both, 5 Min"]
    Combo = ttk.Combobox(frame, values = vlist)
    Combo.set("50°C, Top, 15 Min")
    frame.pack()
    Combo.pack(pady = 10,side=LEFT)
    if Open_flag == 0 and Switch_flag == 1:
        Temp = Button(frame,text = "Set and Start",command = Set_Temp)
    else:
        Temp = Button(frame,text = "Set and Start",state = DISABLED)
    Temp.pack(side = RIGHT,padx = 20,pady=10)
    L = Label(root, image = fsm)
    L.pack()
    if Run_flag == 1:
        Run_State = "Done!"
        Run_flag = 0
        t = Timer(10, lambda:[notVideo(),Button_pack()])
        t.start()
def notVideo():
    f=0
    for widget in root.winfo_children():
        f=f+1
        if f==1:
            continue
        widget.destroy()
def Set_Temp():
    global Combo,Run_State,Run_flag
    Run_State = "Heating"
    Run_flag = 1
    Choice = Combo.get()
    for widget in root.winfo_children():
        widget.destroy()
    my_label = Label(root)
    my_label.pack() 
    if Choice == "50°C, Top, 15 Min":
        player = tkvideo("C:/ATC/Temperature_50.mp4", my_label, loop = 0, size = (250,400))
        player.play()
        action = Label(root,text = "Setting Temperature, Mode and Timer...",font = ("",10,"italic"))
        t1 = Timer(0.315, action.pack)
        t1.start()
        t = Timer(3, lambda:[action.destroy(),Button_pack()])  
        t.start()
    elif Choice == "100°C, Bottom, 15 Min":
        player = tkvideo("C:/ATC/Temperature_100.mp4", my_label, loop = 0, size = (250,400))
        player.play()
        action = Label(root,text = "Setting Temperature, Mode and Timer...",font = ("",10,"italic"))
        t1 = Timer(0.315, action.pack)
        t1.start()
        t = Timer(4.7, lambda:[action.destroy(),Button_pack()])  
        t.start()
    else:
        player = tkvideo("C:/ATC/Temperature_200.mp4", my_label, loop = 0, size = (250,400))
        player.play()
        action = Label(root,text = "Setting Temperature, Mode and Timer...",font = ("",10,"italic"))
        t1 = Timer(0.315, action.pack)
        t1.start()
        t = Timer(3, lambda:[action.destroy(),Button_pack()])  
        t.start()
def Open_Door():
    global Open_flag,Curr_State,Open_State
    Open_flag = 1
    Open_State = "Door Opened"
    for widget in root.winfo_children():
        widget.destroy() 
    my_label = Label(root)
    my_label.pack()
    player = tkvideo("C:/ATC/Door_Open.mp4", my_label, loop = 0, size = (710,400))
    player.play()
    action = Label(root,text = "Opening Door...",font = ("",10,"italic"))
    t1 = Timer(0.315, action.pack)
    t1.start()
    t = Timer(2, lambda:[action.destroy(),Button_pack()])  
    t.start()
def Close_Door():
    global Open_flag,Curr_State,Open_State
    Open_flag = 0
    Open_State = "Door Closed"
    for widget in root.winfo_children():
        widget.destroy() 
    my_label = Label(root)
    my_label.pack()
    player = tkvideo("C:/ATC/Door_Close.mp4", my_label, loop = 0, size = (710,400))
    player.play()
    action = Label(root,text = "Closing Door...",font = ("",10,"italic"))
    t1 = Timer(0.315, action.pack)
    t1.start()
    t = Timer(1.5, lambda:[action.destroy(),Button_pack()])  
    t.start()
def Switch_On():
    global Switch_flag,Curr_State
    Switch_flag = 1
    Curr_State = "ON"
    for widget in root.winfo_children():
        widget.destroy() 
    my_label = Label(root)
    my_label.pack()
    player = tkvideo("C:/ATC/Switch_on.mp4", my_label, loop = 0, size = (710,400))
    player.play()
    action = Label(root,text = "Switching On...",font = ("",10,"italic"))
    t1 = Timer(0.315, action.pack)
    t1.start()
    t = Timer(0.95, lambda:[action.destroy(),Button_pack()])  
    t.start()
def Switch_Off():
    global Switch_flag,Curr_State
    Switch_flag = 0
    Curr_State = "OFF"
    for widget in root.winfo_children():
        widget.destroy() 
    my_label = Label(root)
    my_label.pack()
    action = Label(root,text = "Switching Off...",font = ("",10,"italic"))
    t1 = Timer(0.315, action.pack)
    t1.start()
    player = tkvideo("C:/ATC/Switch_off.mp4", my_label, loop = 0, size = (710,400))
    player.play()  
    t = Timer(0.95, lambda:[action.destroy(),Button_pack()])  
    t.start()
root = Tk()
root.title("FSA of an Oven - ATC_002_011_036_120")
root.geometry("800x950")
root.resizable(0,0)
Photos()
L = Label(root,image = img)
L.pack()
root.after(140,Button_pack())
root.mainloop()