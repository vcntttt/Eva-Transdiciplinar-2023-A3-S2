import tkinter as tk
from tkinter import messagebox as msg
# import ttkbootstrap as ttk
import customtkinter as ctk
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
# -----------------------------------------------------------#
# Init Canvas
# -----------------------------------------------------------#
frameMenu = ctk.CTkFrame(win,fg_color='#2f3123',width=240,height=800)
frameMenu.place(x=0,y=0)
frameCaja = ctk.CTkFrame(win,fg_color='#A18072',width=720,height=500,corner_radius=0)
frameCaja.place(x=240,y=0)
canvasCaja = tk.Canvas(win, width=720, height=400)
canvasCaja.place(x=241, y=0)
framePmt = ctk.CTkFrame(win,fg_color='#f1cc7a',width=720,height=300,corner_radius=0)
framePmt.place(x=240,y=500)
frameMenuCalc = ctk.CTkFrame(win,fg_color='#2f3123', width=240, height=800,corner_radius=0)
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


def formulas():
    labelTitleMM = ctk.CTkLabel(frameMenu, text='Modelo Matematico', font=('Times new roman', 18),
                             text_color='white', fg_color='#2f3123')
    labelTitleMM.place(relx=0.5, anchor='center', y=280)
    choice = selectVar.get()
    if choice == 'FDA':
        labelTitleFT.place(relx=0.5, anchor='center', y=320)
        FT.place(relx=0.5, anchor='center', y=380)
        labelTitleD.place(x=10, y=420)
        labelTitleFEc.place_forget()
        labelTitleVE.place_forget()
        FEc.place_forget()
        FWEc.place_forget()
        VEc.place_forget()
        VEc_2.place_forget()
        labelTitleD_1.place_forget()
        labelTitleD_2.place_forget()
    elif choice == 'MV':
        labelTitleFEc.place(relx=0.5, anchor='center', y=320)
        FEc.place(relx=0.5, anchor='center', y=380)
        labelTitleD_1.place(x=10, y=420)
        labelTitleFT.place_forget()
        labelTitleVE.place_forget()
        FT.place_forget()
        FWEc.place_forget()
        VEc.place_forget()
        VEc_2.place_forget()
        labelTitleD.place_forget()
        labelTitleD_2.place_forget()
    elif choice == 'MVF-MVI':
        labelTitleVE.place(relx=0.5, anchor='center', y=320)
        FWEc.place(relx=0.5, anchor='center', y=380)
        VEc.place(relx=0.5, anchor='center', y=420)
        VEc_2.place(relx=0.5, anchor='center', y=460)
        labelTitleD_2.place(x=10, y=510)
        labelTitleFEc.place_forget()
        labelTitleFT.place_forget()
        FEc.place_forget()
        FT.place_forget()
        labelTitleD.place_forget()
        labelTitleD_1.place_forget()
    return formulas

# -------------------------------------------------------------#
# Funciones Caja
# -------------------------------------------------------------#


def mueveCaja(resultado,direccion):
    desplazamiento = resultado * 1000
    disRecorrida = 0
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
        time.sleep(0.01)
    return


def BtnRun():
    resultado = float(calc()[9])
    direccion = float(calc()[10])
    posIni()
    PintaLinea(resultado,direccion)
    mueveCaja(resultado,direccion)


def posIni():
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(coords[0]-posIniX)
        canvasCaja.move(fig, despX, 0)


