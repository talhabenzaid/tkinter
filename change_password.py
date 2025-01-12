import mysql.connector
from tkinter import *
from tkinter import messagebox

con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

class change_password(Tk):
    def existe(self):
        t=False
        global con
        global cur
        sql="SELECT login, password FROM users WHERE login=%s and password=%s  "
        c=(self.saiutili.get(),self.saimot.get())
        cur.execute(sql,c)
        l=cur.fetchall()
        r=cur.rowcount
        if r>0 and self.saiutili.get()!="" and self.saimot.get()!="":
            t=True   
        return t

    def mot_de_passe(self):
        t=False
        if self.sainouv.get()==self.saicon.get():
            t=True
        return t    


    def modifier(self):
        if self.existe()==False:
            messagebox.showerror("Error","Utilisateur ou mot de passe incorect")
        elif self.mot_de_passe()==False:
            messagebox.showerror("Error","nouveau mot de passe incorrect")
        else:       
            global con
            global cur
            sql="UPDATE users SET password=%s WHERE login=%s"
            t=(self.var_sainouv.get(),self.var_saiutili.get())
            cur.execute(sql,t)
            cur=con.commit()  
            messagebox.showinfo("info","modifier")
            self.destroy()

    def __init__(self):
        Tk.__init__(self)
        self.title("Nouveau mot de passe")
        self.geometry("330x170")
        self.resizable(False,False)

        lblutili=Label(self,text="Nom d'utilisateur")
        lblutili.place(x=30,y=10)

        self.var_saiutili=StringVar()
        self.saiutili=Entry(self,textvariable=self.var_saiutili)
        self.saiutili.place(x=170,y=10)

        lblmot=Label(self,text="Mot de passe")
        lblmot.place(x=30,y=40)

        self.var_saimot=StringVar()
        self.saimot=Entry(self,textvariable=self.var_saimot,show="*")
        self.saimot.place(x=170,y=40)

        lblnouv=Label(self,text="Nouveau mot de passe")
        lblnouv.place(x=30,y=70)

        self.var_sainouv=StringVar()
        self.sainouv=Entry(self,textvariable=self.var_sainouv,show="*")
        self.sainouv.place(x=170,y=70)

        lblcon=Label(self,text="Confirme mot de passe")
        lblcon.place(x=30,y=100)

        self.var_saicon=StringVar()
        self.saicon=Entry(self,textvariable=self.var_saicon,show="*")
        self.saicon.place(x=170,y=100)

        btn1=Button(self,text="Modifier",command=self.modifier)
        btn1.place(x=30,y=130)

        btn2=Button(self,text="Quitter",command=quit)
        btn2.place(x=240,y=130)


        

