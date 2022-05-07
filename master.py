from tkinter import *
import os
from tkinter import  messagebox



RHG=Tk()


width_of_window = 320
height_of_window = 210
screen_width = RHG.winfo_screenwidth()
screen_height = RHG.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
RHG.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
RHG.config(bg="black")
RHG.overrideredirect(1)

image10=PhotoImage(file="IMG/master1.png")
Label(RHG,image=image10,bd=0,bg="#fff").place(x=10,y=10)

def main_window():
             RHG.destroy()
             os.system('python3 minu.py')


RHG.after(3000, main_window)

RHG.mainloop()

