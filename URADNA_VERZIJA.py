import tkinter as tk
from model2 import Zivljenja


##class Zivljenja:
##    def __init__(self):
##        self.zivljenja = 0
##
##    def __repr__(self):
##        return '%s' % (self.zivljenja)
##
##    def lahka_igra(self):
##        self.zivljenja += 3        
##        self.preveri_zivljenja()
##        return self.zivljenja
##
##    def tezka_igra(self):
##        self.zivljenja += 1
##        self.preveri_zivljenja()
##        return '%s' % (self.zivljenja)
##    
##    def napacen_odgovor1(self):
##        self.zivljenja -= 1
##        self.preveri_zivljenja()
##        return '%s' % (self.zivljenja)
##
##    def preveri_zivljenja(self):
##        text = 'Življenja: %s' % self.zivljenja

##class Napake:
##
##    napake = 0
##    
##    def __init__(self, parent, controller):
##        Napake.napake = tk.IntVar()
##
##    def __repr__(self):
##        return "%s" % (self.napake)
##
##    def counter():
##        Napake.napake.set(Napake.napake.get() + 1)
####        stevec_napak.config(text='Število napak = ' + str(napake.get()))
##
##    def preveri_napake():
##        if Napake.napake.get() > 2:
##            konec_igre()        
##            
##    def konec_igre():
##        Kviz.controller.pokazi_stran("konec_igre")

##class Zivljenja:
##    def __init__(self):
##        self.zivljenja = 0
##
##    def __repr__(self):
##        return '%s' % (self.zivljenja)
##
##    def lahka_igra(self):
##        total.set(total.get() + 3)
##
##    def tezka_igra(self):
##        total.set(total.get() + 1)
##    
##    def napacen_odgovor(self):
##        total.set(total.get() - 1)
##
##    def preveri_zivljenja(self):
##        text = 'Življenja: %s' % self.zivljenja
##        print(text)
##
##    def counter(self):
##        total.set(total.get() + 1)

######NARED TKO DA BO TOTAL V MODELU NAPAKE NE V KVIZU in verjetn bo to resil problem z updateanjem



class Kviz(tk.Tk):

    total = 0
    
    def __init__(self):
        tk.Tk.__init__(self)

        Kviz.total = tk.IntVar()

        vse_strani = tk.Frame(self)
        vse_strani.pack(side="top", fill="both", expand=True)

        self.stran = {}
        for F in (zacetna_stran, izbira_tezavnosti, prvo_vprasanje, drugo_vprasanje, tretje_vprasanje, cetrto_vprasanje, peto_vprasanje, konec_igre, prvo_vprasanje_tezka, drugo_vprasanje_tezka, tretje_vprasanje_tezka, cetrto_vprasanje_tezka, peto_vprasanje_tezka):
            ime_strani = F.__name__
            frame = F(parent=vse_strani, controller=self)
            self.stran[ime_strani] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.pokazi_stran("zacetna_stran")

    def pokazi_stran(self, ime_strani):
        frame = self.stran[ime_strani]
        frame.tkraise()


class zacetna_stran(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        naslov = tk.Label(self, text='KVIZ', font=("Helvetica", 20))
        naslov.pack()
        gumb = tk.Button(self, text="Začetek", command=lambda: controller.pokazi_stran("izbira_tezavnosti"))
        gumb.pack()

class izbira_tezavnosti(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
        naslov = tk.Label(self, text='Izbira težavnosti', font=("Helvetica", 20))
        naslov.pack()
        button = tk.Button(self, text="Lahka (dovoljeni 2 napaki)", command=lambda: [controller.pokazi_stran("prvo_vprasanje")])
        button.pack()
        button2 = tk.Button(self, text="Težka (dovoljenih 0 napak)", command=lambda: [controller.pokazi_stran("prvo_vprasanje_tezka")])
        button2.pack()

#############LAHKA IGRA

class prvo_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total
##        Napake.__init__(self)

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("drugo_vprasanje")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [counter(), preveri_napake()], text='NE', font=("Helvetica", 16))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text='Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        stevec_napak.pack()

##        stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            
            stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("konec_igre")

class drugo_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje1 = tk.Label(self, text="koliko je 7 krat 8?", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("tretje_vprasanje")], text='42', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [counter(), preveri_napake()], text='48', font=("Helvetica", 16))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text='Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        stevec_napak.pack()

        stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            
            stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("konec_igre")
        
class tretje_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje1 = tk.Label(self, text="koliko je 7 krat 8?", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("cetrto_vprasanje")], text='42', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [counter(), preveri_napake()], text='48', font=("Helvetica", 16))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text='Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        stevec_napak.pack()

        stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            
            stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("konec_igre")
        
class cetrto_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje1 = tk.Label(self, text="koliko je 7 krat 8?", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("peto_vprasanje")], text='42', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [counter(), preveri_napake()], text='48', font=("Helvetica", 16))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text='Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        stevec_napak.pack()

        stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("konec_igre")
        
class peto_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje1 = tk.Label(self, text="koliko je 7 krat 8?", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("konec_igre")], text='42', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [counter(), preveri_napake()], text='48', font=("Helvetica", 16))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text='Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        stevec_napak.pack()

        stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            
            stevec_napak.config(text='Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("konec_igre")
             

#############TEŽKA IGRA
        
class prvo_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("drugo_vprasanje_tezka")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [controller.pokazi_stran("zacetna_stran")], text='NE', font=("Helvetica", 16))
        odgovor2.pack()

class drugo_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("tretje_vprasanje_tezka")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [controller.pokazi_stran("zacetna_stran")], text='NE', font=("Helvetica", 16))
        odgovor2.pack()

class tretje_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("cetrto_vprasanje_tezka")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [controller.pokazi_stran("zacetna_stran")], text='NE', font=("Helvetica", 16))
        odgovor2.pack()

class cetrto_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("peto_vprasanje_tezka")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [controller.pokazi_stran("zacetna_stran")], text='NE', font=("Helvetica", 16))
        odgovor2.pack()

class peto_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje1 = tk.Label(self, text="i", font=("Helvetica", 20))
        vprasanje1.pack()
        odgovor1 = tk.Button(self, command=lambda: [controller.pokazi_stran("konec_igre")], text='DA', font=("Helvetica", 16))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command=lambda: [controller.pokazi_stran("zacetna_stran")], text='NE', font=("Helvetica", 16))
        odgovor2.pack()


############KONEC IGRE

class konec_igre(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        konec = tk.Label(self, text="Konec", font=("Helvetica", 20))
        konec.pack() 



if __name__ == "__main__":
    kviz = Kviz()
    kviz.title("KVIZ")
    kviz.mainloop()
