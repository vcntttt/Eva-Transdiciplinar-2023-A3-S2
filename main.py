import tkinter as tk
import time
import ttkbootstrap as ttk
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
canvasMenu.create_rectangle(0, 0, 200, 800, fill='#2f3123')
canvasMenu.place(x=0, y=0)
canvasPmt = ttk.Canvas(win, width=640, height=300)
canvasPmt.create_rectangle(0, 0, 640, 300, fill='#f1cc7a', outline='#f1cc7a')
canvasPmt.place(x=201, y=501)
canvasCaja = ttk.Canvas(win, width=640, height=500)
canvasCaja.place(x=201, y=0)
# -----------------------------------------------------------#
# Lienzo del menu
# -----------------------------------------------------------#

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
    0, 400, 640, 500, fill='#124b5b', outline='#124b5b')


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
labelFN = ttk.Label(canvasCaja, text='Desplazamiento', font=('Helvetica', 20))
puntaPos = None
puntaNeg = None


def PintaLinea(movimiento):
    global puntaPos, puntaNeg
    if movimiento > 0:
        puntaPos = canvasCaja.create_polygon(
            411, 200, 391, 190, 391, 210, fill='black')
        canvasCaja.create_line(
            200, 200, 411, 200, fill='black', width=3)
        canvasCaja.create_window(320, 150, window=labelFN)
        if puntaNeg is not None:
            canvasCaja.delete(puntaNeg)
    elif movimiento < 0:
        canvasCaja.create_line(200, 200, 411, 200, fill='black', width=3)
        puntaNeg = canvasCaja.create_polygon(
            180, 200, 200, 190, 200, 210, fill='black')
        canvasCaja.create_window(320, 150, window=labelFN)
        if puntaPos is not None:
            canvasCaja.delete(puntaPos)
    else:
        return
    return


# Boton 'Run'
def BtnRun():
    movimiento = calc()
    posIni(movimiento)
    PintaLinea(movimiento)
    mueveCaja(movimiento)


def calc():
    resultado = 0
    f = float(entryF.get()+'0')
    d = float(entryD.get()+'0')
    a = float(entryA.get()+'0')
    m = float(entryM.get()+'0')
    v = float(entryV.get()+'0')
    if f and d and a:
        resultado = f * d * a
        labelR.configure(text=f"Resultado: {resultado}")
    elif m and v:
        resultado = (0.5 * m) * (v ** 2)
        labelR.configure(text=f"Resultado: {resultado}")
    print(f, d, a, m, v, resultado)
    return resultado


ButtonRun = ttk.Button(canvasCaja, text='Run', command=BtnRun)
canvasCaja.create_window(320, 450, window=ButtonRun, width=100, height=40)
# -----------------------------------------------------------#
# Lienzo Parametros
# -----------------------------------------------------------#

# Roce
checkRoce = tk.IntVar(value=0)


def getRoce():
    roce = checkRoce.get()
    if roce == 1:
        labelMC.place(x=20, y=50)
        materialCaja.place(x=20, y=80)
        labelMS.place(x=20, y=130)
        materialSuelo.place(x=20, y=160)
        labelRr.place(x=20, y=210)

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


askRoce = ttk.Checkbutton(canvasPmt, text='Roce?',
                          command=getRoce, variable=checkRoce,
                          bootstyle='round-toggle')
askRoce.place(x=50, y=20)
labelMC = ttk.Label(canvasPmt, text='Material Caja')
labelMS = ttk.Label(canvasPmt, text='Material Suelo')
labelR = ttk.Label(canvasPmt, text=f'El coeficiente de roce es {0}')
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
entryH = ttk.Entry(canvasPmt)
labelF = ttk.Label(canvasPmt, text='Fuerza (N)')
labelD = ttk.Label(canvasPmt, text='Desplazamiento (mt)')
labelA = ttk.Label(canvasPmt, text='Angulo')
labelM = ttk.Label(canvasPmt, text='Masa (Kg)')
labelV = ttk.Label(canvasPmt, text='Velocidad (mt/s**2)')
labelH = ttk.Label(canvasPmt, text='Altura (mt)')
labelR = ttk.Label(canvasPmt, text="Resultado:")
selectVar = tk.StringVar()
rbtn1 = ttk.Radiobutton(
    canvasPmt, text='Fuerza, Desplazamiento y Angulo', value='FDA', variable=selectVar)
rbtn2 = ttk.Radiobutton(
    canvasPmt, text='Masa y Velocidad', value='MV', variable=selectVar)
rbtn1.place(x=350, y=20)
rbtn2.place(x=350, y=50)


def refreshPmt(*args):
    choice = selectVar.get()
    if choice == 'FDA':
        labelF.place(x=350, y=70)
        entryF.place(x=350, y=100)
        labelD.place(x=350, y=150)
        entryD.place(x=350, y=180)
        labelA.place(x=350, y=230)
        entryA.place(x=350, y=260)
        labelR.place(x=520, y=215)
        entryM.place_forget()
        entryV.place_forget()
        labelM.place_forget()
        labelV.place_forget()
    elif choice == 'MV':
        labelM.place(x=350, y=70)
        entryM.place(x=350, y=100)
        labelV.place(x=350, y=150)
        entryV.place(x=350, y=180)
        labelR.place(x=520, y=215)
        labelF.place_forget()
        entryF.place_forget()
        labelD.place_forget()
        entryD.place_forget()
        labelA.place_forget()
        entryA.place_forget()


selectVar.trace('w', refreshPmt)

win.mainloop()
