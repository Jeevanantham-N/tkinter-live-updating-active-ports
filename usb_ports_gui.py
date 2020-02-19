import serial.tools.list_ports
import tkinter as tk
from tkinter import *

class usb_ports_gui:

    @staticmethod
    def linux_Function_call():
        usb_ports_gui.linux_usb_ports("self")
    @staticmethod
    def window_Function_call():
        usb_ports_gui.window_usb_ports("self")

    def window_usb_ports(self):
        global usb_ports
        usb_ports = []
        for port in serial.tools.list_ports.comports():
            port_ = str(port)
            list_ = port_.split(" ")
            concat = ""
            for i in range(2, len(list_) - 1):
                concat = concat + list_[i] + " "
            usb_ports.append([list_[0], concat])
        usb_list = []
        usb_ports = [['COM1', 'Communications Port ']]
        for i in usb_ports:
            usb_list.append([i[0] + "  " + i[1], i[1].split(" ")[0]])
        print(usb_list)
        usb_ports_gui.usb_port_count(self,usb_list)
    def linux_usb_ports(self):
        global usb_ports
        usb_ports = []
        for port in serial.tools.list_ports.comports():
            port_ = str(port)
            list_= port_.split(" ")
            concat = ""
            for i in range(2,len(list_)):
                concat = concat+list_[i]+" "
            string = list_[0][slice(5, len(list_[0]))] + "  " + concat
            usb_ports.append([string,string.split(" ")[2]])
        print(usb_ports)
        usb_ports_gui.usb_port_count(self,usb_ports)

    def usb_port_count(self,usb_ports):
        ignore = []
        count = 0
        list_ = []
        for i in range(0, len(usb_ports)):
            com1 = usb_ports[i][1]
            for j in range(i,len(usb_ports)):
                com2 = usb_ports[j][1]
                if j not in ignore:
                    if com1 == com2:
                        ignore.append(j)
                        count +=1
            if count != 0:
                list_.append([usb_ports[i][0],count])
            count = 0
        print(list_)
        usb_ports_gui.gui(self,list_)

    def gui(self,list_):
        r = tk.Tk()
        r.geometry('700x300')
        r.title('List of usb ports')
        btn = Button(r,text = "refresh",command =usb_ports_gui.linux_Function_call).pack()
        text_ = 'Total usb devices count   :'+str(len(usb_ports))
        tk.Label(r, text=text_, font=("Aerial Bold", 20)).pack()
        for i in list_:
            split_ = i[0].split(" ")
            text_ = 'id  :'+split_[0]+',  usb device:   '+split_[2]+',  count   :'+str(i[1])
            print(text_)
            tk.Label(r, text=text_, font=("Aerial Bold", 20)).pack()
        r.mainloop()

def main():
    obj1 = usb_ports_gui()
    obj1.window_usb_ports()

if __name__ == '__main__':
    main()