def PintaLinea(resultado,direccion):
    choice = selectVar.get()
    canvasCaja.delete('linea')
    if resultado:
        canvasCaja.create_line(
            275, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(350, 150, window=labelFN,tags='linea')
        if direccion > 0:
            canvasCaja.create_polygon(
            411, 200, 391, 190, 391, 210, fill='black', tags='linea')
    elif direccion < 0:
        canvasCaja.create_polygon(
            275, 200, 295, 190, 295, 210, fill='black', tags='linea')
    else:
        return
    if choice == 'FDA': 
        canvasCaja.create_window(350,100,window=labelDl,tags='linea')

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
    elif choice == 'MVF-MVI':
        try:
            m = float(entryM.get())
            vf = float(entryVf.get())
            vi = float(entryVi.get())
            eCf = (0.5 * m) * (vf ** 2)
            eCi = (0.5 * m) * (vi ** 2)
            VE = eCf - eCi
            rType = 'Variacion de energia'
            rNum = VE
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
    valores = [f, d, aG, aR, m, v, vi, vf, rType, rNum,dire]
    return valores


def refreshPmt(*args):
    choice = selectVar.get()
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
        labelVi.place_forget()
        entryVi.place_forget()
        labelVf.place_forget()
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
        labelVi.place_forget()
        entryVi.place_forget()
        labelVf.place_forget()
        entryVf.place_forget()
    elif choice == 'MVF-MVI':
        labelM.place(x=109, y=60)
        entryM.place(x=81, y=90)
        labelVi.place(x=270, y=60)
        entryVi.place(x=294, y=90)
        labelVf.place(x=490, y=60)
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
labelTitleM = ctk.CTkLabel(frameMenu, text='Menu',
                        font=('Times new roman', 20), text_color='white')
labelTitleM.place(relx=0.5, anchor='center', y=50)
btnSS = ctk.CTkButton(frameMenu, text="Screenshot", command=screenshot)
btnSS.place(relx=0.5, anchor='center', y=130)
# Modelo Matematico
labelTitleFT = ctk.CTkLabel(frameMenu, text='Del Trabajo', font=('Times new roman', 18),
                         text_color='white', fg_color='#2f3123')
labelTitleFEc = ctk.CTkLabel(frameMenu, text='De Energia Cinetica', font=('Times new roman', 18),
                          text_color='white', fg_color='#2f3123')
labelTitleVE = ctk.CTkLabel(frameMenu, text='Variacion de energia', font=('Times new roman', 18),
                         text_color='white', fg_color='#2f3123')
FT = ctk.CTkLabel(frameMenu, text='W = | F | x | D | x cos a°', font=('Times new roman', 18),
               text_color='white', fg_color='#2f3123')
FEc = ctk.CTkLabel(frameMenu, text='Ec = ½m V²', font=('Times new roman', 18),
                text_color='white', fg_color='#2f3123')
FWEc = ctk.CTkLabel(frameMenu, text='W = ∆Ec', font=('Times new roman', 18),
                 text_color='white', fg_color='#2f3123')
VEc = ctk.CTkLabel(frameMenu, text='∆Ec = Ecf - Eci', font=('Times new roman', 18),
                text_color='white', fg_color='#2f3123')
VEc_2 = ctk.CTkLabel(frameMenu, text='∆Ec = ½m Vf² - ½m Vi²', font=('Times new roman', 18),
                  text_color='white', fg_color='#2f3123')

labelTitleD = ctk.CTkLabel(frameMenu, text='Donde: \n•W = Trabajo\n•F = Fuerza\n•D = Distancia\n•a = angulo',
                        font=('Times new roman', 15), text_color='white', fg_color='#2f3123')
labelTitleD_1 = ctk.CTkLabel(frameMenu, text='Donde: \n•Ec = Energia Cinetica\n•m = Masa\n•V = Velocidad\n',
                          font=('Times new roman', 15), text_color='white', fg_color='#2f3123')
labelTitleD_2 = ctk.CTkLabel(frameMenu, text='Donde: \n•∆Ec = Variacion\nde energia cinetica\n•Ecf = Energia\nCinetica Final\n•Eci = Energia\nCinetica Inicial\n•m = Masa\n•Vf = Velociad final\n•Vi = Velocidad Inicial',
                          font=('Times new roman', 15), text_color='white', fg_color='#2f3123')
# -------------------------------------------------------------#
# Elementos Caja
# -------------------------------------------------------------#
posIniX = 271
posIniY = 250
labelFN = ctk.CTkLabel(canvasCaja, text='',
                    font=('Times new roman', 15),text_color='black')
labelDl = ctk.CTkLabel(canvasCaja,text='Desplazamiento: ',font=('Times new roman',15),text_color='black')
btnRun = ctk.CTkButton(frameMenu, text='Run', command=BtnRun)
btnRun.place(relx=0.5,y=180, anchor= 'center')
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 451, 400, fill='#ff6a36', outline='#ff6a36')
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
labelF = ctk.CTkLabel(framePmt, text='Fuerza (N)', font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelD = ctk.CTkLabel(framePmt, text='Desplazamiento (m)', font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelA = ctk.CTkLabel(framePmt, text='Angulo (°) ', font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelM = ctk.CTkLabel(framePmt, text='Masa (kg)', font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelV = ctk.CTkLabel(framePmt, text='Velocidad (m/s²)', font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelR = ctk.CTkLabel(framePmt, text="Resultado:", font=('Times new roman', 15),
                   text_color='black', fg_color='#f1cc7a')
labelVi = ctk.CTkLabel(framePmt, text='Velocidad Inicial (m/s²)', font=('Times new roman', 15),
                    text_color='black', fg_color='#f1cc7a')
labelVf = ctk.CTkLabel(framePmt, text='Velocidad Final (m/s²)', font=('Times new roman', 15),
                    text_color='black', fg_color='#f1cc7a')
# -------------------------------------------------------------#
# Elementos Menu Calculos
# -------------------------------------------------------------#
labelTitleTyEc = ctk.CTkLabel(frameMenuCalc, text='¿Que desea calcular?', font=('Times new roman', 20),
                           text_color='white', fg_color='#2f3123')
labelTitleTyEc.place(relx=0.5, anchor='center', y=50)

labelTitleC = ctk.CTkLabel(canvasCaja, text='TRABAJO Y ENERGIA', font=('Times new roman', 25),
                        text_color='black')
labelTitleC.place(relx=0.5, anchor='center', y=50)
selectVar = tk.StringVar()
rbtn1 = ctk.CTkRadioButton(
    frameMenuCalc, text='Calcular Trabajo : ', value='FDA', variable=selectVar, command=formulas)
rbtn2 = ctk.CTkRadioButton(
    frameMenuCalc, text='Calcular Energia Cinetica: ', value='MV', variable=selectVar, command=formulas)
rbtn3 = ctk.CTkRadioButton(
    frameMenuCalc, text='Variacion de energia: ', value='MVF-MVI', variable=selectVar, command=formulas)
rbtn1.place(x=30, y=100)
rbtn2.place(x=30, y=140)
rbtn3.place(x=30, y=180)
selectVar.trace('w', refreshPmt)
win.mainloop()
