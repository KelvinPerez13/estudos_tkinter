from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='black')
        self.root.geometry("600x850")
        self.root.resizable(True, True)
        self.root.maxsize(width=1900, height=1700)
        self.root.minsize(width=600, height=750)

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg='pink',
                            highlightbackground= 'brown'
                            ,highlightthickness=2
                                            )
        self.frame1.place(relx=0.01, rely=0.01
                          ,relwidth = 0.98, relheight=0.48
                                        )
        
        self.frame2 = Frame(self.root, bd=4, bg='pink',
                            highlightbackground= 'brown'
                            ,highlightthickness=2
                                            )
        self.frame2.place(relx=0.01, rely=0.5
        ,relwidth = 0.98, relheight=0.43)
    
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame1, text="Limpar", bg='brown', fg='white')
        self.bt_limpar.place(relx= 0.55, rely = 0.1
                             , relwidth=0.15, relheight= 0.09)
        
        self.bt_limpar = Button(self.frame1, text="Buscar")
        self.bt_limpar.place(relx= 0.70, rely = 0.1
                             , relwidth=0.15, relheight= 0.09)
## entry e label codigo 
        self.lb_codigo = Label(self.frame1, text="Codigo", bg='pink')
        self.lb_codigo.place(relx= 0.08 , rely=0.05)
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx= 0.06, rely=0.12, relheight=0.05, relwidth=0.15)

## entry e label nome cliente
        self.lb_codigo = Label(self.frame1, text="Nome", bg='pink')
        self.lb_codigo.place(relx= 0.08 , rely=0.2)
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx= 0.06, rely=0.27, relheight=0.05, relwidth=0.35)

Application()
