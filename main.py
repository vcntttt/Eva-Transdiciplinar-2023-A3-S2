import tkinter as tk 
from tkinter import ttk,Frame,Button
import tkinter as tk
from tkinter import messagebox as msg
import customtkinter as ctk
import time
import math
from PIL import ImageGrab,Image, ImageTk
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
    while disRecorrida < desplazamiento:
        coords = canvasCaja.coords(fig)
        esqDer = coords[2] + direccion
        esqIzq = coords[0] + direccion
        canvasCaja.move(fig, direccion, 0)
        disRecorrida += 1
        if esqDer > 640 or esqIzq < 0:
            posIni()
            break
        canvasCaja.update()
        time.sleep(velTime)
    return


def BtnRun():
    resultado = float(calc()[9])
    direccion = float(calc()[10])
    posIni()
    PintaLinea(resultado,direccion)
    mueveCaja(direccion)


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


def PintaLinea(resultado,direccion):
    choice = selectVar.get()
    if choice == 'FDA':
        Label_imagen.place(x=0,y=300)
        Label_imagen_2.place_forget()
        Label_imagen_3.place_forget()
    elif choice == 'MV':
        Label_imagen_2.place(x=0,y=300)
        Label_imagen.place_forget()
        Label_imagen_3.place_forget()
    elif choice == 'MVF-MVI':
        Label_imagen_3.place(x=0,y=300)
        Label_imagen.place_forget()
        Label_imagen_2.place_forget()
    return formulas



checkbox_var = tk.IntVar(value = 0)

formula = ttk.Checkbutton(canvasTyEc, text='Modelo Matematico',command=formulas, variable=checkbox_var,bootstyle='round-toggle')
formula.place(x=30,y=400)

materiales = ['Madera', 'Acero', 'Cobre']
materialCaja = ttk.Combobox(canvasPmt, values=materiales, state='readonly')

