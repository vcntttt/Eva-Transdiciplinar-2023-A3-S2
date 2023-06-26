import tkinter as tk
from tkinter import messagebox as msg
import ttkbootstrap as ttk
import time
import math
from PIL import ImageGrab,Image, ImageTk
nRes = [1200, 800]
# Dimensiones (ojo, no son coordenadas, es lo que miden los espacios)
# Menu --> 240x800
# Caja Objeto --> 720x500
# Caja Parametros --> 720x300
# Caja de caclulos --> 240x800
# ----------------------------------------------------------#
# Tkinter base
# -----------------------------------------------------------#
win = ttk.Window(themename='flatly')
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
# -----------------------------------------------------------#
# Init Canvas
# -----------------------------------------------------------#
canvasMenu = ttk.Canvas(win, width=240, height=800)
canvasMenu.create_rectangle(0, 0, 240, 800, fill='#2f3123', outline='#2f3123')
canvasMenu.place(x=0, y=0)
canvasTyEc = ttk.Canvas(win, width=240, height=800)
canvasTyEc.create_rectangle(0, 0, 240, 800, fill='#2f3123', outline='#2f3123')
canvasTyEc.place(x=961, y=0)
canvasPmt = ttk.Canvas(win, width=719, height=300)
canvasPmt.create_rectangle(0, 0, 719, 300, fill='#f1cc7a', outline='#f1cc7a')
canvasPmt.place(x=241, y=501)
canvasCaja = ttk.Canvas(win, width=720, height=500)
canvasCaja.create_rectangle(
    0, 400, 719, 500, fill='#A18072', outline='#A18072')
canvasCaja.place(x=241, y=0)
# Caja
posIniX = 271
posIniY = 250
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 451, 400, fill='#ff6a36', outline='#ff6a36')

#-------------------------------------------------------------#
# Boton Run
#-------------------------------------------------------------#
def BtnRun():
    calculo = float(calc()[9])
    posIni()
    PintaLinea(calculo)
    mueveCaja(calculo)
#-------------------------------------------------------------#
# Movimiento Caja
#-------------------------------------------------------------#
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
        esqDer = coords[2] + direccion
        esqIzq = coords[0] + direccion
        canvasCaja.move(fig, direccion, 0)
        disRecorrida += 1
        if esqDer > 640 or esqIzq < 0:
            posIni()
            break
        canvasCaja.update()
        time.sleep(0.01)
    return

# Linea Referencia Movimiento
labelFN = ttk.Label(canvasCaja, text='Desplazamiento', font=('Times new roman', 20))
#-------------------------------------------------------------#
# 
#-------------------------------------------------------------#
def posIni():
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(coords[0]-posIniX)
        canvasCaja.move(fig, despX, 0)

#-------------------------------------------------------------#
# Boton de "screeshot"
#-------------------------------------------------------------#
contador = 1
def screenshot():
    global contador
    x = win.winfo_rootx()
    y = win.winfo_rooty()
    captura = ImageGrab.grab(bbox=(x, y, x+nRes[0], y+nRes[1]))
    captura.save(f'captura_{contador}.png')
    contador += 1
    return
#-------------------------------------------------------------#
# Modelo Matematico
#-------------------------------------------------------------#

formulas = []
formulas.append(Image.open("latex_formula.png"))
formulas.append(Image.open("latex_formula_1.png"))
formulas.append(Image.open("latex_formula_2.png"))

imagen = ImageTk.PhotoImage(formulas[0])
imagen2 = ImageTk.PhotoImage(formulas[1])
imagen3 = ImageTk.PhotoImage(formulas[2])

Label_imagen = tk.Label(win, image=imagen, borderwidth=0)
Label_imagen_2 = tk.Label(win, image=imagen2, borderwidth=0)
Label_imagen_3 = tk.Label(win, image=imagen3, borderwidth=0)

def formulas():
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
labelTitleD= ttk.Label(canvasMenu, text= 'Donde: \n•W = Trabajo\n•F = Fuerza\n•D = Distancia\n•a = angulo',
                    font=('Times new roman',18),foreground='white', background='#2f3123')
labelTitleD_1 = ttk.Label(canvasMenu, text= 'Donde: \n•Ec = Energia Cinetica\n•m = Masa\n•V = Velocidad\n',
                    font=('Times new roman',18),foreground='white', background='#2f3123')
labelTitleD_2 = ttk.Label(canvasMenu, text= 'Donde: \n•∆Ec = Variacion\nde energia cinetica\n•Ecf = Energia\nCinetica Final\n•Eci = Energia\nCinetica Inicial\n•m = Masa\n•Vf = Velociad final\n•Vi = Velocidad Inicial',
                    font=('Times new roman',18),foreground='white', background='#2f3123')
#-------------------------------------------------------------#
def formulas():
    labelTitleMM = ttk.Label(canvasMenu, text= 'Modelo Matematico', font=('Times new roman',20),
                    foreground='white', background='#2f3123')
    labelTitleMM.place(relx=0.5, anchor='center', y=280)
    choice = selectVar.get()
    if choice == 'FDA':
        labelTitleFT.place(relx=0.5, anchor='center', y=320)
        FT.place(relx=0.5,anchor='center',y=380)
        labelTitleD.place(x=10,y=420)
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
        FEc.place(relx=0.5,anchor='center',y=380)
        labelTitleD_1.place(x=10,y=420)
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
        FWEc.place(relx=0.5,anchor='center',y=380)
        VEc.place(relx=0.5,anchor='center',y=420)
        VEc_2.place(relx=0.5,anchor='center',y=460)
        labelTitleD_2.place(x=10,y=510)
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


def mueveCaja(direccion):
    desplazamiento = 1000
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
    mueveCaja(direccion)


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

btnPrint = ttk.Button(canvasMenu, text="Imprimir valores guardados",
                      command=printValues)
btnPrint.place(relx=0.5, anchor='center', y=200)

#btnF = ttk.Button(canvasMenu, text='Modelo Matematico',command=formulas)
#btnF.place(relx=0.5, anchor='center', y=270)
#-------------------------------------------------------------#

win.mainloop()
