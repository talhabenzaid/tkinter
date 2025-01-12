import mysql.connector
from tkinter import *
from tkinter import messagebox


con=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
cur=con.cursor()

class Nouvel_utilisateur(Tk):
    def existe(self):
        e=True
        global con
        global cur
        sql="SELECT login FROM users WHERE login=%s"
        t=(self.saiutili.get(),)
        cur.execute(sql,t)
        l=cur.fetchall()
        r=cur.rowcount
        if r>0:
            e=False
        return e

    def mot_de_passe(self):
        t=False
        if self.saimot.get()==self.saicon.get():
            t=True
        return t         

    def enregstre(self):
        if self.existe()==False:
            messagebox.showerror("Errer","Utilisateur existe")
        elif self.mot_de_passe()==False:
            messagebox.showerror("Error","Mot de passe incorrect")
        else:        
            global con
            global cur
            sql="INSERT INTO users(login, password) VALUES (%s,%s)"
            t=(self.var_saiutili.get(),self.var_saimot.get())
            cur.execute(sql,t)
            cur=con.commit()
            messagebox.showinfo("info","ajouter")
            self.destroy()

    def __init__(self):
        Tk.__init__(self)
    
        self.title("Nouveau utilisateur")
        self.geometry("290x140")
        self.resizable(False,False)

        lblutili=Label(self,text="Nom d'utilisateur")
        lblutili.place(x=20,y=10)

        self.var_saiutili=StringVar()
        self.saiutili=Entry(self,textvariable=self.var_saiutili)
        self.saiutili.place(x=130,y=10)

        lblmot=Label(self,text="Mot de passe")
        lblmot.place(x=20,y=40)

        self.var_saimot=StringVar()
        self.saimot=Entry(self,textvariable=self.var_saimot,show="*")
        self.saimot.place(x=130,y=40)

        lblcon=Label(self,text="Confirme")
        lblcon.place(x=20,y=70)

        self.var_saicon=StringVar()
        self.saicon=Entry(self,textvariable=self.var_saicon,show="*")
        self.saicon.place(x=130,y=70)



        btn1=Button(self,text="Enregstre",command=self.enregstre)
        btn1.place(x=20,y=100)

        btn2=Button(self,text="Quitter",command=quit)
        btn2.place(x=220,y=100)




      