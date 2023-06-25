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
frameMenu = ctk.CTkFrame(win, fg_color='#2f3123', width=240, height=800)
frameMenu.place(x=0, y=0)
canvasCaja = tk.Canvas(win, width=720, height=500)
canvasCaja.place(x=240, y=0)
framePmt = ctk.CTkFrame(win, fg_color='#f1cc7a',
                        width=720, height=300, corner_radius=0)
framePmt.place(x=240, y=500)
frameMenuCalc = ctk.CTkFrame(
    win, fg_color='#2f3123', width=240, height=800, corner_radius=0)
frameMenuCalc.place(x=960, y=0)
# -------------------------------------------------------------#
# Funciones Menu
# -------------------------------------------------------------#
contador = 1


def screenshot():
    global contador
    x = win.winfo_rootx()
    y = win.winfo_rooty()
    captura = ImageGrab.grab(bbox=(x, y, x+nRes[0], y+nRes[1]))
    captura.save(f'captura_{contador}.png')
    contador += 1
    return


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


def mueveCaja(movimiento = 0, direccion = 1,velocidad = 1):
    choice = selectVar.get()
    desplazamiento = movimiento * 1000
    disRecorrida = 0
    maxVelTime = 0.2
    minVelTime = 0.00002
    if choice == "FDA" or choice == 'MV':
        rango = maxVelTime - minVelTime
        escala = velocidad / (velocidad + 1)
        velTime = maxVelTime - (rango * escala)
    elif choice == "VEc":
        velTime = velocidad
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
        time.sleep(velTime)
    return

def BtnRun():
    choice = selectVar.get()
    roce = checkRoce.get()
    if choice != 'Manual':
        posIni()
        values, parametros = calc()
        resultado = float(parametros[1])
        movimiento = float(parametros[3])
        direccion = float(parametros[2])
        velocidad = float(parametros[4])
        PintaLinea(movimiento, direccion)
        mueveCaja(movimiento, direccion, velocidad)
    else:
        return

def posIni():
    choice = selectVar.get()
    x1,y1,x2,y2 = canvasCaja.coords(fig)
    posI = 0
    if choice == 'FDA' or choice == 'MV':
        posI = posIniX
    elif choice == 'VEc' or choice == 'Manual':
        posI = 0
    else:
        posI = posIniX
    if x1 != posI:            
        if x1 > posI:
            despX = -(abs(x1-posI))
        else:
            despX = abs(x1-posI)
        canvasCaja.move(fig, despX, 0)

