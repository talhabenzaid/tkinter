import mysql.connector
from tkinter import *
from tkinter import messagebox
import menu



con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

def fon_menu():
    menu.Liste_menu()

def trouver():
    global con
    global cur
    sql="SELECT login , password FROM users where login =%s and password=%s"
    t=(sai1.get(),sai2.get())
    cur.execute(sql,t)
    l=cur.fetchall()
    r=cur.rowcount
    if r>0:
        window.destroy()
        fon_menu()
    else:
        messagebox.showerror("Error","Mot de passe incorrect")


window=Tk()
window.title("connecter")
window.geometry("280x150")



lbl1=Label(window,text="Utilisateur")
lbl1.place(x=30,y=30)

var_sai1=StringVar()
sai1=Entry(window,textvariable=var_sai1)
sai1.place(x=130,y=30)

lbl2=Label(window,text="Mot de passe")
lbl2.place(x=30,y=60)

var_sai2=StringVar()
sai2=Entry(window,textvariable=var_sai2,show="*")
sai2.place(x=130,y=60)

btn1=Button(window,text="Connexion",command=trouver)
btn1.place(x=190,y=100)

btn2=Button(window,text="Quitter",command=quit)
btn2.place(x=40,y=100)

window.resizable(False,False)
window.mainloop()