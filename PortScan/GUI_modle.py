#GUI  class
 
import Tkinter
import socket
import sys , os
import threading
import string

class TkFrame(Tkinter.Frame):
	"""docstring for TkFrame"""
	def __init__(self, master = None , side = None):
		Tkinter.Frame.__init__(self , master)
		self.pack(side = side)

	def C_Entry(self , width = 5 , side = Tkinter.LEFT , defaltevalue = ''):
		entry = Tkinter.Entry(self , width = width );
		entry.insert(0 , defaltevalue)
		entry.pack(side = side)
		return entry

	def C_Lable(self , text = None , side = Tkinter.LEFT):
		lable = Tkinter.Label(self , text = text)
		lable.pack(side = side)
		return lable

	def C_Button(self , text = "button" , command = None , side = Tkinter.LEFT):
		button = Tkinter.Button(self , text = text , command = command)
		button.pack(side = side)
		return button

	def C_Scrollbar(self , side = Tkinter.LEFT , fill = Tkinter.Y):
		scrollbar = Tkinter.Scrollbar(self)
		scrollbar.pack(side = side , fill = fill)
		return scrollbar

	def C_Listbox(self , side = Tkinter.LEFT , fill = Tkinter.BOTH , scrollbar = None):
		mylist = Tkinter.Listbox(self , yscrollcommand = scrollbar.set)
		mylist.pack(side = side , fill = fill)
		return mylist
