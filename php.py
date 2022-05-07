from tkinter import *
import os
import sys
import time

ngrok = Tk()
ngrok.title("FACEBOOK SERVER")
ngrok.geometry("260x300")
ngrok.config(bg="white")

button_mode1=True

def hellong():

    fileng=Filenameng1.get()
    rhgng=Filenameng4.get()
    pathng=Filenameng2.get()
    os.system('xterm -bg black -fg red -hold -e '+"php -S"+' '+str(fileng+":"+pathng+' '+rhgng+'&'))


def ngrok2():
    os.system('python3 ngrok.py &')

def python():
   os.system('python3 server.py &')

def ssh():
   os.system('python3 ssh.py &')

def php():

   os.system('python3 php.py &')


host1=Label(ngrok,text="HOST:",bg="#fff",font="Arial 9 bold")
host1.place(x=10,y=100)

Filenameng1=StringVar()
HOST1=Entry(ngrok,textvariable=Filenameng1,width=18,font="arial 9")
HOST1.place(x=70,y=100)
Filenameng1.set("localhost")


port1=Label(ngrok,text="PORT:",bg="#fff",font="Arial 9 bold")
port1.place(x=10,y=130)

Filenameng2=StringVar()
PORT1=Entry(ngrok,textvariable=Filenameng2,width=18,font="arial 9")
PORT1.place(x=70,y=130)
Filenameng2.set("8080")


path1=Label(ngrok,text="PATH:",bg="#fff",font="Arial 9 bold")
path1.place(x=10,y=160)

Filenameng4=StringVar()
PHP=Entry(ngrok,textvariable=Filenameng4,width=18,font="arial 9")
PHP.place(x=70,y=160)
Filenameng4.set("")



B11 = Button(ngrok,bg="#DC143C", text = "STOP", font="Arial 10 bold",command = hellong)
B11.place(x = 20,y = 265)


B11 = Button(ngrok,bg="#34A56F", text = "START",font="Arial 10 bold",command = hellong)
B11.place(x = 170,y = 265)


ngrok1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "NGROK", command = ngrok2)
ngrok1.place(x = 30,y = 10)


python1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "PYTHON", command = python)
python1.place(x = 90,y = 10)

ssh1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "SSH", command = ssh)
ssh1.place(x = 150,y = 10)

php1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "PHP", command = php)
php1.place(x = 190,y = 10)


ngrok.mainloop()
