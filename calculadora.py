# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:30:43 2020

@author: Alex
"""
from tkinter import Tk, Label, Entry, Button, messagebox
from functools import partial


numero1=0
numero2=0
simbolo=0
tamanio=0
respuesta=""

def insertar(a):
    caja.configure(state='normal')
    caja.insert('end', a)
    caja.configure(state='disabled')
    
def operador(arg,signo):
    global numero1
    global simbolo
    global tamanio
    numero1=int(caja.get());
    simbolo=arg
    caja.configure(state='normal')
    caja.insert('end', signo)
    tamanio=len(caja.get())
    caja.configure(state='disabled')
    btnsuma["state"] = "disabled"
    btnresta["state"] = "disabled"
    btnmultiplicacion["state"] = "disabled"
    btndivision["state"] = "disabled"
    

def resolver():
    global numero1
    global simbolo
    global numero2
    global respuesta
    numero2=int(caja.get()[tamanio:])
    if simbolo == 0:
	    respuesta=str(numero1+numero2)
    elif simbolo == 1:
	    respuesta=str(numero1-numero2)
    elif simbolo == 2:
	    respuesta=str(numero1*numero2)
    elif simbolo == 3 and numero2!=0:
        respuesta=str(numero1/numero2)
    else:
        respuesta="Error"
        
    caja.configure(state='normal')
    caja.delete(0, 'end')
    caja.insert('end', "Respuesta="+respuesta)
    caja.configure(state='disabled')
    btnigual["state"] = "disabled"

def resetear():
    global numero1
    global simbolo
    global numero2
    global respuesta
    numero1=0
    numero2=0
    simbolo=0
    respuesta=""
    caja.configure(state='normal')
    caja.delete(0, 'end')
    caja.configure(state='disabled')
    btnsuma["state"] = "normal"
    btnresta["state"] = "normal"
    btnmultiplicacion["state"] = "normal"
    btndivision["state"] = "normal"
    btnigual["state"] = "normal"
    
window = Tk()
window.title("Calculadora")
window.geometry("400x200")
window["bg"] = "#b3e5fc"

caja =Entry(window, state='disabled', width=40)
caja.grid(row=0,column=3)
btn1 = Button(window,height=1,width =3,text="1", command=partial(insertar,"1"))
btn1.grid(row=1, column=0)
btn2 = Button(window,height=1,width =3,text="2", command=partial(insertar,"2"))
btn2.grid(row=1, column=1)
btn3 = Button(window,height=1,width =3,text="3", command=partial(insertar,"3"))
btn3.grid(row=1, column=2)
btn4 = Button(window,height=1,width =3,text="4", command=partial(insertar,"4"))
btn4.grid(row=2, column=0)
btn5 = Button(window,height=1,width =3,text="5", command=partial(insertar,"5"))
btn5.grid(row=2, column=1)
btn6 = Button(window,height=1,width =3,text="6", command=partial(insertar,"6"))
btn6.grid(row=2, column=2)
btn7 = Button(window,height=1,width =3,text="7", command=partial(insertar,"7"))
btn7.grid(row=3, column=0)
btn8 = Button(window,height=1,width =3,text="8", command=partial(insertar,"8"))
btn8.grid(row=3, column=1)
btn9 = Button(window,height=1,width =3,text="9", command=partial(insertar,"9"))
btn9.grid(row=3, column=2)
btn10 = Button(window,height=1,width =3,text="0", command=partial(insertar,"0"))
btn10.grid(row=4, column=1)

btnsuma = Button(window,height=1,width =4,text="+", command=partial(operador,0,"+"))
btnsuma.grid(row=1, column=3)
btnresta = Button(window,height=1,width =4,text="-", command=partial(operador,1,"-"))
btnresta.grid(row=2, column=3)
btnmultiplicacion = Button(window,height=1,width =4,text="*", command=partial(operador,2,"*"))
btnmultiplicacion.grid(row=3, column=3)
btndivision = Button(window,height=1,width =4,text="/", command=partial(operador,3,"/"))
btndivision.grid(row=4, column=3)

btnigual = Button(window,height=2,width =4,text="=", command=partial(resolver))
btnigual.grid(row=6, column=3)

btnreset = Button(window,height=1,width =4,text="RESET", command=partial(resetear))
btnreset.grid(row=1, column=5)

window.mainloop()

