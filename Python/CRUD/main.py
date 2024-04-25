# Import tkinter tools for front-end (ferramentas para desenvolvimento da parte visual)
from tkinter import*
from tkinter import font
from cgitb import text
from tkcalendar import Calendar, DateEntry # Necessery enter in virtual environment (necessário ativar ambiente virtual e executar esse arquivo pelo cmd)
from tkinter import ttk
from view import * # Import main.py
from tkinter import messagebox

# Colors
Black = "#f0f3f5"  # preta
White = "#feffff"  # branca
Green = "#4fa882"  # verde
Value = "#38576b"  # valor
Letter = "#403d3d"   # letra
Profit = "#e06636"   # - profit
Blue = "#038cfc"   # azul
Red = "#ef5350"   # vermelha
MoreGreen = "#263238"   # + verde
SkyBlue = "#e9edf5"   # azul pastel
Yellow = "#dbd712" # amarelo

# Create windowns (criando janela)
windowns = Tk() # Open objet TK() (Adquirindo o objeto TK())
windowns.title("Students Database") # (Definindo título da janela)
windowns.geometry('1050x450') # Setting windowns dimensions (Definindo dimensões da janela)
windowns.config(background=SkyBlue) # Setting windowns background (Definindo cor de fundo)
windowns.resizable(width=False, height=False) # Setting windowns extremities (Bloqueando expandir tela)

#Splitting windowns (dividindo janelas; DIV's)
frameHeaderForm = Frame(windowns, width=310, height=50, bg=Green, relief='flat') # Setting frame dimensions (Definindo dimensões do frame)
frameHeaderForm.grid(row=0, column=0) # Setting frame position (Definindo posição do frame)

frameForm = Frame(windowns, width=310, height=400, bg=White, relief='flat') # Setting frame dimensions (Definindo dimensões do frame)
frameForm.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW) # Setting frame position (Definindo posição do frame

frameDatabaseView = Frame(windowns, width=588, height=403, bg=White, relief='flat') # Setting frame dimensions (Definindo dimensões do frame)
frameDatabaseView.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) # Setting frame position (Definindo posição do frame

# Label for frameHeaderForm (label da frame cabeçalho do formulário)
appTitle = Label(frameHeaderForm, text="Formulário de consultoria", bg=Green, anchor=NW, font=("Ivy 13 bold"), fg=White, relief="flat")
appTitle.place(relx=0.67, rely=0.5, anchor=E)

# insert function
def insert():
    name = entryName.get()
    email = entryEmail.get()
    tel = entryTel.get()
    date = entryDate.get()
    appointment = entryAppointment.get()
    about = entryAbout.get()
    userInfo = [name, email, tel, date, appointment, about]
    if name == '':
        messagebox.showerror("Error!", "Name field cannot be empty.")
    else:
        creaty(userInfo)
        messagebox.showinfo("Sucess!", "User registed.")

        entryName.delete(0, 'end')
        entryEmail.delete(0, 'end')
        entryTel.delete(0, 'end')
        entryDate.delete(0, 'end')
        entryAppointment.delete(0, 'end')
        entryAbout.delete(0, 'end')

        for widget in frameDatabaseView.winfo_children():
            widget.destroy()
    show()

# global variable "tree"
global tree

# update function
def update():
    try:
        treev_dados = tree.focus()
        treev_dicionary = tree.item(treev_dados)
        tree_list = treev_dicionary['values']
        id = tree_list[0]

        entryName.delete(0, 'end')
        entryEmail.delete(0, 'end')
        entryTel.delete(0, 'end')
        entryDate.delete(0, 'end')
        entryAppointment.delete(0, 'end')
        entryAbout.delete(0, 'end')
        
        entryName.insert(0, tree_list[1])
        entryEmail.insert(0, tree_list[2])
        entryTel.insert(0, tree_list[3])
        entryDate.insert(0, tree_list[4])
        entryAppointment.insert(0, tree_list[5])
        entryAbout.insert(0, tree_list[6])

        # atualizar function
        def atualizar():
            name = entryName.get()
            email = entryEmail.get()
            tel = entryTel.get()
            date = entryDate.get()
            appointment = entryAppointment.get()
            about = entryAbout.get()
            userInfo = [name, email, tel, date, appointment, about, id]
            if name == '':
                messagebox.showerror("Error!", "Name field cannot be empty.")
            else:
                update_info(userInfo)
                messagebox.showinfo("Sucess!", "User updated.")

                entryName.delete(0, 'end')
                entryEmail.delete(0, 'end')
                entryTel.delete(0, 'end')
                entryDate.delete(0, 'end')
                entryAppointment.delete(0, 'end')
                entryAbout.delete(0, 'end')

                for widget in frameDatabaseView.winfo_children():
                    widget.destroy()
                show()
        # Update Button (botão atualizar)
        confirmUpdateButton = Button(frameForm, command=atualizar, text="Confirmar", width=10, font=("Inv 7 bold"), bg=Green, fg=White, relief="raised", overrelief="ridge")
        confirmUpdateButton.place(x=120, y=377)
    
    except IndexError:
        messagebox.showerror("Error!", "Select a data from the table!")

