'''
Created on Jan 8, 2017

@author: rounsifr
'''
from Tkinter import *
from com.gvsubusroutes import BusArrival
from numpy.core.defchararray import title


## MAIN WINDOW
root = Tk()                             

## VARIABLES
time = BusArrival.nextarrival('Trio')

## BACKGROUND IMAGE
background_image = PhotoImage('/home/rounsifr/pi/background5')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

## TITLE
root.title("GVSU Bus Arrival Times")

## LABELS
triolbl = Label(root, text="Trio")
triolbl.grid(row=0,column=0)
label_trio = Label(root, text=BusArrival.nextarrival('Trio'))
label_trio.grid(row=0,column=1)

triolbl = Label(root, text="Copper")
triolbl.grid(row=1,column=0)
label_trio = Label(root, text=BusArrival.nextarrival('Copper'))
label_trio.grid(row=1,column=1)

triolbl = Label(root, text="Pierce")
triolbl.grid(row=2,column=0)
label_trio = Label(root, text=BusArrival.nextarrival('Pierce'))
label_trio.grid(row=2,column=1)





root.mainloop()