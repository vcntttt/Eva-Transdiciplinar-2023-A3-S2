import PyAutoGUI
import tkinter as tk
from tkinter import ttk
import time
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
canvasMenu.create_text(
    107, 90, text="MENU", fill="black", font=('Helvetica 15 bold'))
boton = ttk.Button(text="Boton Que Imprima")
boton.place(x=50, y=130)
def captura():
    PyAutoGUI.screenshot()
    captura.save("screenshot.png")


boton2 = ttk.Button(text="Boton Screenshot", command=captura)
boton2.place(x=55, y=200)
canvasMenu.create_text(
    107, 300, text= "Se Aceptan Ideas ;)", fill="green", font=("helvetica 15 bold"))    

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
    if movimiento > 0:
        canvasCaja.create_polygon(411, 200, 391, 190, 391, 210, fill='black')
        canvasCaja.create_line(200, 200, 411, 200, fill='black', width=3)
        canvasCaja.create_window(320, 150, window=labelFN)
    elif movimiento < 0:
        canvasCaja.create_line(200, 200, 411, 200, fill='black', width=3)
        canvasCaja.create_polygon(180, 200, 200, 190, 200, 210, fill='black')
    else:
        return
    return


# Boton 'Run'
def BtnRun(movimiento):
    posIni(movimiento)
    PintaLinea(movimiento)
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
win.mainloop()
