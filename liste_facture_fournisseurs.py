from tkinter import *
from tkinter import ttk 
import mysql.connector
from functools import partial
from tkinter import messagebox

con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

class Facture_fournisseurs(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("760x370")
        self.title("Facture fourniseur")
        self.resizable(False,False)

        self.frame1=Frame(self,bg="light blue")
        self.frame1.place(x=0,y=0,width=760,height=60)  

        self.btn1=Button(self.frame1,text="Nouveau",bg="black",fg="white",command=partial(self.window,""))
        self.btn1.place(x=40,y=15,width=100)

        self.btn2=Button(self.frame1,text="Modifier",bg="black",fg="white",command=partial(self.window,"Modifier"))
        self.btn2.place(x=240,y=15,width=100)

        self.btn3=Button(self.frame1,text="Supprime",bg="black",fg="white")
        self.btn3.place(x=440,y=15,width=100)

        self.btn4=Button(self.frame1,text="Quit",bg="black",fg="white",command=quit)
        self.btn4.place(x=630,y=15,width=100)
        
        self.frame2=Frame(self)
        self.frame2.place(x=0,y=60,width=760,height=310)
        
        self.tv=ttk.Treeview(self.frame2,columns=(1,2,3,4,5),show="headings")
        self.tv.heading(1,text="Facture N°")
        self.tv.heading(2,text="Date")
        self.tv.heading(3,text="Fournisseur")
        self.tv.heading(4,text="Nom")
        self.tv.heading(5,text="Montant")

        self.tv.column(1,width=10)
        self.tv.column(2,width=100)
        self.tv.column(3,width=100)
        self.tv.column(4,width=100)
        self.tv.column(5,width=100)

        self.tv.place(x=0,y=0,width=760,height=310)

    def rempl(self):
        global con
        global cur
        sql="SELECT detai_facture.id_facture,facture_fournisseur.date,facture_fournisseur.id_fournisseur,fournisseur.nom_fournisseur,SUM(detai_facture.QTE*detai_facture.prix) FROM detai_facture,facture_fournisseur,fournisseur WHERE detai_facture.id_facture=facture_fournisseur.id_facture_fournisseur AND facture_fournisseur.id_fournisseur=fournisseur.id_fournisseur GROUP by detai_facture.id_facture,facture_fournisseur.date,facture_fournisseur.id_fournisseur,fournisseur.nom_fournisseur"    
        cur=con.cursor()
        cur.execute(sql)
        l=cur.fetchall()
        i=1
        for e in l:
            self.tv.insert(parent="",index=i,values=(e))
            i+=1

    def window(self,n):
        self.winf=Toplevel()
        self.winf.geometry("760x370")
        self.winf.title("Facture fournisseur")
        self.winf.resizable(False,False)

        self.frame3=Frame(self.winf,bg="gray")
        self.frame3.place(x=0,y=30,width=760,height=80)

        self.lblidf=Label(self.frame3,text="Facture N°",bg="gray",fg="white")
        self.lblidf.place(x=30,y=10)

        self.var_saiidf=StringVar()
        self.saiidf=Entry(self.frame3,textvariable=self.var_saiidf)
        self.saiidf.place(x=100,y=10,width=80,height=20)

        self.lbldate=Label(self.frame3,text="Date",bg="gray",fg="white")
        self.lbldate.place(x=260,y=10)

        self.var_saidate=StringVar()
        self.saidate=Entry(self.frame3,textvariable=self.var_saidate)
        self.saidate.place(x=330,y=10,width=130,height=20)

        self.lblfour=Label(self.frame3,text="Fournisseur",bg="gray",fg="white")
        self.lblfour.place(x=30,y=50)

        self.var_saifour=StringVar()
        self.saifour=Entry(self.frame3,textvariable=self.var_saifour)
        self.saifour.place(x=100,y=50,width=80,height=20)

        self.btnfou=Button(self.frame3,text="...",bg="black",fg="white",command=self.recherche_fou)
        self.btnfou.place(x=185,y=50,width=20,height=20)

        self.lblnom=Label(self.frame3,text="Nom",bg="gray",fg="white")
        self.lblnom.place(x=260,y=50)

        self.var_sainom=StringVar()
        self.sainom=Entry(self.frame3,textvariable=self.var_sainom)
        self.sainom.place(x=330,y=50,width=130,height=20)

        self.frame4=Frame(self.winf,bg="light blue")
        self.frame4.place(x=0,y=110,width=760,height=70) 

        self.lblref=Label(self.frame4,text="Reference",bg="light blue",fg="black")
        self.lblref.place(x=30,y=10)

        self.var_sairef=StringVar()
        self.sairef=Entry(self.frame4,textvariable=self.var_sairef)
        self.sairef.place(x=100,y=10,width=80,height=20)

        self.btn2=Button(self.frame4,text="...",bg="black",fg="white",command=self.ajouter_art)
        self.btn2.place(x=185,y=10,width=20,height=20)


        self.lbldes=Label(self.frame4,text="Designation",bg="light blue",fg="black")
        self.lbldes.place(x=250,y=10)

        self.var_saides=StringVar()
        self.saides=Entry(self.frame4,textvariable=self.var_saides)
        self.saides.place(x=330,y=10,width=80,height=20)

        self.lblpu=Label(self.frame4,text="PU",bg="light blue",fg="black")
        self.lblpu.place(x=430,y=10)

        self.var_saipu=StringVar()
        self.saipu=Entry(self.frame4,textvariable=self.var_saipu)
        self.saipu.place(x=470,y=10,width=80,height=20)

        self.lblqte=Label(self.frame4,text="QTE",bg="light blue",fg="black")
        self.lblqte.place(x=600,y=10)

        self.btn3=Button(self.frame4,text="...",bg="black",fg="white",command=self.calcu_mantant)
        self.btn3.place(x=725,y=10,width=20,height=20)

        self.var_saiqte=StringVar()
        self.saiqte=Entry(self.frame4,textvariable=self.var_saiqte)
        self.saiqte.place(x=640,y=10,width=80,height=20)

        self.lblmon=Label(self.frame4,text="Montant",bg="light blue",fg="black")
        self.lblmon.place(x=500,y=40)

        self.var_saimon=StringVar()
        self.saimon=Entry(self.frame4,textvariable=self.var_saimon)
        self.saimon.place(x=560,y=40,width=80,height=20)

        self.btnajou2=Button(self.frame4,text="Ajouter",bg="black",fg="white",command=self.rempl2)
        self.btnajou2.place(x=660,y=40,width=80,height=20)

        self.frame5=Frame(self.winf,bg="black")
        self.frame5.place(x=0,y=0,width=760,height=30)

        self.frame6=Frame(self.winf)
        self.frame6.place(x=0,y=180,width=760,height=220)
        
        self.tv=ttk.Treeview(self.frame6,columns=(1,2,3,4,5),show="headings")
        self.tv.heading(1,text="Reference")
        self.tv.heading(2,text="Designation")
        self.tv.heading(3,text="PU")
        self.tv.heading(4,text="QTE")
        self.tv.heading(5,text="Montant")

        self.tv.column(1,width=10)
        self.tv.column(2,width=100)
        self.tv.column(3,width=100)
        self.tv.column(4,width=100)
        self.tv.column(5,width=100)

        self.tv.place(x=0,y=0,width=760,height=220)

        if n=="":
            self.btn6=Button(self.frame5,text="Enregister",bg="white",fg="black",command=self.ener_nov)
            self.btn6.place(x=30,y=6,width=80,height=20)

            


    def ener_nov(self):
        global con
        global cur
        sql="INSERT INTO facture_fournisseur(id_facture_fournisseur, date, id_fournisseur) VALUES (%s,%s,%s)"
        t=(self.var_saiidf.get(),self.var_saidate.get(),self.var_saifour.get())
        cur=con.cursor()
        cur.execute(sql,t)
        con.commit()

        select=self.tv.focus()
        self.el=self.tv.item(select,"values")
        print(len(self.el))
        i=1
    
        for item in self.el:
            data = self.tv.item(item)
            d=list(data.values())
        

        while i<=len(self.el):
            sql2="INSERT INTO detai_facture (id_facture, id_article, QTE, prix) VALUES (%s,%s,%s,%s)"
            t2=(self.var_saiidf.get(),self.el[0],int(self.el[3]),float(self.el[2]))
            cur2=con.cursor()
            cur2.execute(sql2,t2)
            con.commit()
            print(self.var_saiidf.get())
            print(self.el[0])
            print(self.el[3])
            print(self.el[2])
            i=+1


        




    def calcu_mantant(self):
        if self.var_saiqte.get()=="":
            messagebox.showerror("Error","QTE est vide")
        elif self.var_saipu.get()=="":
            messagebox.showerror("Error","PU est vide")    
        else:
            self.var_saimon.set(float(self.var_saipu.get())*int(self.var_saiqte.get()))

    def recherche_fou(self):
        global con
        global cur
        sql="SELECT nom_fournisseur FROM fournisseur WHERE id_fournisseur=%s"
        t=(self.var_saifour.get(),)
        cur.execute(sql,t)
        l=cur.fetchall()
        for e in l:
            self.var_sainom.set(e)  
        if len(l)==0 and self.var_saifour.get()!="":
            messagebox.showerror("Error","Fournisseur n'existe pas")
        if self.saifour.get()=="":
            self.var_sainom.set("")        

    def ajouter_art(self):
        global con
        global cur
        sql="SELECT designation, prix_venter FROM article WHERE id_article=%s"
        t=(self.var_sairef.get(),)
        cur.execute(sql,t)
        l=cur.fetchall()
        for e in l:
            self.var_saides.set(e[0])
            self.var_saipu.set(float(e[1]))
        if len(l)==0 and self.var_sairef.get()!="":
            messagebox.showerror("Error","article n'existe pas")
        if self.sairef.get()=="":
            self.var_saides.set("")
            self.var_saipu.set("")

    def rempl2(self):
        l=(self.var_sairef.get(),self.var_saides.get(),self.var_saipu.get(),self.var_saiqte.get(),self.var_saimon.get())
        self.tv.insert(parent="",index=1,values=(l))                

       
     
    
        

