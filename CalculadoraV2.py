from tkinter import *

# inicio de proyecto calculadora

ventana = Tk()
ventana.title('Calculadora V2 - Gustavo Colmenares')
ventana.config(bg='#2C3333')

# FUNCIONES
E = 0
# PULSADO DE BOTONES
def click(num):
    global E
    ECUACION.insert(E, num)
    E += 1


# BORRADO
def borrar():
    ECUACION.delete(0, END)
    RESULTADO.delete(0, END)
    E = 0


# OPERACIONES MATEMÁTICAS
def operacion():
    global E
    try:
        ecuacion = ECUACION.get()
        resultado = eval(ecuacion)
        RESULTADO.delete(0, END)
        RESULTADO.insert(0, float(resultado))
        E = 0
    except SyntaxError:
        return None


# --- FRAME 1 ECUACION -------------------------------------
Frame1= Frame(ventana, bg='#2C3333')
Frame1.pack()

ECUACION= Entry(Frame1, bg='#2C3333', width=35, font=('Arial', 10), fg='#395B64', justify="right", borderwidth=0)
ECUACION.grid(row=0, padx=3, pady=3)



# --- FRAME 2 RESULTADO ------------------------------------
Frame2= Frame(ventana, bg='#2C3333')
Frame2.pack()

RESULTADO= Entry(Frame2, bg='#2C3333', width=16, font=('Arial', 20), fg='#395B64', justify="right", borderwidth=0)
RESULTADO.grid(row=0, rowspan=2, padx=3, pady=5)


# --- FRAME 3 BOTONES ---------------------------------------

Frame3= Frame(ventana, bg='#2C3333')
Frame3.pack()

# ------- FILA 1 -------
botonC= Button(Frame3, bg='#2666CF', font=('Arial', 9), 
    width=7, height=2, borderwidth=0, text='C', command= lambda: borrar())
botonC.grid(row=0, column=0, padx=5, pady=5)

botonP1= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='(', command=lambda: click("("))
botonP1.grid(row=0, column=1, padx=5, pady=5)

botonP2= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text=')', command=lambda: click(")"))
botonP2.grid(row=0, column=2, padx=5, pady=5)

botonDiv= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='/', command=lambda: click("/"))
botonDiv.grid(row=0, column=3, padx=5, pady=5)


# ------- FILA 2 -------
boton7= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='7', command=lambda: click("7"))
boton7.grid(row=1, column=0, padx=5, pady=5)

boton8= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='8', command=lambda: click("8"))
boton8.grid(row=1, column=1, padx=5, pady=5)

boton9= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='9', command=lambda: click("9"))
boton9.grid(row=1, column=2, padx=5, pady=5)

botonMult= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='x', command=lambda: click("*"))
botonMult.grid(row=1, column=3, padx=5, pady=5)


# ------- FILA 3 -------
boton4= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='4')
boton4.grid(row=2, column=0, padx=5, pady=5)

boton5= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='5')
boton5.grid(row=2, column=1, padx=5, pady=5)

boton6= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='6')
boton6.grid(row=2, column=2, padx=5, pady=5)

botonRes= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='-')
botonRes.grid(row=2, column=3, padx=5, pady=5)


# ------- FILA 4 -------
boton1= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='1')
boton1.grid(row=3, column=0, padx=5, pady=5)

boton2= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='2')
boton2.grid(row=3, column=1, padx=5, pady=5)

boton3= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='3')
boton3.grid(row=3, column=2, padx=5, pady=5)

botonMas= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='+')
botonMas.grid(row=3, column=3, padx=5, pady=5)


# ------- FILA 5 -------
boton0= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='0')
boton0.grid(row=3, column=0, padx=5, pady=5)

botonPunto= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='°')
botonPunto.grid(row=3, column=1, padx=5, pady=5)

botonBorra= Button(Frame3, bg='#395B64', font=('Arial', 9), width=7, height=2, borderwidth=0, text='<')
botonBorra.grid(row=3, column=2, padx=5, pady=5)

botonIgual= Button(Frame3, bg='#2666CF', font=('Arial', 9), width=7, height=2, borderwidth=0, text='=')
botonIgual.grid(row=3, column=3, padx=5, pady=5)


ventana.mainloop()