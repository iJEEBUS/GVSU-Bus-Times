'''
Created on Jan 8, 2017

@author: rounsifr
'''
from Tkinter import *
import busTimes as b
import time

def run():
	root = Tk()
	next_stop_time = ''
	clock = Label(root, font=('arial', 300, 'bold'),fg='white', bg='blue')
	clock.pack(fill=BOTH, expand=1)

	def update():
		next_stop_time = b.run()
		clock.config(text=next_stop_time)
		clock.after(200, update)

	update()
	root.mainloop()