#-------------------------------------------------------------#
# 
#-------------------------------------------------------------#
def PintaLinea(movimiento):
    canvasCaja.delete('linea')
    if movimiento:
        canvasCaja.create_line(
            275, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(350, 150, window=labelFN)
    if choice == 'FDA': labelDl.place(x=250,y=100)
    if direccion > 0:
        canvasCaja.create_polygon(
            411, 200, 391, 190, 391, 210, fill='black', tags='linea')
    elif direccion < 0:
        canvasCaja.create_polygon(
            275, 200, 295, 190, 295, 210, fill='black', tags='linea')
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
    choice = refreshPmt()
    f = d = aG = aR = m = v = vi = vf = 0
    dire = 1
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
            trabajo = abs(f * d) * math.cos(aR)
            if trabajo < 0:
                dire = -1
            elif trabajo > 0:
                dire = 1
            trabajo = abs(trabajo)
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
        labelFN.configure(text=f'{rType}: {resultadoF} Joules')
        rNum = resultadoF
    else:
        labelFN.configure(text=f'{rType}: {int(rNum)} J')
    valores = [f, d, aG, aR, m, v, vi, vf, rType, rNum,dire]
    return valores


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
        labelF.place(x=100, y=60)
        entryF.place(x=81, y=90)
        labelD.place(x=290, y=60)
        entryD.place(x=294, y=90)
        labelA.place(x=525, y=60)
        entryA.place(x=507, y=90)
        entryM.place_forget()
        entryV.place_forget()
        labelM.place_forget()
        labelV.place_forget()
        LabelVi.place_forget()
        entryVi.place_forget()
        LabelVf.place_forget()
        entryVf.place_forget()
    elif choice == 'MV':
        labelM.place(x=180, y=60)
        entryM.place(x=152, y=90)
        labelV.place(x=436, y=60)
        entryV.place(x=436, y=90)
        labelF.place_forget()
        entryF.place_forget()
        labelD.place_forget()
        entryD.place_forget()
        labelA.place_forget()
        entryA.place_forget()
        LabelVi.place_forget()
        entryVi.place_forget()
        LabelVf.place_forget()
        entryVf.place_forget()
    elif choice == 'MVF-MVI':
        labelM.place(x=109, y=60)
        entryM.place(x=81, y=90)
        LabelVi.place(x=270, y=60)
        entryVi.place(x=294, y=90)
        LabelVf.place(x=490, y=60)
        entryVf.place(x=507, y=90)
        labelF.place_forget()
        entryF.place_forget()
        labelD.place_forget()
        entryD.place_forget()
        labelA.place_forget()
        entryA.place_forget()
        entryV.place_forget()
        labelV.place_forget()
        labelA.place_forget()
        entryA.place_forget()
    return choice


# -------------------------------------------------------------#
# Elementos Menu
# -------------------------------------------------------------#
labelTitleM = ttk.Label(canvasMenu, text='Menu',
                        font=('Times new roman', 20), foreground='white', background='#2f3123')
labelTitleM.place(relx=0.5, anchor='center', y=50)
btnSS = ttk.Button(canvasMenu, text="Screenshot", command=screenshot)
btnSS.place(relx=0.5, anchor='center', y=130)
# Modelo Matematico
labelTitleFT = ttk.Label(canvasMenu, text='Del Trabajo', font=('Times new roman', 18),
                         foreground='white', background='#2f3123')
labelTitleFEc = ttk.Label(canvasMenu, text='De Energia Cinetica', font=('Times new roman', 18),
                          foreground='white', background='#2f3123')
labelTitleVE = ttk.Label(canvasMenu, text='Variacion de energia', font=('Times new roman', 18),
                         foreground='white', background='#2f3123')
FT = ttk.Label(canvasMenu, text='W = | F | x | D | x cos a°', font=('Times new roman', 18),
               foreground='white', background='#2f3123')
FEc = ttk.Label(canvasMenu, text='Ec = ½m V²', font=('Times new roman', 18),
                foreground='white', background='#2f3123')
FWEc = ttk.Label(canvasMenu, text='W = ∆Ec', font=('Times new roman', 18),
                 foreground='white', background='#2f3123')
VEc = ttk.Label(canvasMenu, text='∆Ec = Ecf - Eci', font=('Times new roman', 18),
                foreground='white', background='#2f3123')
VEc_2 = ttk.Label(canvasMenu, text='∆Ec = ½m Vf² - ½m Vi²', font=('Times new roman', 18),
                  foreground='white', background='#2f3123')

labelTitleD = ttk.Label(canvasMenu, text='Donde: \n•W = Trabajo\n•F = Fuerza\n•D = Distancia\n•a = angulo',
                        font=('Times new roman', 15), foreground='white', background='#2f3123')
labelTitleD_1 = ttk.Label(canvasMenu, text='Donde: \n•Ec = Energia Cinetica\n•m = Masa\n•V = Velocidad\n',
                          font=('Times new roman', 15), foreground='white', background='#2f3123')
labelTitleD_2 = ttk.Label(canvasMenu, text='Donde: \n•∆Ec = Variacion\nde energia cinetica\n•Ecf = Energia\nCinetica Final\n•Eci = Energia\nCinetica Inicial\n•m = Masa\n•Vf = Velociad final\n•Vi = Velocidad Inicial',
                          font=('Times new roman', 15), foreground='white', background='#2f3123')
# -------------------------------------------------------------#
# Elementos Caja
# -------------------------------------------------------------#
posIniX = 271
posIniY = 250
labelFN = ttk.Label(canvasCaja, text='',
                    font=('Times new roman', 15))
labelDl = ttk.Label(canvasCaja,text='Desplazamiento: ',font=('Times new roman',15))
ButtonRun = ttk.Button(canvasCaja, text='Run', command=BtnRun, style='primary')
canvasCaja.create_window(360, 450, window=ButtonRun, width=100, height=40)
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 451, 400, fill='#ff6a36', outline='#ff6a36')
# -------------------------------------------------------------#
# Elementos Parametros
# -------------------------------------------------------------#
entryF = ttk.Entry(canvasPmt)
entryD = ttk.Entry(canvasPmt)
entryA = ttk.Entry(canvasPmt)
entryM = ttk.Entry(canvasPmt)
entryV = ttk.Entry(canvasPmt)
entryVi = ttk.Entry(canvasPmt)
entryVf = ttk.Entry(canvasPmt)
labelF = ttk.Label(canvasPmt, text='Fuerza (N)', font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
labelD = ttk.Label(canvasPmt, text='Desplazamiento (m)', font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
labelA = ttk.Label(canvasPmt, text='Angulo (°) ', font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
labelM = ttk.Label(canvasPmt, text='Masa (kg)', font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
labelV = ttk.Label(canvasPmt, text='Velocidad (m/s²)', font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
labelR = ttk.Label(canvasPmt, text="Resultado:", font=('Times new roman', 15),
                   foreground='black', background='#f1cc7a')
LabelVi = ttk.Label(canvasPmt, text='Velocidad Inicial (m/s²)', font=('Times new roman', 15),
                    foreground='black', background='#f1cc7a')
LabelVf = ttk.Label(canvasPmt, text='Velocidad Final (m/s²)', font=('Times new roman', 15),
                    foreground='black', background='#f1cc7a')
# -------------------------------------------------------------#
# Elementos Menu Calculos
# -------------------------------------------------------------#
labelTitleTyEc = ttk.Label(canvasTyEc, text='¿Que desea calcular?', font=('Times new roman', 20),
                           foreground='white', background='#2f3123')
labelTitleTyEc.place(relx=0.5, anchor='center', y=50)

labelTitleC = ttk.Label(canvasCaja, text='TRABAJO Y ENERGIA', font=('Times new roman', 25),
                        foreground='black')
labelTitleC.place(relx=0.5, anchor='center', y=50)
selectVar = tk.StringVar()
rbtn1 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Trabajo : ', value='FDA', variable=selectVar, command=formulas)
rbtn2 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Energia Cinetica: ', value='MV', variable=selectVar, command=formulas)
rbtn3 = ttk.Radiobutton(
    canvasTyEc, text='Variacion de energia: ', value='MVF-MVI', variable=selectVar, command=formulas)
rbtn1.place(x=30, y=100)
rbtn2.place(x=30, y=140)
rbtn3.place(x=30, y=180)
selectVar.trace('w', refreshPmt)
win.mainloop()