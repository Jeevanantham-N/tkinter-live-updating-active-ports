import serial.tools.list_ports
import tkinter as tk

class usb_ports_gui:

    def usb_ports(self):
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
        usb_ports_gui.gui(self,list_)
    def gui(self,list_):
        r = tk.Tk()
        r.geometry('600x300')
        r.title('List of usb ports')
        for i in list_:
            print(i)
            tk.Label(r, text=i[0]+str(i[1]), font=("Aerial Bold", 20)).pack()

        r.mainloop()
        usb_ports_gui.usb_ports(self)

def main():
    obj1 = usb_ports_gui()
    obj1.usb_ports()

if __name__ == '__main__':
    main()