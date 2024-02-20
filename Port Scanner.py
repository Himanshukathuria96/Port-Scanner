import tkinter as tk
import tkinter.font as tkFont
import socket
import time
import pyfiglet

def recurringFX():

    t_host = GLineEdit_342.get()   
    t_ip = socket.gethostbyname(t_host)

    start_port = GLineEdit_779.get()
    start_port = int(start_port)
    end_port = GLineEdit_626.get()
    end_port = int(end_port)

    for port in range(start_port, end_port+1):    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((t_ip, port))
        if result ==0:
            return "Port {} is [Open] \n".format(port)
        else:
            continue

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_848=tk.Label(root)
        GLabel_848["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_848["font"] = ft
        GLabel_848["fg"] = "#333333"
        GLabel_848["justify"] = "center"
        GLabel_848["text"] = "Port Scanner"
        GLabel_848.place(x=220,y=10,width=175,height=50)

        GLabel_762=tk.Label(root)
        GLabel_762["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_762["font"] = ft
        GLabel_762["fg"] = "#02050e"
        GLabel_762["justify"] = "center"
        GLabel_762["text"] = "Target"
        GLabel_762.place(x=20,y=110,width=117,height=37)

        global GLineEdit_342
        GLineEdit_342=tk.Entry(root)
        GLineEdit_342["bg"] = "#ebe3e3"
        GLineEdit_342["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        GLineEdit_342["font"] = ft
        GLineEdit_342["fg"] = "#333333"
        GLineEdit_342["justify"] = "center"
        GLineEdit_342["text"] = ""
        GLineEdit_342.place(x=210,y=110,width=300,height=40)

        GLabel_336=tk.Label(root)
        GLabel_336["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_336["font"] = ft
        GLabel_336["fg"] = "#333333"
        GLabel_336["justify"] = "center"
        GLabel_336["text"] = "Ports"
        GLabel_336.place(x=20,y=190,width=117,height=37)
        
        global GLineEdit_779
        GLineEdit_779=tk.Entry(root)
        GLineEdit_779["bg"] = "#ebe3e3"
        GLineEdit_779["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        GLineEdit_779["font"] = ft
        GLineEdit_779["fg"] = "#333333"
        GLineEdit_779["justify"] = "center"
        GLineEdit_779["text"] = ""
        GLineEdit_779.place(x=210,y=190,width=111,height=36)
        
        global GLineEdit_626
        GLineEdit_626=tk.Entry(root)
        GLineEdit_626["bg"] = "#efe8e8"
        GLineEdit_626["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        GLineEdit_626["font"] = ft
        GLineEdit_626["fg"] = "#333333"
        GLineEdit_626["justify"] = "center"
        GLineEdit_626["text"] = ""
        GLineEdit_626.place(x=410,y=190,width=101,height=35)

        GLabel_362=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        GLabel_362["font"] = ft
        GLabel_362["fg"] = "#333333"
        GLabel_362["justify"] = "center"
        GLabel_362["text"] = "-"
        GLabel_362.place(x=330,y=190,width=73,height=38)

        GButton_496=tk.Button(root)
        GButton_496["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=12)
        GButton_496["font"] = ft
        GButton_496["fg"] = "#000000"
        GButton_496["justify"] = "center"
        GButton_496["text"] = "Scan "
        GButton_496.place(x=330,y=260,width=79,height=30)
        GButton_496["command"] = self.GButton_496_command

        GLabel_946=tk.Label(root)
        GLabel_946["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_946["font"] = ft
        GLabel_946["fg"] = "#333333"
        GLabel_946["justify"] = "center"
        GLabel_946["text"] = "Result "
        GLabel_946.place(x=30,y=460,width=117,height=37)

        

    def GButton_496_command(self):
        GMessage_892=tk.Message(root)
        GMessage_892["bg"] = "#eadede"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_892["font"] = ft
        GMessage_892["fg"] = "#333333"
        GMessage_892["justify"] = "center"
        GMessage_892["text"] = recurringFX()
        GMessage_892.place(x=210,y=320,width=300,height=273)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
