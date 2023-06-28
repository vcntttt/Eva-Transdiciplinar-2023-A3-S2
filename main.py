import tkinter as tk
from tkinter import messagebox as msg
import customtkinter as ctk
import time
import math
from PIL import ImageGrab
nRes = [1200, 800]
coeficiente = 0
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
        if esqDer > 720 or esqIzq < 0:
            posIni()
            break
        canvasCaja.update()
        time.sleep(0.02)
    return
def BtnRun():
    choice = selectVar.get()
    roce = checkRoce.get()
    if choice == 'Manual':
        return
    posIni()
    values, parametros = calc()
    movimiento,direccion, velocidad = map(float, parametros[2:5])
    vi = vf = 0
    PintaLinea(movimiento, direccion)
    if choice == 'VEc':
        vi, vf = map(float, values[6:8])
        mueveCajaVEc(direccion, vi, vf)
    else:
        mueveCaja(direccion, velocidad)


def posIni(movimiento):
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(x1-posI)
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
    calcular_MV_thread()
    calcular_FDA_thread()
    calcular_FD_thread()
    mueveCaja(movimiento)
    



coeficiente = 0
def calc():
    global coeficiente
    choice = selectVar.get()
    f = d = aG = aR = m = v = vi = vf = pi = pf = 0
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
    if roce == 1:
        x = [0.4,0.7,0.7,0.6]
        y = [50,80,110,140]
        labelMC.place(relx=0.1, y= 50)
        materialCaja.place(relx=0.1,y= 80)
        labelMS.place(relx=0.1, y=150)
        materialSuelo.place(relx=0.1,y=180)
        labelRr.place(relx=0.1, y=250)
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

def calcular_FD():
    fuerza = float(entryF.get())
    desplazamiento = float(entryD.get())
    resultado = fuerza * desplazamiento
    label_reFDA.config(text="Resultado: " + str(resultado))
    
def calcular_MV():
    masa = float(entryM.get())
    velocidad = float(entryV.get())
    resultado = (0.5 * masa) * (velocidad ** 2)
    label_reFDA.config(text="Resultado: " + str(resultado))
    
#-------------------------------------------------------------
# Llamada a los calculos
#-------------------------------------------------------------
def calcular_FDA_thread():
    thread = th.Thread(target=calcular_FDA)
    thread.start()
    
def calcular_FD_thread():
    thread = th.Thread(target=calcular_FD)
    thread.start()
    
def calcular_MV_thread():
    thread = th.Thread(target=calcular_MV)
    thread.start()

# ------------------------
materiales = ['Madera', 'Acero', 'Cobre']
labelMC = ctk.CTkLabel(framePmt, text='Material Caja',text_color='black')
labelMS = ctk.CTkLabel(framePmt, text='Material Suelo',text_color='black')
materialCaja = ctk.CTkComboBox(framePmt, values=materiales, state='readonly',command=getCoefRoce,variable=varCaja)
materialSuelo = ctk.CTkComboBox(framePmt, values=materiales, state='readonly',command=getCoefRoce,variable=varSuelo)
labelRr = ctk.CTkLabel(framePmt, text=f'El coeficiente de roce es {0}',text_color='black')
win.mainloop()