# delete function
def delete():
    try:
        treev_dados = tree.focus()
        treev_dicionary = tree.item(treev_dados)
        tree_list = treev_dicionary['values']
        
        id = [tree_list[0]]

        delete_info(id)
        messagebox.showinfo("Sucess!", "User deleted.")

        for widget in frameDatabaseView.winfo_children():
                    widget.destroy()
        show()
        
    except IndexError:
        messagebox.showerror("Error!", "Select a data from the table!")

# Labels/Entrys for frameForm (labels e entrys da frame formulário)
# Name (nome)
labelName = Label(frameForm, text="Nome *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelName.place(x=10, y=10)

entryName = Entry(frameForm, width=45, justify="left", relief="solid")
entryName.place(x=15, y=40)

# E-mail
labelEmail = Label(frameForm, text="E-mail *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelEmail.place(x=10, y=70)

entryEmail = Entry(frameForm, width=45, justify="left", relief="solid")
entryEmail.place(x=15, y=100)

# Tel.:
labelTel = Label(frameForm, text="Telefone *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelTel.place(x=10, y=140)

entryTel = Entry(frameForm, width=45, justify="left", relief="solid")
entryTel.place(x=15, y=170)

# Date (data)
labelDate = Label(frameForm, text="Data *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelDate.place(x=10, y=210)

entryDate = DateEntry(frameForm, width=12, background="darkblue", foreground='"white', borderwidth=2, year=2023)
entryDate.place(x=15, y=240)

# Medicinal Appointment (consulta médica)
labelAppointment = Label(frameForm, text="Estado *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelAppointment.place(x=150, y=210)

entryAppointment = Entry(frameForm, width=22, justify="left", relief="solid")
entryAppointment.place(x=155, y=240)

# About (sobre)
labelAbout = Label(frameForm, text="Consulta sobre *", bg=White, anchor=NW, font=("Ivy 10 bold"), fg=Letter, relief="flat")
labelAbout.place(x=10, y=280)

entryAbout = Entry(frameForm, width=45, justify="left", relief="solid")
entryAbout.place(x=15, y=310)

# Create buttons (criando botões)
# Insert Button (botão inserir)
insertButton = Button(frameForm, command=insert, text="Inserir", width=10, font=("Inv 9 bold"), bg=Blue, fg=White, relief="raised", overrelief="ridge")
insertButton.place(x=10, y=350)

# Update Button (botão atualizar)
updatetButton = Button(frameForm, command=update, text="Atualizar", width=10, font=("Inv 9 bold"), bg=Green, fg=White, relief="raised", overrelief="ridge")
updatetButton.place(x=115, y=350)

# Delete Button (botão deletar)
DeleteButton = Button(frameForm, command=delete, text="Deletar", width=10, font=("Inv 9 bold"), bg=Red, fg=White, relief="raised", overrelief="ridge")
DeleteButton.place(x=220, y=350)

# -------- Código para tabela -------- 
def show():
    global tree
    lista = ready()

    # list for header
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    # create the table
    tree = ttk.Treeview(frameDatabaseView, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDatabaseView, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frameDatabaseView, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDatabaseView.grid_rowconfigure(0, weight=12)
    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
    for item in lista:
        tree.insert('', 'end', values=item)

show()
# Open windowns (abrindo janela)
windowns.mainloop()
