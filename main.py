import tkinter as tk
from tkinter import ttk
import time
import math as ma
import pint as pi
import random as ra
import threading as th

ureg = pi.UnitRegistry()

nRes = [1200, 800]
# Dimensiones (ojo, no son coordenadas, es lo que miden los espacios)
# Menu --> 200x800
# Caja Objeto --> 640x500
# Caja Parametros --> 640x300
# Ambos graficos son de 400x400
# -----------------------------------------------------------#
# Tkinter base
# -----------------------------------------------------------#
win = tk.Tk()
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)

# -----------------------------------------------------------#
# Lienzo del menu
# -----------------------------------------------------------#
canvasMenu = tk.Canvas(win, width=200, height=800)
canvasMenu.place(x=0, y=0)
canvasMenu.create_rectangle(
    0, 0, 200, 800, fill='lightgray', outline=canvasMenu['background'])
# -----------------------------------------------------------#
# Lienzo Caja
# -----------------------------------------------------------#
canvasCaja = tk.Canvas(win, width=640, height=500)
canvasCaja.place(x=201, y=0)
canvasCaja.create_rectangle(
    0, 0, 640, 500, fill='white', outline=canvasMenu['background'])
# Caja
posIniX = 231
posIniY = 250
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 411, 400, fill='red', outline=canvasMenu['background'])
# Suelo
canvasCaja.create_rectangle(
    0, 400, 640, 500, fill='#A18072', outline=canvasMenu['background'])

# Movimiento Caja


def mueveCaja(movimiento):
    desplazamiento = abs(movimiento)
    disRecorrida = 0
    if movimiento > 0:
        direccion = 1
    elif movimiento < 0:
        direccion = -1
    else:
        direccion = 0
    while disRecorrida < desplazamiento:
        coords = canvasCaja.coords(fig)
        if coords[0] <= 0 or coords[2] >= 730:
            posIni(movimiento)
            break
        canvasCaja.move(fig, direccion, 0)
        disRecorrida += 1
        canvasCaja.update()
        time.sleep(0.02)
    return


def posIni(movimiento):
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(coords[0]-posIniX)
        canvasCaja.move(fig, despX, 0)


# Linea Referencia Movimiento
labelFN = ttk.Label(canvasCaja, text='Fuerza Neta')


def PintaLinea(movimiento):
    canvasCaja.delete("linea")
    if movimiento > 0:
        canvasCaja.create_polygon(391, 190, 391, 210, 411, 200, fill='black', tags="linea")
        canvasCaja.create_line(200, 200, 411, 200, fill='black', width=3, tags="linea")
        canvasCaja.create_window(320, 150, window=labelFN)
    elif movimiento < 0:
        canvasCaja.create_line(200, 200, 411, 200, fill='black', width=3, tags="linea")
        canvasCaja.create_polygon(200, 190, 200, 210, 180, 200, fill='black', tags="linea")
    else:
        return
    



# Boton 'Run'
def BtnRun(movimiento):
    posIni(movimiento)
    PintaLinea(movimiento)
    calcular_MV_thread()
    calcular_FDA_thread()
    mueveCaja(movimiento)
    

dis = -150  # Valor de prueba
ButtonRun = tk.Button(canvasCaja, text='Run', command=lambda: BtnRun(dis))
canvasCaja.create_window(320, 450, window=ButtonRun, width=100, height=40)
# -----------------------------------------------------------#
# Lienzo Parametros
# -----------------------------------------------------------#
canvasPmt = tk.Canvas(win, width=640, height=300)
canvasPmt.place(x=201, y=501)
canvasPmt.create_rectangle(
    0, 0, 640, 300, fill='lightblue', outline=canvasMenu['background'])
# Roce
checkRoce = tk.IntVar(value=0)


def getRoce():
    roce = checkRoce.get()
    if roce == 1:
        labelMC.place(x=20, y=50)
        materialCaja.place(x=20, y=80)
        labelMS.place(x=20, y=130)
        materialSuelo.place(x=20, y=160)
        labelR.place(x=20, y=210)
        btnShowTable.place(x=20, y=250)

    else:
        labelMC.place_forget()
        materialCaja.place_forget()
        labelMS.place_forget()
        materialSuelo.place_forget()
        labelR.place_forget()
    return


