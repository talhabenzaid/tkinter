from tkinter import *

import liste_clients
import liste_fournisseurs
import liste_articles
import liste_facture_fournisseurs
import nouvel_utilisateur
import change_password


class Liste_menu(Tk):

    def fon_liste_clients(self):
        liste_clients.Liste_client().rempl()
        liste_clients.Liste_client().recherche()
        

    def fon_liste_fournisseurs(self):
        liste_fournisseurs.liste_fournisseur().rempl()

    def fon_liste_articles(self):
        liste_articles.Liste_article().rempl()

    def fon_liste_facture_clients(self):
        pass

    def fon_liste_facture_fournisseurs(self):
        liste_facture_fournisseurs.Facture_fournisseurs().rempl()
        pass

    def fon_Etat_de_stock(self):
        pass

    def fon_nouvel_utilisateur(self):
        nouvel_utilisateur.Nouvel_utilisateur()
        pass

    def fon_change_password(self):
        change_password.change_password()
        pass



    def __init__(self):
        Tk.__init__(self)
        self.geometry("1000x600")
        self.title("gestion")
        self.resizable(False,False)

        self.img=PhotoImage(file=r"C:\Users\LENOVO\Desktop\prog\python\big proj\comm.png")
        self.lbl=Label(self,image=self.img)
        self.lbl.pack()

        menubar=Menu(self)

        base=Menu(menubar,tearoff=0)
        base.add_command(label="Articles",command=self.fon_liste_articles)
        base.add_command(label="Clients",command=self.fon_liste_clients)
        base.add_command(label="Fournisseurs",command=self.fon_liste_fournisseurs)
        base.add_separator()
        base.add_command(label="Quit",command=quit)
        menubar.add_cascade(label="Base",menu=base)

        achat=Menu(menubar,tearoff=0)
        achat.add_command(label="Facture",command=self.fon_liste_facture_clients)
        achat.add_separator()
        achat.add_command(label="Quit",command=quit)
        menubar.add_cascade(label="Achat",menu=achat)


        vender=Menu(menubar,tearoff=0)
        vender.add_command(label="Facture",command=self.fon_liste_facture_fournisseurs)
        vender.add_separator()
        vender.add_command(label="Quit",command=quit)
        menubar.add_cascade(label="vender",menu=vender)


        stock=Menu(menubar,tearoff=0)
        stock.add_command(label="Etat de stock",command=self.fon_Etat_de_stock)
        stock.add_separator()
        stock.add_command(label="Quit",command=quit)
        menubar.add_cascade(label="Stock",menu=stock)

        utilisateur=Menu(menubar,tearoff=0)
        utilisateur.add_command(label="Nouveau utilisateur",command=self.fon_nouvel_utilisateur)
        utilisateur.add_command(label="Nouveau mot passe",command=self.fon_change_password)
        utilisateur.add_separator()
        utilisateur.add_command(label="Quit",command=quit)
        menubar.add_cascade(label="Utilisateur",menu=utilisateur)

        self.config(menu=menubar)
