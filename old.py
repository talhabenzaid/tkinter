from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

def afficher(event):
    s=tv.selection()
    l=tv.item(s)["values"]
    print(l)

def comp():
        global con
        global cur
        sql="SELECT code,nom, ville FROM client "
        cur=con.cursor()
        cur.execute(sql)
        l=cur.fetchall()
        for e in l:
            tv.insert("",END,values=e)

def ouvrir():
    root=Toplevel()
    root.title("Client")
    root.geometry("210x140")
    root.resizable(False,False)
    
    lblid=Label(root,text="Id")
    lblid.place(x=20,y=10)

    var_saiid=StringVar()
    saiid=Entry(root,textvariable=var_saiid)
    saiid.place(x=80,y=10)
    
    var_saiid.set(afficher[0])

    lblnom=Label(root,text="Nom")
    lblnom.place(x=20,y=50)

    var_sainom=StringVar()
    sainom=Entry(root,textvariable=var_sainom)
    sainom.place(x=80,y=50) 

    lblvil=Label(root,text="Ville")
    lblvil.place(x=20,y=90)

    var_saivil=StringVar()
    saivil=Entry(root,textvariable=var_saivil)
    saivil.place(x=80,y=90)          


window=Tk()
window.geometry("600x500")
window.resizable(False,False)

fram1=Frame(window,bg="lightgray")
fram1.place(x=0,y=0,width=600,height=40)

btnnou=Button(fram1,text="Nouveau",bg="gray",fg="white")
btnnou.place(x=10,y=5,width=100,height=30)

btnouv=Button(fram1,text="Ouvrir",bg="gray",fg="white",command=ouvrir)
btnouv.place(x=170,y=5,width=100,height=30)

btnsup=Button(fram1,text="Supprime",bg="gray",fg="white")
btnsup.place(x=330,y=5,width=100,height=30)

btnfer=Button(fram1,text="Ferme",bg="gray",fg="white")
btnfer.place(x=490,y=5,width=100,height=30)

fram2=Frame(window,bg="darkgrey")
fram2.place(x=0,y=40,width=200,height=460)

lblcod=Label(fram2,text="Code",bg="darkgrey")
lblcod.place(x=80,y=10,width=40)

var_saicod=StringVar()
saicod=Entry(fram2,textvariable=var_saicod)
saicod.place(x=20,y=40,width=160)

lblnom=Label(fram2,text="Nom",bg="darkgrey")
lblnom.place(x=80,y=90,width=40)

var_sainom=StringVar()
sainom=Entry(fram2,textvariable=var_sainom)
sainom.place(x=20,y=120,width=160)

lblvil=Label(fram2,text="Ville",bg="darkgrey")
lblvil.place(x=80,y=170,width=40)

var_saivil=StringVar()
saivil=Entry(fram2,textvariable=var_saivil)
saivil.place(x=20,y=200,width=160)

btnrech=Button(fram2,text="Recherge",bg="lightgray")
btnrech.place(x=55,y=250,width=100,height=30)

fram3=Frame(window)
fram3.place(x=200,y=40,width=400,height=460)

tv=ttk.Treeview(fram3,columns=("numero","nom","ville"),show="headings")

tv.column("numero",width=80)
tv.column("nom",width=100)
tv.column("ville",width=100)

tv.heading("numero",text="Numero")
tv.heading("nom",text="Nom")
tv.heading("ville",text="Ville")


tv.bind("<<TreeviewSelect>>",afficher)

tv.place(x=0,y=0,width=400,height=460)



comp()
window.mainloop()