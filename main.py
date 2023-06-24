import tkinter as tk
from tkinter import ttk
import time
import math
from PIL import ImageGrab
nRes = [1200, 800]
# Dimensiones (ojo, no son coordenadas, es lo que miden los espacios)
# Menu --> 240x800
# Caja Objeto --> 720x500
# Caja Parametros --> 720x300
# Caja de caclulos --> 240x800
# ----------------------------------------------------------#
# Tkinter base
# -----------------------------------------------------------#
win = ctk.CTk()
win._set_appearance_mode('light')
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.iconbitmap('icon.ico')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
fuente = ctk.CTkFont(family='Times New Roman', size=12)
# -----------------------------------------------------------#
# Init Canvas
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

def formulas(*args):
    return
def toggleTheme(): #Not work
    theme = win._get_appearance_mode()
    print(theme)
    if theme == 'light':
        win.set_appearance_mode('dark')
    else:
        win.set_appearance_mode('light')
    win.update()
# -------------------------------------------------------------#
# Funciones Caja
# -------------------------------------------------------------#


def mueveCaja(resultado =0, direccion = 1,velocidad = 1):
    choice = selectVar.get()
    desplazamiento = resultado * 1000
    disRecorrida = 0
    velTime = velocidad / 10000
    print(f'velocidad: {velTime}')
    while disRecorrida < desplazamiento:
        coords = canvasCaja.coords(fig)
        esqDer = coords[2] + direccion
        esqIzq = coords[0] + direccion
        canvasCaja.move(fig, direccion, 0)
        disRecorrida += 1
        if esqDer > 720 or esqIzq < 0:
            posIni()
            break
        canvasCaja.update()
        time.sleep(0.02)
    return


def posIni(movimiento):
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(x1-posI)
        canvasCaja.move(fig, despX, 0)

def PintaLinea(resultado, direccion):
    choice = selectVar.get()
    canvasCaja.delete('linea')
    if resultado:
        canvasCaja.create_line(
            275, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(350, 150, window=labelFN, tags='linea')
        if direccion > 0:
            canvasCaja.create_polygon(
                411, 200, 391, 190, 391, 210, fill='black', tags='linea')
    elif direccion < 0:
        canvasCaja.create_polygon(
            275, 200, 295, 190, 295, 210, fill='black', tags='linea')
    else:
        return
    if choice == 'FDA':
        canvasCaja.create_window(350, 100, window=labelDl, tags='linea')
    return

def stop():
    posIni()
    return

posX = None
def toggleMovManual(*args):
    choice = selectVar.get()
    if choice == 'Manual':
        canvasCaja.bind('<Button-1>', pickBox)
        canvasCaja.bind('<B1-Motion>', moveOn)
        canvasCaja.bind('<ButtonRelease-1>',letItgo)
    else:
        posIni()
        canvasCaja.unbind('<Button-1>')
        canvasCaja.unbind('<B1-Motion>')
        canvasCaja.unbind('<ButtonRelease-1>')
    return

def pickBox(event):
    global posX
    x1,y1,x2,y2 = canvasCaja.coords(fig)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        posX = event.x
    return

desp = 0
def moveOn(event):
    global posX,desp
    if posX is not None:
        x1,y2,x2,y2 = canvasCaja.coords(fig)
        despX = event.x - posX
        newX1 = x1 + despX
        newX2 = x2 + despX
        if newX1 >= 0 and newX2 <= canvasCaja.winfo_width():
            desp = abs(x1-posIniX) 
            labelDl.place(x= 320, y= 200)
            labelDl.configure(text = f'Desplazamiento: {int(desp)} metros')
            calcInv(desp)
            canvasCaja.move(fig,despX,0)
            posX = event.x
            if desp > 260:
                return
    return

def letItgo(event):
    global posX
    posX = None
    return

def calcInv(desplazamiento):
    choice = selectVar.get()
    try:
        fuerza = float(entryF.get())
        trabajo = fuerza * desplazamiento
        print(f'Trabajo: {trabajo}')

    except ValueError:
        msg.showerror(
                'Valores incompletos', 'Porfavor ingresar todos los valores solicitados')
    return
# -------------------------------------------------------------#
# Funciones Parametros
# -------------------------------------------------------------#

coeficiente = 0
def calc():
    global coeficiente
    choice = selectVar.get()
    f = d = aG = aR = m = v = vi = vf = 0
    u = coeficiente
    dire = 1
    rType = 'Resultado'
    rNum = 0
    if choice == 'FDA':
        try:
            f = float(entryF.get())
            d = float(entryD.get())
            aG = float(entryA.get())
            aR = math.radians(aG)
            trabajo = abs(f * d) * math.cos(aR)
            if trabajo < 0:
                dire = -1
            elif trabajo > 0:
                dire = 1
            trabajo = abs(trabajo)
            aR = '{:.4f}'.format(aR)
            rType = 'Trabajo'
            rNum = trabajo
            labelFN.configure(text=f"{rType}: {rNum}")
            labelDl.configure(text=f'Desplazamiento: {d} metros')

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
    posIni()
    canvasCaja.delete('linea')
    widgetsForget = [labelF,entryF,labelD,entryD,labelA,entryA,labelV,entryV,labelM,entryM,labelVf,entryVf,labelVi,entryVi,labelMC,materialCaja,labelMS,materialSuelo,labelRr]
    for widget in widgetsForget:
        widget.place_forget()
    if roce == 1:
        x = [0.4,0.7,0.7,0.6]
        y = [50,80,110,140]
        labelMC.place(relx=0.1, y= 50)
        materialCaja.place(relx=0.1,y= 80)
        labelMS.place(relx=0.1, y=150)
        materialSuelo.place(relx=0.1,y=180)
        labelRr.place(relx=0.1, y=250)
    else:
        x = [0.2,0.5,0.6,0.4]
        y = [50,80,110,140]
    if choice == 'FDA':
        labelF.place(relx = x[0], y = y[0])
        entryF.place(relx = x[0], y = y[1])
        labelD.place(relx = x[2], y = y[0])
        entryD.place(relx = x[2], y = y[1])
        labelA.place(relx = x[3], y = y[2])
        entryA.place(relx = x[3], y = y[3])
    if choice == 'MV':
        labelM.place(relx = x[0], y =  y[0])
        entryM.place(relx = x[0], y =  y[1])
        labelV.place(relx = x[1], y =  y[0])
        entryV.place(relx = x[1], y =  y[1])
    if choice == 'VEc':
        labelVf.place(relx  = x[0], y = y[0])
        entryVf.place(relx  = x[0], y = y[1])
        labelVi.place(relx  = x[2], y = y[0])
        entryVi.place(relx  = x[2], y = y[1])
        labelM.place(relx = x[3], y = y[2])
        entryM.place(relx = x[3], y = y[3])
    if choice == 'Manual':
        labelF.place(relx=0.4,y=70)
        entryF.place(relx=0.4, y = 100)
    return 

# -------------------------------------------------------------#
# Funciones Parametros - Roce
# -------------------------------------------------------------#
def getCoefRoce(event):
    caja = varCaja.get()
    suelo = varSuelo.get()
    coeficiente = 0
    if caja and suelo:
        coeficiente = calcRoce(caja, suelo)
    if coeficiente:
        labelRr.configure(text=f'El coeficiente de roce es {coeficiente}')
    return coeficiente

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