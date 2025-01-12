from tkinter import *
import mysql.connector
from tkinter import ttk
from functools import partial
from tkinter import messagebox

con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

class Liste_article(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("760x370")
        self.title("Article")
        self.resizable(False,False)

        self.frame1=Frame(self,bg="light blue")
        self.frame1.place(x=0,y=0,width=200,height=430)

        self.btn_rech=Button(self.frame1,text="Recherche",bg="gray",fg="white",command=self.recherche)
        self.btn_rech.place(x=0,y=0,width=200,height=50)

        self.lblid=Label(self.frame1,text="ID",bg="black",fg="white")
        self.lblid.place(x=40,y=70,width=100,height=20)
        
        self.var_saiid=StringVar()
        self.saiid=Entry(self.frame1,textvariable=self.var_saiid,bg="gray",fg="white")
        self.saiid.place(x=20,y=100,width=140,height=20)
        
        self.lbldesi=Label(self.frame1,text="Designation",bg="black",fg="white")
        self.lbldesi.place(x=40,y=130,width=100,height=20)
        
        self.var_saidesi=StringVar()
        self.saidesi=Entry(self.frame1,textvariable=self.var_saidesi,bg="gray",fg="white")
        self.saidesi.place(x=20,y=160,width=140,height=20)
        
        self.lblpv=Label(self.frame1,text="Prix venter",bg="black",fg="white")
        self.lblpv.place(x=40,y=190,width=100,height=20)
        
        self.var_saipv=StringVar()
        self.saipv=Entry(self.frame1,textvariable=self.var_saipv,bg="gray",fg="white")
        self.saipv.place(x=20,y=220,width=140,height=20)
        
        self.lblss=Label(self.frame1,text="Stock seuil",bg="black",fg="white")
        self.lblss.place(x=40,y=250,width=100,height=20)
        
        self.var_saiss=StringVar()
        self.saiss=Entry(self.frame1,textvariable=self.var_saiss,bg="gray",fg="white")
        self.saiss.place(x=20,y=280,width=140,height=20)

        self.lblsf=Label(self.frame1,text="Stock finial",bg="black",fg="white")
        self.lblsf.place(x=40,y=310,width=100,height=20)
        
        self.var_saisf=StringVar()
        self.saisf=Entry(self.frame1,textvariable=self.var_saisf,bg="gray",fg="white")
        self.saisf.place(x=20,y=340,width=140,height=20)

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
        self.frame3.place(x=200,y=50,width=600,height=430)
        
        self.tv=ttk.Treeview(self.frame3,columns=(1,2,3,4,5),show="headings")
        self.tv.heading(1,text="ID")
        self.tv.heading(2,text="Designation")
        self.tv.heading(3,text="Prix")
        self.tv.heading(4,text="Stock")
        self.tv.heading(5,text="Stock finial")

        self.tv.column(1,width=10)
        self.tv.column(2,width=100)
        self.tv.column(3,width=100)
        self.tv.column(4,width=100)
        self.tv.column(5,width=100)    

        self.tv.place(x=0,y=0,width=560,height=500)

    def rempl(self):
        global con
        global cur
        sql="SELECT id_article, designation, prix, stock, stock_fin FROM article "
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
            sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE id_article=%s"
            t=(self.var_saiid.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","N'existe pas")
            for e  in l:
                desi=True
                pv=True
                ss=True
                sf=True
                if self.var_saidesi.get()!="":
                    desi=False
                    if e[1]==self.var_saidesi.get():
                        desi=True
                if self.var_saipv.get()!="":
                    pv=False
                    if e[2]==self.var_saipv.get():
                        pv=True
                if self.var_saiss.get()!="":
                    ss=False
                    if e[3]==self.var_saiss.get():
                        ss=True
                if self.var_saisf.get()!="":
                    sf=False
                    if e[4]==self.var_saisf.get():
                        sf=True                        
                if desi==True and pv==True and ss==True and sf==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showerror("Error","N'existe pas")   
        elif self.var_saidesi.get()!="":
            sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE designation=%s "
            t=(self.var_saidesi.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","N'existe pas")
            for e  in l:
                pv=True
                ss=True
                sf=True
                if self.var_saipv.get()!="":
                    pv=False
                    if e[2]==self.var_saipv.get():
                        pv=True
                if self.var_saiss.get()!="":
                    ss=False
                    if e[3]==self.var_saiss.get():
                        ss=True
                if self.var_saisf.get()!="":
                    sf=False
                    if e[4]==self.var_saisf.get():
                        sf=True                        
                if pv==True and ss==True and sf==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showerror("Error","N'existe pas")     
        elif self.var_saipv.get()!="":
            sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE prix=%s "
            t=(self.var_saipv.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","N'existe pas")
            for e  in l:
                ss=True
                sf=True
                if self.var_saiss.get()!="":
                    ss=False
                    if e[3]==self.var_saiss.get():
                        ss=True
                if self.var_saisf.get()!="":
                    sf=False
                    if e[4]==self.var_saisf.get():
                        sf=True                        
                if ss==True and sf==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showerror("Error","N'existe pas")     
        elif self.var_saiss.get()!="":
            sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE stock=%s "
            t=(self.var_saiss.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","N'existe pas")
            for e  in l:
                sf=True
                if self.var_saisf.get()!="":
                    sf=False
                    if e[4]==self.var_saisf.get():
                        sf=True                        
                if sf==True:
                    self.supprime_tout()
                    self.tv.insert(parent="",index=0,values=(e))
                else:
                    messagebox.showerror("Error","N'existe pas")
        elif self.var_saisf.get()!="":
            sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE stock_fin=%s"
            t=(self.var_saisf.get(),)
            cur.execute(sql,t)
            l=cur.fetchall()
            if len(l)==0:
                messagebox.showerror("Error","N'existe pas")
            for e  in l:
                self.supprime_tout()
                self.tv.insert(parent="",index=0,values=(e))
        else:
            self.supprime_tout()
            self.rempl()                

    
    def window(self,n):
        self.winf=Toplevel()
        self.winf.title("Article")
        self.winf.geometry("300x170")
        self.winf.resizable(False,False)
       

        self.lbldesi=Label(self.winf,text="Designation")
        self.lbldesi.place(x=20,y=10)

        self.var_saidesi=StringVar()
        self.saidesi=Entry(self.winf,textvariable=self.var_saidesi)
        self.saidesi.place(x=120,y=10)

        self.lblpv=Label(self.winf,text="Prix venter")
        self.lblpv.place(x=20,y=40)

        self.var_saipv=StringVar()
        self.saipv=Entry(self.winf,textvariable=self.var_saipv)
        self.saipv.place(x=120,y=40)

        self.lblss=Label(self.winf,text="Stock seuil")
        self.lblss.place(x=20,y=70)

        self.var_saiss=StringVar()
        self.saiss=Entry(self.winf,textvariable=self.var_saiss)
        self.saiss.place(x=120,y=70)

        self.lblsf=Label(self.winf,text="stock fin")
        self.lblsf.place(x=20,y=100)

        self.var_saisf=StringVar()
        self.saisf=Entry(self.winf,textvariable=self.var_saisf)
        self.saisf.place(x=120,y=100)

        self.btn1=Button(self.winf,text="Quitter",command=quit)
        self.btn1.place(x=230,y=130)

        if n=="modifier":
            select=self.tv.focus()
            self.el=self.tv.item(select,"values")

            self.var_saiid.set(self.el[0])
            self.var_saidesi.set(self.el[1])
            self.var_saipv.set(self.el[2])
            self.var_saiss.set(self.el[3])
            self.var_saisf.set(self.el[4])

            self.btn2=Button(self.winf,text="Modifier",command=self.modifier)
            self.btn2.place(x=20,y=130)
            

        elif n=="nouveau":
            self.btn2=Button(self.winf,text="Ajouter",command=self.ajouter)
            self.btn2.place(x=20,y=130)
            

        elif n=="Supprime":
            select=self.tv.focus()
            self.el=self.tv.item(select,"values")

            self.var_saiid.set(self.el[0])
            self.var_saidesi.set(self.el[1])
            self.var_saipv.set(self.el[2])
            self.var_saiss.set(self.el[3])
            self.var_saisf.set(self.el[4])

            self.btn2=Button(self.winf,text="Supprime",command=self.supprime)
            self.btn2.place(x=20,y=160)         

    def code(self):
        global con
        global cur
        sql="SELECT id_article, designation, prix, stock, stock_fin FROM article WHERE id_article=%s"
        t=(self.var_saiid.get(),)
        cur.execute(sql,t)
        l=cur.fetchall()
        return l

    def ajouter(self):

        global con
        global cur
        if len(self.code())==0:
            sql="INSERT INTO article (id_article, designation, prix, stock, stock_fin) VALUES(%s,%s,%s,%s,%s)"
            t=(self.var_saiid.get(),self.var_saidesi.get(),self.var_saipv.get(),self.var_saiss.get(),self.var_saisf.get())
            cur=con.cursor()
            cur.execute(sql,t)
            con.commit()
            messagebox.showinfo("info","ajouter")
            self.supprime_tout()
            self.rempl()
        else:
            messagebox.showerror("Error","client existe")
    
    def modifier(self):
        if len(self.code())>0:
            sql="UPDATE article SET designation=%s,prix=%s,stock=%s,stock_fin=%s WHERE id_article=%s"
            t=(self.var_saidesi.get(),self.var_saipv.get(),self.var_saiss.get(),self.var_saisf.get(),self.var_saiid.get())
            c=messagebox.askyesno("ask","Modiffier")
            if c==True:
                cur=con.cursor()
                cur.execute(sql,t)
                con.commit()
                self.supprime_tout()
                self.rempl()
        else:
            messagebox.showerror("Error","client n'existe pas")
    def supprime(self):
        if len(self.code())>0:
            sql="DELETE FROM article WHERE id_article=%s"
            t=(self.var_saiid.get(),)
            c=messagebox.askyesno("ask","Supprimer")
            if c==True:
                cur=con.cursor()
                cur.execute(sql,t)
                con.commit()
                self.supprime_tout()
                self.rempl()
        else:
            messagebox.showerror("Error","client n'existe pas")
            