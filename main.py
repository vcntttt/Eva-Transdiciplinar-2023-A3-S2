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
# Menu --> 200x800
# Caja Objeto --> 640x500
# Caja Parametros --> 640x300
# Ambos graficos son de 400x400
# -----------------------------------------------------------#
# Tkinter base
# -----------------------------------------------------------#
win = ttk.Window(themename='flatly')
win.iconbitmap('icon.ico')
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
# -----------------------------------------------------------#
# Init Canvas
# -----------------------------------------------------------#
canvasMenu = ttk.Canvas(win, width=200, height=800)
canvasMenu.create_rectangle(0, 0, 200, 800, fill='#2f3123', outline='#2f3123')
canvasMenu.place(x=0, y=0)
canvasTyEc = ttk.Canvas(win, width= 357, height=800)
canvasTyEc.create_rectangle(0,0,357,800, fill='#2f3123', outline='#2f3123')
canvasTyEc.place(x=843, y=0)
canvasPmt = ttk.Canvas(win, width=640, height=300)
canvasPmt.create_rectangle(0, 0, 640, 300, fill='#f1cc7a', outline='#f1cc7a')
canvasPmt.place(x=201, y=501)
canvasCaja = ttk.Canvas(win, width=640, height=500)
canvasCaja.place(x=201, y=0)
# -----------------------------------------------------------#
# Lienzo Caja
# -----------------------------------------------------------#
# Caja
posIniX = 231
posIniY = 250
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 411, 400, fill='#ff6a36', outline='#ff6a36')
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

def posIni():
    coords = canvasCaja.coords(fig)
    if coords[0] != posIniX:
        if coords[0] > posIniX:
            despX = -(abs(coords[0]-posIniX))
        else:
            despX = abs(coords[0]-posIniX)
        canvasCaja.move(fig, despX, 0)

# Linea Referencia Movimiento
labelFN = ttk.Label(canvasCaja, text='Desplazamiento', font=('Helvetica', 20))

def PintaLinea(movimiento):
    canvasCaja.delete('linea')
    if movimiento:
        canvasCaja.create_line(
            200, 200, 411, 200, fill='black', width=3, tags='linea')
        canvasCaja.create_window(320, 150, window=labelFN)
    if movimiento > 0:
        canvasCaja.create_polygon(
            411, 200, 391, 190, 391, 210, fill='black', tags='linea')
    elif movimiento < 0:
        canvasCaja.create_polygon(
            180, 200, 200, 190, 200, 210, fill='black', tags='linea')
    else:
        return
    return


# Boton 'Run'
def BtnRun():
    calculo = float(calc()[7])
    posIni()
    PintaLinea(calculo)
    mueveCaja(calculo)


def calc():
    choice = refreshPmt()
    f = d = aG = aR = m = v = 0
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
    if int(rNum) != rNum:
        resultadoF = '{:.2f}'.format(rNum)
        labelFN.configure(text=f'{rType}: {resultadoF} Joules')
        rNum = resultadoF
    else:
        labelFN.configure(text=f'{rType}: {int(rNum)} Joules')
    valores = [f, d, aG, aR, m, v, rType, rNum]
    return valores


ButtonRun = ttk.Button(canvasCaja, text='Run', command=BtnRun, style='primary')
canvasCaja.create_window(320, 450, window=ButtonRun, width=100, height=40)
# -----------------------------------------------------------#
# Lienzo Parametros
# -----------------------------------------------------------#

# Roce
checkRoce = tk.IntVar(value=0)


def getRoce():
    roce = checkRoce.get()
    if roce == 1:
        labelMC.place(x=20, y=40)
        materialCaja.place(x=20, y=70)
        labelMS.place(x=20, y=120)
        materialSuelo.place(x=20, y=150)
        labelRr.place(x=20, y=200)

    else:
        labelMC.place_forget()
        materialCaja.place_forget()
        labelMS.place_forget()
        materialSuelo.place_forget()
        labelRr.place_forget()
    return


def getCoefRoce(event):
    caja = materialCaja.get()
    suelo = materialSuelo.get()
    coeficiente = calcRoce(caja, suelo)
    if coeficiente:
        labelRr.configure(text=f'El coeficiente de roce es {coeficiente}')


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