def PintaLinea(movimiento, direccion):
    choice = selectVar.get()
    canvasCaja.delete('linea')
    if movimiento:
        canvasCaja.create_line(
            275, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(350, 150, window=labelFN, tags='linea')
        if direccion > 0:
                canvasCaja.create_polygon(
                    411, 200, 391, 190, 391, 210, fill='black', tags='linea')
        elif direccion < 0:
            canvasCaja.create_polygon(
                275, 200, 295, 190, 295, 210, fill='black', tags='linea')
        if choice == 'FDA':
            canvasCaja.create_window(350, 100, window=labelDl, tags='linea')
    else:
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

def calc():
    global coeficiente
    choice = selectVar.get()
    f = d = aG = aR = m = v = vi = vf = 0
    g = 9.8
    u = coeficiente
    print(f'Coeficiente de Roce: {u}')
    rad180 = math.radians(180)
    rType = 'Resultado'
    rNum = 0
    dire = 1
    movimiento = velocidad = 0
    if choice == 'FDA':
        try:
            f = float(entryF.get())
            d = float(entryD.get())
            aG = float(entryA.get())
            aR = math.radians(aG)
            if u != 0:
                m = float(entryM.get())
                print('Pumba roce')
                w = f * d * math.cos(aR)
                wFr = u * m * g * d * math.cos(rad180)
                wNeto = w + wFr
                print(f'Trabajo del roce: {wFr}')
                print(f'Trabajo: {w}')
                print(f'neto: {wNeto}')
                if wNeto < 0:
                    movimiento = 0
                    print('Se necesita aplicar mas fuerza')
                # Fuerza necesaria para Movimiento
                    fMov = 0
                else:
                    movimiento = d
                    velocidad = f
                
            else:
                wNeto = abs(f * d) * math.cos(aR)
                movimiento = d
                velocidad = f
            if wNeto < 0:
                dire = -1
            elif wNeto > 0:
                dire = 1
            aR = '{:.4f}'.format(aR)
            rType = 'Trabajo'
            rNum = wNeto
            labelFN.configure(text=f"{rType}: {rNum}")
            labelDl.configure(text=f'Desplazamiento: {d} metros')
        except ValueError:
            msg.showerror(
                'Valores incompletos', 'Porfavor ingresar todos los valores solicitados')
    elif choice == 'MV':
        try:
            m = float(entryM.get())
            v = float(entryV.get())
            eC = (0.5 * m) * (v ** 2)
            if v < 0:
                dire = -1
            elif v > 0:
                dire = 1
            eC = abs(eC)
            movimiento = eC
            velocidad = v
            rType = 'Energia Cinetica'
            rNum = eC
            labelR.configure(text=f"{rType}: {rNum}")
        except ValueError:
            msg.showerror(
                'Valores incompletos', 'Porfavor ingresar todos los valores solicitados')
    elif choice == 'VEc':
        try:
            m = float(entryM.get())
            vf = float(entryVf.get())
            vi = float(entryVi.get())
            eCf = (0.5 * m) * (vf ** 2)
            eCi = (0.5 * m) * (vi ** 2)
            if u != 0:
                w = eCf - eCi
                wNeto = w - wFr
            else:
                wNeto = eCf - eCi
            rType = 'Variacion de energia'
            rNum = wNeto
            labelR.configure(text=f"{rType}: {rNum}")
        except ValueError:
            msg.showerror(
                'Valores incompletos', 'Porfavor ingresar todos los valores solicitados')
    if int(rNum) != rNum:
        resultadoF = '{:.2f}'.format(rNum)
        labelFN.configure(text=f'{rType}: {resultadoF} J')
        rNum = resultadoF
    else:
        labelFN.configure(text=f'{rType}: {int(rNum)} J')
    valores = [f, d, aG, aR, m, v, vi, vf]
    parametros = [rType, rNum, dire, movimiento, velocidad]
    return valores, parametros


def refreshPmt(*args):
    choice = selectVar.get()
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
        if roce == 1:
            labelM.place(relx = x[0], y = y[2])
            entryM.place(relx = x[0], y = y[3])
            labelA.place(relx = x[2], y = y[2])
            entryA.place(relx = x[2], y = y[3])
        else:
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
    global coeficiente
    caja = varCaja.get()
    suelo = varSuelo.get()
    coeficiente = 0
    if caja and suelo:
        coeficiente = calcRoce(caja, suelo)
    if coeficiente:
        labelRr.configure(text=f'El coeficiente de roce es {coeficiente}')
    return coeficiente

def calcRoce(caja, suelo):
    roceDict = {
        ('Madera', 'Madera'): 0.45,
        ('Madera', 'Acero'): 0.5,
        ('Madera', 'Cobre'): 0.45,
        ('Acero', 'Madera'): 0.5,
        ('Acero', 'Acero'): 0.55,
        ('Acero', 'Cobre'): 0.4,
        ('Cobre', 'Madera'): 0.45,
        ('Cobre', 'Acero'): 0.4,
        ('Cobre', 'Cobre'): 0.4
    }
    return roceDict[(caja, suelo)]
# -------------------------------------------------------------#
# Elementos Menu
# -------------------------------------------------------------#
labelTitleM = ctk.CTkLabel(frameMenu, text='Menu',
                            text_color='white')
labelTitleM.place(relx=0.5, anchor='center', y=50)
btnSS = ctk.CTkButton(frameMenu, text="Screenshot", command=screenshot)
btnSS.place(relx=0.5, anchor='center', y=130)
btnRun = ctk.CTkButton(frameMenu, text='Run', command=BtnRun)
btnStop = ctk.CTkButton(frameMenu,text='Detener',command=stop)
btnRun.place(relx=0.5, y=180, anchor='center')
btnStop.place(relx = 0.5,y = 230,anchor = 'center')
# Modelo Matematico
# -------------------------------------------------------------#
# Elementos Caja
# -------------------------------------------------------------#
posIniX = 271
posIniY = 250
labelTitleC = ctk.CTkLabel(canvasCaja, text='TRABAJO Y ENERGIA', 
                           text_color='black')
labelFN = ctk.CTkLabel(canvasCaja, text='',
                        text_color='black')
labelDl = ctk.CTkLabel(canvasCaja, text='Desplazamiento: ', font=(
    'Times new roman', 15), text_color='black')
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 451, 400, fill='#ff6a36')
suelo = canvasCaja.create_rectangle(0,400,720,500,fill='#A18072',outline='#A18072')
switchTheme = ctk.CTkSwitch(canvasCaja, text='Modo Oscuro',command=toggleTheme,text_color='black')
# switchTheme.place(relx=0.8, y=80, anchor='center')
# -------------------------------------------------------------#
# Elementos Parametros
# -------------------------------------------------------------#
entryF = ctk.CTkEntry(framePmt)
entryD = ctk.CTkEntry(framePmt)
entryA = ctk.CTkEntry(framePmt)
entryM = ctk.CTkEntry(framePmt)
entryV = ctk.CTkEntry(framePmt)
entryVi = ctk.CTkEntry(framePmt)
entryVf = ctk.CTkEntry(framePmt)
labelF = ctk.CTkLabel(framePmt, text='Fuerza (N)', 
                      text_color='black', fg_color='#f1cc7a')