def showTableR():
    tableWin = tk.Tk()
    tableWin.title('Tabla de Coeficientes de Roce')
    tableR = ttk.Treeview(tableWin, columns=materiales, height=3)
    tableR.heading('#0', text='Material')
    tableR.column('#0', width=80)
    for material in materiales:
        tableR.heading(material, text=material)
        tableR.column(material, width=60)
    for i in range(len(materiales)):
        material = materiales[i]
        tableR.insert('', 'end', text=material, values=coeficientes[i])
    tableR.pack()
    return tableWin


askRoce = ttk.Checkbutton(canvasPmt, text='Roce?',
                          command=getRoce, variable=checkRoce)
askRoce.place(x=50, y=20)
labelMC = ttk.Label(canvasPmt, text='Material Caja')
labelMS = ttk.Label(canvasPmt, text='Material Suelo')
materialCaja = ttk.Combobox(canvasPmt)
materialSuelo = ttk.Combobox(canvasPmt)
labelR = ttk.Label(canvasPmt, text=f'El coeficiente de roce es {0}')
btnShowTable = ttk.Button(
    canvasPmt, text='Mostrar Coeficientes de Roce', command=showTableR)

#-------------------------------------------------------------
# Calculos 
#-------------------------------------------------------------
def calcular_FDA():
        fuerza = float(entryF.get())
        desplazamiento = float(entryD.get())
        angulo = float(entryA.get())
        resultado = fuerza * desplazamiento * angulo
        label_reFDA.config(text="Resultado: " + str(resultado))
        PintaLinea(resultado)
        mueveCaja(resultado)

    
def calcular_MV():
    masa = float(entryM.get())
    velocidad = float(entryV.get())
    resultado = (0.5 * masa) * (velocidad ** 2)
    label_reFDA.config(text="Resultado: " + str(resultado))
    PintaLinea(resultado)
    mueveCaja(resultado)

    
#-------------------------------------------------------------
# Llamada a los calculos
#-------------------------------------------------------------
def calcular_FDA_thread():
    thread = th.Thread(target=calcular_FDA)
    thread.start()
    
    
def calcular_MV_thread():
    thread = th.Thread(target=calcular_MV)
    thread.start()

# ------------------------
materiales = ['Madera', 'Acero', 'Cobre']
coeficientes = [
    [0.45, 0.6, 0.45],
    [0.5, 0.55, 0.4],
    [0.45, 0.4, 0.4]
]
materialCaja = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
materialSuelo = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
labelR = ttk.Label(canvasPmt, text=f'El coeficiente de roce es {0}')

# Resto de Parametros
modos = ['Fuerza, Desplazamiento y Angulo'
         , 'Masa, Velocidad']
modo = ttk.Combobox(canvasPmt, values=modos, state='readonly')
labelModo = ttk.Label(canvasPmt, text='Escoja un modo: ',
                      background='lightblue')
entryF = ttk.Entry(canvasPmt)
entryD = ttk.Entry(canvasPmt)
entryA = ttk.Entry(canvasPmt)
entryM = ttk.Entry(canvasPmt)
entryV = ttk.Entry(canvasPmt)
labelF = ttk.Label(canvasPmt, text='Fuerza (N)')
labelD = ttk.Label(canvasPmt, text='Desplazamiento (mt)')
labelA = ttk.Label(canvasPmt, text='Angulo')
labelM = ttk.Label(canvasPmt, text='Masa (Kg)')
labelV = ttk.Label(canvasPmt, text='Velocidad (mt/s**2)')
label_reFDA = ttk.Label(canvasPmt, text="Resultado:")




modo.place(x=350, y=20)
labelModo.place(x=250, y=20)


def refreshPmt(event):
    choice = modo.get()
    if choice == 'Fuerza, Desplazamiento y Angulo':
        labelF.place(x=350, y=70)
        entryF.place(x=350, y=100)
        labelD.place(x=350, y=150)
        entryD.place(x=350, y=180)
        labelA.place(x=350, y=230)
        entryA.place(x=350, y=260)
        label_reFDA.place(x=520, y=215)
        labelM.place_forget()
        labelV.place_forget()
        entryM.place_forget()
        entryV.place_forget()

    elif choice == 'Masa, Velocidad':
        labelM.place(x=350, y=70)
        entryM.place(x=350, y=100)
        labelV.place(x=350, y=150)
        entryV.place(x=350, y=180)
        label_reFDA.place(x=520, y=215)
        labelF.place_forget()
        labelD.place_forget()
        labelA.place_forget()
        entryA.place_forget()
        entryF.place_forget()
        entryD.place_forget()
        

        

modo.bind('<<ComboboxSelected>>', refreshPmt)

# -----------------------------------------------------------#
# Ciclo Principal
# -----------------------------------------------------------#
win.mainloop()