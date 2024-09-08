from tkinter import *
import tkinter
#Ricardo Armando Fuentes Arevalo 07/09/2024
ventana = Frame(height=250, width=450)
ventana.pack(padx=5, pady=5)

def sumar():
    resultado = int(numero1.get()+int(numero2.get()))
    Label(text=resultado,font=("Arial",15),fg="red").place(width=50,x=200,y=160)

def restar():
    resultado = int(numero1.get()-int(numero2.get()))
    Label(text=resultado,font=("Arial",15),fg="red").place(width=50,x=200,y=160)

def multiplicar():
    resultado = int(numero1.get()*int(numero2.get()))
    Label(text=resultado,font=("Arial",15),fg="red").place(width=50,x=200,y=160)

def dividir():
    resultado = int(numero1.get()/int(numero2.get()))
    Label(text=resultado,font=("Arial",15),fg="red").place(width=50,x=200,y=160)


resultado = 0
numero1 = IntVar()
numero2 = IntVar()

titulo = Label(text="Calculadora básica",font=("Arial",15)).place(x=150,y=30)

nu1 = Entry(textvariable=numero1).place(width=130,x=180,y=60)
nu2 = Entry(textvariable=numero2).place(width=130,x=180,y=90)

bsumar = Button(text="suma", command=sumar).place(width=80, x=50,y=120)
botonre = Button(text="resta", command=restar).place(width=80, x=150,y=120)
botonpor = Button(text="multiplicacion", command=multiplicar).place(width=100, x=245,y=120)
botondi = Button(text="división", command=dividir).place(width=80, x=350,y=120)

ventana.mainloop()