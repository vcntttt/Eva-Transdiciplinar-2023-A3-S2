import tkinter as tk 
from tkinter import ttk,Frame,Button
import tkinter as tk
from tkinter import messagebox as msg
import ttkbootstrap as ttk
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
canvasTyEc = ttk.Canvas(win, width= 240, height=800)
canvasTyEc.create_rectangle(0,0,240,800, fill='#2f3123', outline='#2f3123')
canvasTyEc.place(x=961, y=0)
canvasPmt = ttk.Canvas(win, width=719, height=300)
canvasPmt.create_rectangle(0, 0, 719, 300, fill='#f1cc7a', outline='#f1cc7a')
canvasPmt.place(x=241, y=501)
canvasCaja = ttk.Canvas(win, width=720, height=500)
canvasCaja.create_rectangle(0, 400, 719, 500, fill='#A18072', outline='#A18072')
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
# 
#-------------------------------------------------------------#
def printValues():
    choice = refreshPmt()
    values = calc()
    table.delete(*table.get_children())
    data = [
        ['Fuerza', f'{values[0]}'],
        ['Desplazamiento', f'{values[1]}'],
        ['Angulo (Grados)', f'{values[2]}'],
        ['Angulo (Radianes)', f'Aprox {values[3]}'],
        ['Masa', f'{values[4]}'],
        ['Velocidad', f'{values[5]}'],
        ['Masa inicial', f'{values[6]}'],
        ['Velocidad inicial', f'{values[7]}'],
        ['Masa final', f'{values[8]}'],
        ['Velocidad final', f'{values[9]}'],
        [f'{values[10]}', f'{values[11]}'],]
    if choice == 'FDA':
        table.insert('', 'end', values=data[0])
        table.insert('', 'end', values=data[1])
        table.insert('', 'end', values=data[2])
        table.insert('', 'end', values=data[3])
    elif choice == 'MV':
        table.insert('', 'end', values=data[4])
        table.insert('', 'end', values=data[5])
    elif choice == 'MVF-MVI':
        table.insert('', 'end', values=data[6])
        table.insert('', 'end', values=data[7])
        table.insert('', 'end', values=data[8])
        table.insert('', 'end', values=data[9])
    table.place(x=3, y=300)
    return
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
def formulas():
    labelTitleF = ttk.Label(canvasMenu, text= 'Modelo Matematico', font=('Times new roman',20),
                            foreground='white', background='#2f3123')
    labelTitleF.place(relx=0.5, anchor='center', y=330)
    FT = ttk.Label(canvasMenu, text= 'W = | F | x | D | x cos a°', font=('Times new roman',15),
                            foreground='white',background='#2f3123')
    FT.place(relx=0.5,anchor='center',y=380)
    FEc = ttk.Label(canvasMenu, text= 'Ec = ½ m x V² ', font=('Times new roman',15),
                            foreground='white',background='#2f3123')
    FEc.place(relx=0.5,anchor='center',y=410)
    FVEc = ttk.Label(canvasMenu, text= 'W = ∆Ec ', font=('Times new roman',13),
                            foreground='white',background='#2f3123')
    FVEc.place(relx=0.5,anchor='center',y=440)
    FVEc_2 = ttk.Label(canvasMenu, text= '∆Ec = ½ m x Vf² - ½ m x Vi²', font=('Times new roman',15),
                            foreground='white',background='#2f3123')
    FVEc_2.place(relx=0.5,anchor='center',y=470)
