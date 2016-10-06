# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:02:05 2016

@author: jog
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from Tkinter import *
from tkFileDialog import askopenfilename
top = Tk()
top.minsize(width=350,height=100)
top.wm_title("Mobile Pay to Conventus Converter")
var = StringVar()
label = Label(top,textvariable = var,relief=RAISED)
def converter(inname,outname):
    f = open(inname, 'r')
    output = open(outname,'w')
    counter = 0
    stringlist = []
    resList=[]

    for line in f:
        stringlist.append(line.split(';'))

    for i in range(len(stringlist)-3): #3 fordi vi undgaa de første 2 linier og sum linien
        outstring = stringlist[2+i][3][1:] +"; 2004; " + stringlist[2+i][0] + "  " + stringlist[2+i][6] + "; 1; 7380;;;;2;1;3010;;;;2;" +stringlist[2+i][2] +"\n"
        output.write(outstring)

    f.close()
    output.close()

def loadButton():
    global filename
    filename = askopenfilename()
    var.set(filename + " Loaded!")


def saveButton():
    converter(filename,E1.get() + '.csv')
    var.set("Saved as " + E1.get() + ".csv")

Load = Button(top,text = "Load File", command = loadButton)
Save = Button(top,text = "Save File", command = saveButton)



Load.pack()
Save.pack()
label.pack()
L1 = Label(top, text="Save File Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

top.mainloop()
#for line in f:
#    if line[0] == ' ':
#        output.write(line[1:])

#Dato;2004;Navn;1;7380;;;;2;1;3010;;;2;Beløb