askRoce = ttk.Checkbutton(canvasTyEc, text='Roce?',
                          command=getRoce, variable=checkRoce,
                          bootstyle='round-toggle')
askRoce.place(x=30, y=100)
labelMC = ttk.Label(canvasPmt, text='Material Caja')
labelMS = ttk.Label(canvasPmt, text='Material Suelo')
materiales = ['Madera', 'Acero', 'Cobre']
materialCaja = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
materialSuelo = ttk.Combobox(canvasPmt, values=materiales, state='readonly')
materialCaja.bind('<<ComboboxSelected>>', getCoefRoce)
materialSuelo.bind('<<ComboboxSelected>>', getCoefRoce)
labelRr = ttk.Label(canvasPmt, text=f'El coeficiente de roce es {0}')

# Resto de Parametros
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
labelR = ttk.Label(canvasPmt, text="Resultado:")
selectVar = tk.StringVar()
rbtn1 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Trabajo : ', value='FDA', variable=selectVar)
rbtn2 = ttk.Radiobutton(
    canvasTyEc, text='Calcular Energia Cinetica: ', value='MV', variable=selectVar)
rbtn1.place(x=30, y=20)
rbtn2.place(x=30, y=60)


def refreshPmt(*args):
    choice = selectVar.get()
    if choice == 'FDA':
        labelF.place(x=440, y=40)
        entryF.place(x=440, y=70)
        labelD.place(x=440, y=120)
        entryD.place(x=440, y=150)
        labelA.place(x=440, y=200)
        entryA.place(x=440, y=230)
        entryM.place_forget()
        entryV.place_forget()
        labelM.place_forget()
        labelV.place_forget()
    elif choice == 'MV':
        labelM.place(x=230, y=40)
        entryM.place(x=230, y=70)
        labelV.place(x=230, y=120)
        entryV.place(x=230, y=150)
        labelF.place_forget()
        entryF.place_forget()
        labelD.place_forget()
        entryD.place_forget()
        labelA.place_forget()
        entryA.place_forget()
    return choice


selectVar.trace('w', refreshPmt)
# -----------------------------------------------------------#
# Lienzo del menu
# -----------------------------------------------------------#


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
        [f'{values[6]}', f'{values[7]}'],]
    if choice == 'FDA':
        table.insert('', 'end', values=data[0])
        table.insert('', 'end', values=data[1])
        table.insert('', 'end', values=data[2])
        table.insert('', 'end', values=data[3])
        table.insert('', 'end', values=data[6])
    elif choice == 'MV':
        table.insert('', 'end', values=data[4])
        table.insert('', 'end', values=data[5])
        table.insert('', 'end', values=data[6])
    table.place(x=5, y=300)
    return


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
    canvasF = ttk.Canvas(win, width=180,height=490)
    canvasF.create_rectangle(0,0,180,490,fill='#e9fcff', outline='#00221e')
    canvasF.place(x=10,y=300)

    labelTitleF = ttk.Label(canvasF, text= 'Formulas', font=('Times new roman',20),
                            foreground='Black')
    labelTitleF.place(relx=0.5, anchor='center', y=22)



table = ttk.Treeview(canvasMenu, columns=(
    'Unidad', 'Magnitud'), show='headings', style='primary')
table.heading('Unidad', text='Unidad')
table.heading('Magnitud', text='Magnitud')
table.column('Unidad', width=110)
table.column('Magnitud', width=80)

labelTitleM = ttk.Label(canvasMenu, text='Menu',
                        font=('Times new roman', 20), foreground='white', background='#2f3123')
labelTitleM.place(relx=0.5, anchor='center', y=50)
btnSS = ttk.Button(canvasMenu, text="Screenshot", command=screenshot)
btnSS.place(relx=0.5, anchor='center', y=130)
btnPrint = ttk.Button(canvasMenu, text="Imprimir valores guardados",
                      command=printValues)
btnPrint.place(relx=0.5, anchor='center', y=200)
btnF = ttk.Button(canvasMenu, text='Formulas',command=formulas)
btnF.place(relx=0.5, anchor='center', y=270)

win.mainloop()