#-------------------------------------------------------------#
# 
#-------------------------------------------------------------#
def PintaLinea(movimiento):
    canvasCaja.delete('linea')
    if movimiento:
        canvasCaja.create_line(
            275, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(350, 150, window=labelFN)
    if movimiento > 0:
        canvasCaja.create_polygon(
            411, 200, 391, 190, 391, 210, fill='black', tags='linea')
    elif movimiento < 0:
        canvasCaja.create_polygon(
            180, 200, 200, 190, 200, 210, fill='black', tags='linea')
    else:
        return
    return
#-------------------------------------------------------------#
# Calculos
#-------------------------------------------------------------#
def calc():
    choice = refreshPmt()
    f = d = aG = aR = m = v = vi = vf =0
    rType = 'Resultado'
    rNum = 0
    if choice == 'FDA':
        try:
            f = float(entryF.get())
            d = float(entryD.get())
            aG = float(entryA.get())
            aR = math.radians(aG)
            trabajo = f * d * math.cos(aR)
            aR = '{:.4f}'.format(aR)
            rType = 'Trabajo'
            rNum = trabajo
            labelFN.configure(text=f"{rType}: {rNum}")
        except ValueError:
            msg.showerror(
                'Valores incompletos', 'Porfavor ingresar todos los valores solicitados')
    elif choice == 'MV':
        try:
            m = float(entryM.get())
            v = float(entryV.get())
            eC = (0.5 * m) * (v ** 2)
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
        labelFN.configure(text=f'{rType}: {resultadoF} Joules')
        rNum = resultadoF
    else:
        labelFN.configure(text=f'{rType}: {int(rNum)} Joules')
    valores = [f, d, aG, aR, m, v, vi, vf,rType, rNum]
    return valores
#-------------------------------------------------------------#
# Boton "Run"
#-------------------------------------------------------------#
ButtonRun = ttk.Button(canvasCaja, text='Run', command=BtnRun, style='primary')
canvasCaja.create_window(360, 450, window=ButtonRun, width=100, height=40)
# -----------------------------------------------------------#
# Roce
# -----------------------------------------------------------#
# Roce
checkRoce = tk.IntVar(value=0)
#-------------------------------------------------------------#
def getRoce():
    roce = checkRoce.get()
    if roce == 1:
        labelMC.place(x=143, y=140)
        materialCaja.place(x=143, y=170)
        labelMS.place(x=431, y=140)
        materialSuelo.place(x=431, y=170)
        labelRr.place(x=294, y=220)
    else:
        labelMC.place_forget()
        materialCaja.place_forget()
        labelMS.place_forget()
        materialSuelo.place_forget()
        labelRr.place_forget()
    return
#-------------------------------------------------------------#
def getCoefRoce(event):
    caja = materialCaja.get()
    suelo = materialSuelo.get()
    coeficiente = calcRoce(caja, suelo)
    if coeficiente:
        labelRr.configure(text=f'El coeficiente de roce es {coeficiente}')
#-------------------------------------------------------------#
def calcRoce(caja, suelo):
    if caja == 'Madera' and suelo == 'Madera':
        return 0.45
    elif caja == 'Madera' and suelo == 'Acero':
        return 0.5
    elif caja == 'Madera' and suelo == 'Cobre':
        return 0.45
    elif caja == 'Acero' and suelo == 'Madera':
        return 0.5
    elif caja == 'Acero' and suelo == 'Acero':
        return 0.55
    elif caja == 'Acero' and suelo == 'Cobre':
        return 0.4
    elif caja == 'Cobre' and suelo == 'Madera':
        return 0.45
    elif caja == 'Cobre' and suelo == 'Acero':
        return 0.4
    elif caja == 'Cobre' and suelo == 'Cobre':
        return 0.4
#-------------------------------------------------------------#
askRoce = ttk.Checkbutton(canvasTyEc, text='Roce?',
                          command=getRoce, variable=checkRoce,
                          bootstyle='round-toggle')
askRoce.place(x=30, y=220)
labelMC = ttk.Label(canvasPmt, text='Material Caja',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelMS = ttk.Label(canvasPmt, text='Material Suelo',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
materiales = ['Madera', 'Acero', 'Cobre']
materialCaja = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
materialSuelo = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
materialCaja.bind('<<ComboboxSelected>>', getCoefRoce)
materialSuelo.bind('<<ComboboxSelected>>', getCoefRoce)
labelRr = ttk.Label(canvasPmt, text=f'El coeficiente de roce es {0}')
#-------------------------------------------------------------#
# Calculos
#-------------------------------------------------------------#
# Resto de Parametros
labelModo = ttk.Label(canvasPmt, text='Escoja un modo: ',
                      background='lightblue')
entryF = ttk.Entry(canvasPmt)
entryD = ttk.Entry(canvasPmt)
entryA = ttk.Entry(canvasPmt)
entryM = ttk.Entry(canvasPmt)
entryV = ttk.Entry(canvasPmt)
entryVi = ttk.Entry(canvasPmt)
entryVf = ttk.Entry(canvasPmt)
labelF = ttk.Label(canvasPmt, text='Fuerza (N)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelD = ttk.Label(canvasPmt, text='Desplazamiento (d)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelA = ttk.Label(canvasPmt, text='Angulo (°) ',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelM = ttk.Label(canvasPmt, text='Masa (kg)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelV = ttk.Label(canvasPmt, text='Velocidad (m/s²)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
labelR = ttk.Label(canvasPmt, text="Resultado:",font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
LabelVi = ttk.Label(canvasPmt, text='Velocidad Inicial (m/s²)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
LabelVf = ttk.Label(canvasPmt, text='Velocidad Final (m/s²)',font=('Times new roman', 15),
                           foreground='black', background='#f1cc7a')
selectVar = tk.StringVar()
rbtn1 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Trabajo : ', value='FDA', variable=selectVar)
rbtn2 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Energia Cinetica: ', value='MV', variable=selectVar)
rbtn3 = ttk.Radiobutton(
    canvasTyEc, text='Variacion de energia: ', value='MVF-MVI', variable=selectVar)
rbtn1.place(x=30, y=100)
rbtn2.place(x=30, y=140)
rbtn3.place(x=30, y=180)
#-------------------------------------------------------------#
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
#-------------------------------------------------------------#
selectVar.trace('w', refreshPmt)
# -----------------------------------------------------------#
# Lienzo del menu
# -----------------------------------------------------------#
table = ttk.Treeview(canvasTyEc, columns=(
    'Unidad', 'Magnitud'), show='headings', style='primary')
table.heading('Unidad', text='Unidad')
table.heading('Magnitud', text='Magnitud')
table.column('Unidad', width=110)
table.column('Magnitud', width=80)
#-------------------------------------------------------------#
labelTitleTyEc = ttk.Label(canvasTyEc, text='Que desea calcular?', font=('Times new roman', 20),
                           foreground='white', background='#2f3123')
labelTitleTyEc.place(relx=0.5, anchor='center', y=50)

labelTitleC = ttk.Label(canvasCaja, text='TRABAJO Y ENERGIA', font=('Times new roman', 40),
                           foreground='black')
labelTitleC.place(relx=0.5, anchor='center', y=50)

labelTitleC = ttk.Label(canvasPmt, text='Calculos Tutu Tutu', font=('Times new roman', 20),
                           foreground='black',background='#f1cc7a')
labelTitleC.place(relx=0.5, anchor='center', y=30)

labelTitleM = ttk.Label(canvasMenu, text='Menu',
                        font=('Times new roman', 20), foreground='white', background='#2f3123')
labelTitleM.place(relx=0.5, anchor='center', y=50)

btnSS = ttk.Button(canvasMenu, text="Screenshot", command=screenshot)
btnSS.place(relx=0.5, anchor='center', y=130)

btnPrint = ttk.Button(canvasMenu, text="Imprimir valores guardados",
                      command=printValues)
btnPrint.place(relx=0.5, anchor='center', y=200)

btnF = ttk.Button(canvasMenu, text='Modelo Matematico',command=formulas)
btnF.place(relx=0.5, anchor='center', y=270)
#-------------------------------------------------------------#

win.mainloop()
