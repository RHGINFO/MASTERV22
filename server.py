from tkinter import *
import time
import os

root = Tk()
root.title("FACEBOOK SERVER")
root.geometry("260x300")
root.config(bg="white")


button_mode=True

def hello():
    file=Filename.get()
    rhg=Filename1.get()
    path=Filename2.get()
    os.system ('xterm -bg black -fg red -hold -e'+' '+"python3 -m "+str(file+" "+rhg+' '+'-d'+' '+path +'&'))


def ngrok():
    
    os.system('python3 ngrok.py&')
    
def python():
    os.system('python3 server.py&')

def ssh():
   os.system('python3 ssh.py&')

def php():
   os.system('python3 php.py&')

def hell():
    exit()

host=Label(root,text="HOST:",bg="#fff",font="Arial 9 bold")
host.place(x=10,y=100)

Filename=StringVar()
HOST=Entry(root,textvariable=Filename,width=18,font="arial 9")
HOST.place(x=70,y=100)
Filename.set("http.server")


port=Label(root,text="PORT:",bg="#fff",font="Arial 9 bold")
port.place(x=10,y=130)

Filename1=StringVar()
PORT=Entry(root,textvariable=Filename1,width=18,font="arial 9")
PORT.place(x=70,y=130)
Filename1.set("8080")



path=Label(root,text="PATH:",bg="#fff",font="Arial 9 bold")
path.place(x=10,y=160)

Filename2=StringVar()
PATH=Entry(root,textvariable=Filename2,width=18,font="arial 9")
PATH.place(x=70,y=160)
Filename2.set("/login/")


B1 = Button(root,bg="#DC143C", text = "STOP", font="Arial 10 bold",command =hell)
B1.place(x = 20,y = 265)


B1 = Button(root,bg="#34A56F", text = "START",font="Arial 10 bold",command =hello)
B1.place(x = 170,y = 265)


ngrok = Button(root,bg="#fff",font="Arial 7 bold" ,text = "NGROK", command =ngrok)
ngrok.place(x = 30,y = 10)


python = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PYTHON", command =python)
python.place(x = 90,y = 10)

ssh = Button(root,bg="#fff",font="Arial 7 bold" ,text = "SSH", command =ssh)
ssh.place(x = 150,y = 10)

php = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PHP", command =php)
php.place(x = 190,y = 10)

root.mainloop()
