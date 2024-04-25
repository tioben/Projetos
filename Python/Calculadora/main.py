from tkinter import *
from tkinter import ttk

#Cores 
colorBlack = "#3b3b3b"
colorWhite = "#feffff"
colorBlue = "#38576b"
colorOrange = "#FFAB40"
colorGray = "#ECEFF1"

#Variáveis globais
todos_valores = ''

#Funções do app
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_display.set(todos_valores) #Passando valor do resultado para o display

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_display.set(str(resultado))

def limpar_display():
    global todos_valores 
    todos_valores = ""
    valor_display.set("")

#Configurações básicas da janela principal
janela = Tk() #Recebendo o objeto TK
janela.title("Calculadora") #Definindo título da janela
janela.geometry("235x310") #Definindo dimensões iniciais da janela (comprimento x altura)
janela.config(bg=colorBlack) #Configurando background

#Criando frames (display + corpo)
frame_display = Frame(janela, width=235, height=50, bg=colorBlue) #Definindo dimensões do display
frame_display.grid(row=0, column=0) #Definindo posição do display na janela

frame_body = Frame(janela, width=235, height=268) #Definindo dimensões do body
frame_body.grid(row=1, column=0) #Definindo posição do body na janela

#Criando Label (label dentro da frame display)
valor_display = StringVar()
app_label = Label(frame_display, textvariable=valor_display, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=colorBlue, fg=colorWhite)
app_label.place(x=0, y=0)

#Criando botões
b1 = Button(frame_body, command=limpar_display, text="C", width=11, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #Dimensões do botão1
b1.place(x=0,y=0) #Posição do botão1 (poderia usar o .grid() também)
b2 = Button(frame_body, command=lambda:entrar_valores("%") ,text="%", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0) 
b3 = Button(frame_body, command=lambda:entrar_valores("/") ,text="/", width=5, height=2, bg=colorOrange, fg=colorWhite, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b3.place(x=177,y=0) 

b4 = Button(frame_body, command=lambda:entrar_valores("7") ,text="7", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b4.place(x=0,y=52) 
b5 = Button(frame_body, command=lambda:entrar_valores("8") ,text="8", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b5.place(x=59,y=52) 
b6 = Button(frame_body, command=lambda:entrar_valores("9") ,text="9", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b6.place(x=118,y=52) 
b7 = Button(frame_body, command=lambda:entrar_valores("*") ,text="*", width=5, height=2, bg=colorOrange, fg=colorWhite, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b7.place(x=177,y=52) 

b8 = Button(frame_body, command=lambda:entrar_valores("4") ,text="4", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b8.place(x=0,y=104) 
b9 = Button(frame_body, command=lambda:entrar_valores("5") ,text="5", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b9.place(x=59,y=104) 
b10 = Button(frame_body, command=lambda:entrar_valores("6") ,text="6", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b10.place(x=118,y=104) 
b11 = Button(frame_body, command=lambda:entrar_valores("-") ,text="-", width=5, height=2, bg=colorOrange, fg=colorWhite, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b11.place(x=177,y=104) 

b12 = Button(frame_body, command=lambda:entrar_valores("1") ,text="1", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b12.place(x=0,y=156) 
b13 = Button(frame_body, command=lambda:entrar_valores("2") ,text="2", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b13.place(x=59,y=156) 
b14 = Button(frame_body, command=lambda:entrar_valores("3") ,text="3", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b14.place(x=118,y=156) 
b15 = Button(frame_body, command=lambda:entrar_valores("+") ,text="+", width=5, height=2, bg=colorOrange, fg=colorWhite, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b15.place(x=177,y=156) 

b16 = Button(frame_body, command=lambda:entrar_valores("0") ,text="0", width=11, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b16.place(x=0,y=208) 
b17 = Button(frame_body, command=lambda:entrar_valores(".") ,text=".", width=5, height=2, bg=colorGray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b17.place(x=118,y=208) 
b18 = Button(frame_body, command=calcular, text="=", width=5, height=2, bg=colorOrange, fg=colorWhite, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b18.place(x=177,y=208) 

#Abrindo janela
janela.mainloop()