labelD = ctk.CTkLabel(framePmt, text='Desplazamiento (m)', 
                      text_color='black', fg_color='#f1cc7a')
labelA = ctk.CTkLabel(framePmt, text='Angulo (°) ', 
                      text_color='black', fg_color='#f1cc7a')
labelM = ctk.CTkLabel(framePmt, text='Masa (kg)', 
                      text_color='black', fg_color='#f1cc7a')
labelV = ctk.CTkLabel(framePmt, text='Velocidad (m/s²)', 
                      text_color='black', fg_color='#f1cc7a')
labelR = ctk.CTkLabel(framePmt, text="Resultado:", 
                      text_color='black', fg_color='#f1cc7a')
labelVi = ctk.CTkLabel(framePmt, text='Velocidad Inicial (m/s²)', 
                       text_color='black', fg_color='#f1cc7a')
labelVf = ctk.CTkLabel(framePmt, text='Velocidad Final (m/s²)', 
                       text_color='black', fg_color='#f1cc7a')
# -------------------------------------------------------------#
# Elementos Menu Calculos
# -------------------------------------------------------------#
labelTitleTyEc = ctk.CTkLabel(frameMenuCalc, text='¿Que desea calcular?', 
                              text_color='white', fg_color='#2f3123')

selectVar = tk.StringVar()
toggleManual = tk.IntVar()
checkRoce = tk.IntVar(value=0)
rbtn1 = ctk.CTkRadioButton(
    frameMenuCalc, text='Calcular Trabajo : ', value='FDA', variable=selectVar)
rbtn2 = ctk.CTkRadioButton(
    frameMenuCalc, text='Calcular Energia Cinetica: ', value='MV', variable=selectVar)
rbtn3 = ctk.CTkRadioButton(
    frameMenuCalc, text='Variacion de energia: ', value='VEc', variable=selectVar)
rbtn4 = ctk.CTkRadioButton(
    frameMenuCalc, text='Desplazamiento manual',variable=selectVar,value='Manual')
rbtn5 = ctk.CTkSwitch(frameMenuCalc,text='Implementar Roce', variable=checkRoce)
labelTitleC.place(relx=0.5, anchor='center', y=50)
labelTitleTyEc.place(relx=0.5, anchor='center', y=50)
rbtn1.place(x=30, y=100)
rbtn2.place(x=30, y=140)
rbtn3.place(x=30, y=180)
rbtn4.place(x=30, y=220)
rbtn5.place(x=30, y=260)
selectVar.trace('w', refreshPmt)
selectVar.trace('w', formulas)
selectVar.trace('w', toggleMovManual)
checkRoce.trace('w', refreshPmt)
# -------------------------------------------------------------#
# Elementos Roce
# -------------------------------------------------------------#
varCaja = tk.StringVar()
varSuelo = tk.StringVar()
materiales = ['Madera', 'Acero', 'Cobre']
labelMC = ctk.CTkLabel(framePmt, text='Material Caja',text_color='black')
labelMS = ctk.CTkLabel(framePmt, text='Material Suelo',text_color='black')
materialCaja = ctk.CTkComboBox(framePmt, values=materiales, state='readonly',command=getCoefRoce,variable=varCaja)
materialSuelo = ctk.CTkComboBox(framePmt, values=materiales, state='readonly',command=getCoefRoce,variable=varSuelo)
labelRr = ctk.CTkLabel(framePmt, text=f'El coeficiente de roce es {0}',text_color='black')
win.mainloop()