from tkinter import *
from tkinter import ttk 
import mysql.connector
from functools import partial
from tkinter import messagebox

con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

class liste_fournisseur(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("760x370")
        self.title("Fournisseurs")
        self.resizable(False,False)

        self.frame1=Frame(self,bg="light blue")
        self.frame1.place(x=0,y=0,width=200,height=370)

        self.btn_rech=Button(self.frame1,text="Recherche",bg="gray",fg="white",command=self.recherche)
        self.btn_rech.place(x=0,y=0,width=200,height=50)
        
        self.lblid=Label(self.frame1,text="ID",bg="black",fg="white")
        self.lblid.place(x=40,y=70,width=100,height=20)
        
        self.var_saiid=StringVar()
        self.saiid=Entry(self.frame1,textvariable=self.var_saiid,bg="gray",fg="white")
        self.saiid.place(x=20,y=100,width=140,height=20)
        
        self.lblnom=Label(self.frame1,text="Nom",bg="black",fg="white")
        self.lblnom.place(x=40,y=130,width=100,height=20)
        
        self.var_sainom=StringVar()
        self.sainom=Entry(self.frame1,textvariable=self.var_sainom,bg="gray",fg="white")
        self.sainom.place(x=20,y=160,width=140,height=20)
        
        self.lblville=Label(self.frame1,text="Ville",bg="black",fg="white")
        self.lblville.place(x=40,y=190,width=100,height=20)
        
        self.var_saiville=StringVar()
        self.saiville=Entry(self.frame1,textvariable=self.var_saiville,bg="gray",fg="white")
        self.saiville.place(x=20,y=220,width=140,height=20)
        
        self.lbltele=Label(self.frame1,text="Télephone",bg="black",fg="white")
        self.lbltele.place(x=40,y=250,width=100,height=20)
        
        self.var_saitele=StringVar()
        self.saitele=Entry(self.frame1,textvariable=self.var_saitele,bg="gray",fg="white")
        self.saitele.place(x=20,y=280,width=140,height=20)

        self.lblema=Label(self.frame1,text="Email",bg="black",fg="white")
        self.lblema.place(x=40,y=310,width=100,height=20)
        
        self.var_saiema=StringVar()
        self.saiema=Entry(self.frame1,textvariable=self.var_saiema,bg="gray",fg="white")
        self.saiema.place(x=20,y=340,width=140,height=20)

        self.frame2=Frame(self,bg="light blue")
        self.frame2.place(x=200,y=0,width=600,height=50)
        
        self.btn1=Button(self.frame2,text="Nouveau",bg="black",fg="white",command=partial(self.window,"nouveau"))
        self.btn1.place(x=10,y=10,width=100,height=30)
        
        self.btn2=Button(self.frame2,text="Modifier",bg="black",fg="white",command=partial(self.window,"modifier"))
        self.btn2.place(x=120,y=10,width=100,height=30)
        
        self.btn3=Button(self.frame2,text="Supprime",bg="black",fg="white",command=partial(self.window,"Supprime"))
        self.btn3.place(x=230,y=10,width=100,height=30)
        
        self.btn4=Button(self.frame2,text="Imprimer",bg="black",fg="white")
        self.btn4.place(x=340,y=10,width=100,height=30)
        
        self.btn5=Button(self.frame2,text="Ferme",bg="black",fg="white",command=quit)
        self.btn5.place(x=450,y=10,width=100,height=30)

        self.frame3=Frame(self)
        self.frame3.place(x=200,y=50,width=600,height=370)
        
        self.tv=ttk.Treeview(self.frame3,columns=(1,2,3,4,5),show="headings")
        self.tv.heading(1,text="ID")
        self.tv.heading(2,text="Nom")
        self.tv.heading(3,text="Ville")
        self.tv.heading(4,text="Télephone")
        self.tv.heading(5,text="Email")

        self.tv.column(1,width=10)
        self.tv.column(2,width=100)
        self.tv.column(3,width=100)
        self.tv.column(4,width=100)
        self.tv.column(5,width=100)

        self.tv.place(x=0,y=0,width=560,height=500)

    def rempl(self):
        global con
        global cur
        sql="SELECT id_fournisseur, nom, tel, ville, email FROM fournisseur"
        cur=con.cursor()
        cur.execute(sql)
        l=cur.fetchall()
        i=1
        for e in l:
            self.tv.insert(parent="",index=i,values=(e))
            i+=1

    def supprime_tout(self):
        for i in self.tv.get_children():
            self.tv.delete(i)        

    def recherche(self):
        global con
        global cur
        if self.var_saiid.get()!="":
            sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE id_fournisseur=%s"
            t=(self.var_saiid.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","Fournisseur n'existe pas")
            for e  in l:
                nom=True
                ville=True
                tele=True
                ema=True
                if self.var_sainom.get()!="":
                    nom=False
                    if e[1]==self.var_sainom.get():
                        nom=True
                if self.var_saiville.get()!="":
                    ville=False
                    if e[2]==self.var_saiville.get():
                        ville=True
                if self.var_saitele.get()!="":
                    tele=False
                    if e[3]==self.var_saitele.get():
                        tele=True
                if self.var_saiema.get()!="":
                    ema=False
                    if e[4]==self.var_sainom.get():
                        ema=True                        
                if nom==True and ville==True and tele==True and ema==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showinfo("Info","Fournisseur n'existe pas")   
        elif self.var_sainom.get()!="":
            sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE nom_fournisseur=%s "
            t=(self.var_sainom.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","Fourniseur n'existe pas")
            for e  in l:
                ville=True
                tele=True
                ema=True
                if self.var_saiville.get()!="":
                    ville=False
                    if e[2]==self.var_saiville.get():
                        ville=True
                if self.var_saitele.get()!="":
                    tele=False
                    if e[3]==self.var_saitele.get():
                        tele=True
                if self.var_saiema.get()!="":
                    ema=False
                    if e[4]==self.var_sainom.get():
                        ema=True                        
                if ville==True and tele==True and ema==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showinfo("Info","Fournisseur n'existe pas")     
        elif self.var_saiville.get()!="":
            sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE ville=%s  "
            t=(self.var_saiville.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","Fournisseur n'existe pas")
            for e  in l:
                tele=True
                ema=True
                if self.var_saitele.get()!="":
                    tele=False
                    if e[3]==self.var_saitele.get():
                        tele=True
                if self.var_saiema.get()!="":
                    ema=False
                    if e[4]==self.var_sainom.get():
                        ema=True                        
                if tele==True and ema==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showinfo("Info","Fournisseur n'existe pas")     
        elif self.var_saitele.get()!="":
            sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE tel=%s  "
            t=(self.var_saitele.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","Fournisseur n'existe pas")
            for e  in l:
                ema=True
                if self.var_saiema.get()!="":
                    ema=False
                    if e[4]==self.var_sainom.get():
                        ema=True                        
                if ema==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showinfo("Info","Fournisseur n'existe pas")     
        elif self.var_saiema.get()!="":
            sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE email=%s   "
            t=(self.var_saiema.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","Fournisseur n'existe pas")
            for e  in l:
                self.supprime_tout()
                self.tv.insert(parent="",index=0,values=(e))
        else:
            self.supprime_tout()
            self.rempl() 

    def window(self,n):
        self.winf=Toplevel()
        self.winf.title("Fournisseur")
        self.winf.geometry("300x170")
        self.winf.resizable(False,False)
       

        self.lblnom=Label(self.winf,text="Nom")
        self.lblnom.place(x=20,y=10)

        self.var_sainom=StringVar()
        self.sainom=Entry(self.winf,textvariable=self.var_sainom)
        self.sainom.place(x=120,y=10)

        self.lblville=Label(self.winf,text="Ville")
        self.lblville.place(x=20,y=40)

        self.var_saiville=StringVar()
        self.saiville=Entry(self.winf,textvariable=self.var_saiville)
        self.saiville.place(x=120,y=40)

        self.lbltele=Label(self.winf,text="Télephone")
        self.lbltele.place(x=20,y=70)

        self.var_saitele=StringVar()
        self.saitele=Entry(self.winf,textvariable=self.var_saitele)
        self.saitele.place(x=120,y=70)

        self.lblemail=Label(self.winf,text="Email")
        self.lblemail.place(x=20,y=100)

        self.var_saiemail=StringVar()
        self.saiemail=Entry(self.winf,textvariable=self.var_saiemail)
        self.saiemail.place(x=120,y=100)

        self.btn1=Button(self.winf,text="Quitter",command=quit)
        self.btn1.place(x=20,y=130)

        if n=="modifier":
            select=self.tv.focus()
            self.el=self.tv.item(select,"values")

            self.var_saiid.set(self.el[0])
            self.var_sainom.set(self.el[1])
            self.var_saiville.set(self.el[2])
            self.var_saitele.set(self.el[3])
            self.var_saiemail.set(self.el[4])

            self.btn2=Button(self.winf,text="Modifier",command=self.modifier)
            self.btn2.place(x=230,y=130)
            

        elif n=="nouveau":
            self.btn2=Button(self.winf,text="Ajouter",command=self.ajouter)
            self.btn2.place(x=230,y=130)
            

        elif n=="Supprime":
            select=self.tv.focus()
            self.el=self.tv.item(select,"values")

            self.var_saiid.set(self.el[0])
            self.var_sainom.set(self.el[1])
            self.var_saiville.set(self.el[2])
            self.var_saitele.set(self.el[3])
            self.var_saiemail.set(self.el[4])

            self.btn2=Button(self.winf,text="Supprime",command=self.supprime)
            self.btn2.place(x=230,y=130)                

    def code(self):
        global con
        global cur
        sql="SELECT id_fournisseur, nom, ville, tel, email FROM fournisseur WHERE id_fournisseur=%s"
        t=(self.var_saiid.get(),)
        cur.execute(sql,t)
        l=cur.fetchall()
        return l

    def ajouter(self):
        global con
        global cur
        if len(self.code())==0:
            sql="INSERT INTO fournisseur (id_fournisseur, nom, ville, tel, email) VALUES(%s,%s,%s,%s,%s)"
            t=(self.var_saiid.get(),self.var_sainom.get(),self.var_saiville.get(),self.var_saitele.get(),self.var_saiemail.get())
            cur=con.cursor()
            cur.execute(sql,t)
            con.commit()
            messagebox.showinfo("info","ajouter")
            self.supprime_tout()
            self.rempl()
        else:
            messagebox.showerror("Error","Fournisseur existe")
    
    def modifier(self):
        if len(self.code())>0:
            sql="UPDATE fournisseur SET nom=%s,ville=%s,tel=%s,email=%s WHERE id_fournisseur=%s"
            t=(self.var_sainom.get(),self.var_saiville.get(),self.var_saitele.get(),self.var_saiemail.get(),self.var_saiid.get())
            c=messagebox.askyesno("ask","Modiffier")
            if c==True:
                cur=con.cursor()
                cur.execute(sql,t)
                con.commit()
                self.supprime_tout()
                self.rempl()
        else:
            messagebox.showerror("Error","Fournisseur n'existe pas")

    def supprime(self):
        if len(self.code())>0:
            sql="DELETE FROM fournisseur WHERE id_fournisseur=%s"
            t=(self.var_saiid.get(),)
            c=messagebox.askyesno("ask","Supprimer")
            if c==True:
                cur=con.cursor()
                cur.execute(sql,t)
                con.commit()
                self.supprime_tout()
                self.rempl()
        else:
            messagebox.showerror("Error","fournisseur n'existe pas")


             