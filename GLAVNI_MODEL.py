import tkinter as tk

class Napake:

    napake = 0
    
    def __init__(self, parent, controller):
        Napake.napake = tk.IntVar()

    def __repr__(self):
        return "%s" % (self.napake)

    def counter():
        Napake.napake.set(Napake.napake.get() + 1)
        stevec_napak.config(text='Število napak = ' + str(napake.get()))

    def preveri_napake():
        if Napake.napake.get() > 2:
            Kviz.pokazi_stran("konec_igre")
