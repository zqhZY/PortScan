
import Tkinter

from GUI_modle import *

import socket
import sys , os
import threading
import string

Entry = {}


def Scan_bt():

	host = Entry['Domain'].get()
	ip = socket.gethostbyname(host)

	if Entry['IP'].get() == '':
		Entry['IP'].insert(0 , ip)
	else:
		ip = Entry['IP'].get()
		
	
	th_num = string.atoi(Entry['th_num'].get())
	p_start = string.atoi(Entry['start'].get())	
	p_end = string.atoi(Entry['end'].get())

	len_to_scan = p_end - p_start + 1
	ave = len_to_scan/th_num
	print ave

	for x in xrange( 0 , th_num):
		start = p_start + x*ave        
                if x != th_num - 1:
                    end = p_start + (x+1)*ave 
                else:
                    end = p_end + 1
                th = Port_Scan(ip , start , end)
                th.start()


#tkroot
root = Tkinter.Tk()
root.title("zqh")
root.geometry('350x200')

#top frame
frm_top = TkFrame(root , side = Tkinter.TOP)

frm_top.C_Lable(text = "START")
Entry['start'] = frm_top.C_Entry(defaltevalue = 1)
frm_top.C_Lable(text = "END")
Entry['end'] = frm_top.C_Entry(defaltevalue = 80)
frm_top.C_Lable(text = "Thread num")
Entry['th_num'] = frm_top.C_Entry(defaltevalue = 10)
frm_top.C_Button(text = "Scan" , side = Tkinter.BOTTOM  , command = Scan_bt)


#center frame
frm_center = TkFrame(root , side = Tkinter.TOP)
frm_center.C_Lable(text = "Domain")
Entry['Domain'] = frm_center.C_Entry(width = 18 , defaltevalue = 'www.justzqh.com')
frm_center.C_Lable(text = "IP")
Entry['IP'] = frm_center.C_Entry(width = 18)


frm_center2 = TkFrame(root , Tkinter.TOP)
frm_center2.C_Lable(text = "Rsult")
Entry['Rsult'] = frm_center2.C_Entry(width = 30 )


#bottom frame
frm_bottom = TkFrame(root , side = Tkinter.TOP)
scrollbar = frm_bottom.C_Scrollbar(side = Tkinter.RIGHT)
Entry['mylist'] = frm_bottom.C_Listbox(scrollbar = scrollbar)


def port_ping(ip , port):
    try:

        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)#ipv4 , tcp
        #print 'Socket Create'
        s.connect((ip , port))
        #print 'Socket Connected to ' + host + ' on ip ' + ip
        Entry['Rsult'].insert(Tkinter.END, str(port) + ' is open ') 

    except socket.error:
    	Entry['mylist'].insert(Tkinter.END, str(port) + ' is not open ')
        
    
    s.close()


class Port_Scan(threading.Thread):
    def __init__(self , ip , p_start , p_end):
        threading.Thread.__init__(self)
        self.ip = ip
        self.p_start = p_start
        self.p_end  = p_end
    
    def run(self):
        #threadname = threading.currentThread().getName()
        #print 'in sthread : ' + threadname
        
        for i in xrange(self.p_start , self.p_end ):
            port_ping(self.ip , i)
            
        #threadname = threading.currentThread().getName()
        #print threadname + 'has finished work'
        #Entry['mylist'].insert(Tkinter.END, threadname + ' finished!')


if __name__ == '__main__':
    
    root.mainloop()

    