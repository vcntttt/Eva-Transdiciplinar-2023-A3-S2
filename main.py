# Librerias importadas
import tkinter as tk
from tkinter import messagebox as msg
import customtkinter as ctk
import time
import math
from PIL import ImageGrab, ImageTk, Image
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


def screenshot(): #Funcion llamada por el Boton Screenshot
    global contador
    x = win.winfo_rootx()
    y = win.winfo_rooty()
    captura = ImageGrab.grab(bbox=(x, y, x+nRes[0], y+nRes[1]))
    captura.save(f'captura_{contador}.png')
    contador += 1
    return

#se crea una lista para almacenar las imagenes de las formulas en latex
formulas = []
#cargamos las imagenes de las formulas latex y las agregamos a la lista 
formulas.append(Image.open("formulas/Trabajo.png"))
formulas.append(Image.open("formulas/energiaCinetica.png"))
formulas.append(Image.open("formulas/VariacionEc.png"))
formulas.append(Image.open("formulas/TrabajoRoce.png"))
formulas.append(Image.open("formulas/TrabajoNeto.png"))
formulas.append(Image.open("formulas/SimbologiaW.png"))
formulas.append(Image.open("formulas/SimbologiaEc.png"))
formulas.append(Image.open("formulas/SimbologiaDelta.png"))
#utilizamos la expresion ImageTK.PhotoImage para que tome un elemento de la lista "Formulas" para
#transformar las imagenes de la lista en una PhotoImage para asi utilizar las fotos agregadas
imagenes = [ImageTk.PhotoImage(formula) for formula in formulas]
#creamos otra lista para agregar las fotos "label" que vamos a almacenar
label_imagen = []
#se itera sobre la lista imagen y crea un objeto label para cada imagen, luego lo agrega a la lista
for imagen in imagenes:
    label = tk.Label(win, image=imagen, borderwidth=0)
    label_imagen.append(label)
#esta variable se usa para controlar si se muestran las formulas o no
formulasVar = tk.IntVar()
simbologiaVar = tk.IntVar()

#verifica si al apretar el boton de mostrar formulas se muestren las formulas cuando presiones 
#los botones de lo que quieras calcular, las posiciona en cierta parte de la pantalla
#y tambien usa el place_forget para que al apretar otro boton se oculten las formulas
def formulas():
    form = formulasVar.get()
    simb = simbologiaVar.get()
    for i in label_imagen:
        i.place_forget()
    if form == 1 or simb == 1:
        switchSimb.place(x=30,y=340)
    else:
        switchSimb.place_forget()
    if form == 1:
        choice = selectVar.get()
        roce = checkRoce.get()
        if choice == 'FDA':
            label_imagen[0].place(x=0,y=300)
            if simb == 1:
                label_imagen[5].place(x=0,y=450) 
        if choice == 'MV':
            label_imagen[1].place(x=0,y=300)
            if simb == 1:
                label_imagen[6].place(x=0,y=450)
        if choice == 'VEc':
            label_imagen[2].place(x=0,y=300)
            if simb == 1:
                label_imagen[7].place(x=0,y=450)
        if choice == 'Manual':
            label_imagen[0].place(x=0,y=300)
            if simb == 1:
                label_imagen[5].place(x=0,y=450)  
        return 
# -------------------------------------------------------------#
# Funciones Caja
# -------------------------------------------------------------#
moving = False # Bandera utilizada para confirmacion de movimiento
def confirmClose(): # Confirma si quieres salir mientras se mueve la caja
    if moving:
        cierre = msg.askyesno('Salir', 'Movimiento ejecutandose, ¿Desea salir de todas formas?')
        if cierre:
            win.destroy()
        else:
            pass
    else:
        win.destroy()
def mueveCaja(resultado,direccion,velocidad): # Funcion que mueve la caja para el trabajo y la energia cinetica
    global moving
    try:
        if velocidad == 0 or direccion == 0 or resultado == 0:
            return
        moving = True
        choice = selectVar.get()
        desplazamiento = 1000
        disRecorrida = 0
        maxVelTime = 0.2
        minVelTime = 0.00002
        velTime = 1
        if choice == "FDA" or choice == 'MV':
            print(f'Velocidad: {velocidad}')
            rango = maxVelTime - minVelTime
            escala = velocidad / (velocidad + 10)
            velTime = maxVelTime - (rango * escala)
        # Ciclo que mueve la caja hasta llegar al final de la pantalla
        while disRecorrida < desplazamiento:
            coords = canvasCaja.coords(fig)
            esqDer = coords[2] + direccion
            esqIzq = coords[0] + direccion
            canvasCaja.move(fig, direccion, 0)
            disRecorrida += 1
            # Comprueba si se ha llegado al final, por cualquiera de los dos lados
            if esqDer > 720 or esqIzq < 0:
                    posIni()
                    break
            canvasCaja.update()
            # print(f'velTime: {velTime}')
            time.sleep(velTime)
        moving = False
    except KeyboardInterrupt: #Si se trata de cerrar la ventana durante un movimiento, te pide confirmacion de que quieres salir
        print('Programa interrumpido')
        confirmClose()
    return
win.protocol('WM_DELETE_WINDOW', confirmClose)
def mueveCajaVEc(direccion = 1, vi = 0, vf = 0): # Funcion que mueve la caja para la variacion de la energia cinetica
    global moving
    try:
        moving = True
        desplazamiento = 540
        disRecorrida = 0
        rango = 0.2 - 0.0002
        direccion = 1
        while disRecorrida < desplazamiento:
            escala = vf / (vi + (vf - vi)*((disRecorrida / 100)))
            velTime = (0.2 - (rango * escala)) /10
            velTime = abs(velTime)
            coords = canvasCaja.coords(fig)
            esqDer = coords[2] + direccion
            esqIzq = coords[0] + direccion
            canvasCaja.move(fig, direccion, 0)
            disRecorrida += 1
            if esqDer >= 720 or esqIzq < 0:
                posIni()
                break
            canvasCaja.update()
            # print(f'velTime en {disRecorrida}: {velTime}')
            time.sleep(velTime)
        moving = False
    except KeyboardInterrupt:
        print('Programa interrumpido')
        confirmClose()
    return
def BtnRun(): # Funcion que se ejecuta al presionar el boton run
    canvasCaja.delete('linea')
    choice = selectVar.get()
    roce = checkRoce.get()
    if choice == 'Manual':
        return
    posIni()
    values, parametros = calc()
    resultado = float(parametros[1])
    direccion = float(parametros[2])
    movimiento = float(parametros[3])
    velocidad = float(parametros[4])
    vi = vf = 0
    print(f'Movimiento: {movimiento} ; Velocidad: {velocidad} ; Direccion: {direccion} ; Roce: {roce} ; Resultado: {resultado} ; Choice: {choice}') 
    PintaLinea(movimiento, direccion)
    if choice == 'VEc':
        vi = float(values[6])
        vf = float(values[7])
        mueveCajaVEc(direccion, vi, vf)
    else:
        mueveCaja(resultado,direccion, velocidad)

def posIni(): # Funcion utilizada para resetear la posicion de la caja, entre otras cosas
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

def PintaLinea(movimiento, direccion): #Pinta la linea de movimiento segun la direccion y el movimiento
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
posX = None
def toggleMovManual(*args): # Activa/ Desactiva el movimiento manual
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

def pickBox(event): #Detecta el click en la caja
    global posX
    x1,y1,x2,y2 = canvasCaja.coords(fig)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        posX = event.x
    return

desp = 0
def moveOn(event):
    global posX, desp
    if posX is not None:
        x1, y1, x2, y2 = canvasCaja.coords(fig)
        despX = event.x - posX
        newX1 = x1 + despX
        newX2 = x2 + despX
        canvas_width = canvasCaja.winfo_width()
        if newX1 >= 0 and newX2 <= canvas_width:
            desp = newX1  # Calcular el desplazamiento actualizado
            labelDl.place(x=160, y=95)
            labelDl.configure(text=f'Desplazamiento: {int(desp)} metros')
            try:
                fuerza = float(entryF.get())
                if desp == 0:
                    trabajo = 0  # El desplazamiento es 0, trabajo es 0
                else:
                    trabajo = calcInv(desp, fuerza)  # Pasar también la fuerza como argumento
                print(f'Trabajo: {trabajo}')
                canvasCaja.move(fig, despX, 0)
                posX = event.x
                if desp > 260 and despX > 0:
                    return
            except ValueError:
                msg.showerror('Error', 'El valor de fuerza ingresado es inválido.')
                labelDl.configure(text='Desplazamiento: 0 metros')
                return
    return

def letItgo(event): #Detecta cuando soltamos el click en la caja
    global posX
    posX = None
    return

def calcInv(desplazamiento, fuerza):
    try:
        trabajo = fuerza * desplazamiento
        print(f'Trabajo: {trabajo}')
        return trabajo
    except ValueError:
        msg.showerror('Valores incompletos', 'Por favor ingresar todos los valores solicitados')
        return 0
# -------------------------------------------------------------#
# Funciones Parametros
# -------------------------------------------------------------#

def calc(): #Funcion de calculo general, aca pasa la magia
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
                wFr = u * m * g * d * math.cos(rad180)
                wNeto = w + wFr
            else:
                wNeto = eCf - eCi
            movimiento = wNeto
            velocidad = 0
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


def refreshPmt(*args): # Funcion encargada de poner los widgets en pantalla segun la opcion que hayamos escogido
    choice = selectVar.get()
    roce = checkRoce.get()
    form = formulasVar.get()
    posIni()
    formulas()
    canvasCaja.delete('linea')
    widgetsForget = [labelF,entryF,labelD,entryD,labelA,entryA,labelV,entryV,labelM,entryM,labelVf,entryVf,labelVi,entryVi,labelMC,materialCaja,labelMS,materialSuelo,labelRr,switchRoce,switchMM,switchSimb]
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
        switchRoce.place(x=30, y=260)
        switchMM.place(x=30, y=290)
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
        switchMM.place(x=30, y=290)
    if choice == 'VEc':
        labelVi.place(relx  = x[0], y = y[0])
        entryVi.place(relx  = x[0], y = y[1])
        labelVf.place(relx  = x[2], y = y[0])
        entryVf.place(relx  = x[2], y = y[1])
        labelM.place(relx = x[3], y = y[2])
        entryM.place(relx = x[3], y = y[3])
        switchRoce.place(x=30, y=260)
        switchMM.place(x=30, y=290)

    if choice == 'Manual':
        labelF.place(relx=0.4,y=70)
        entryF.place(relx=0.4, y = 100)
        switchMM.place(x=30, y=290)
    if form == 1:
        switchSimb.place(x=30,y=340)
    return 
# -------------------------------------------------------------#
# Funciones Parametros - Roce
# -------------------------------------------------------------#
def getCoefRoce(event): # Detecta los materiales escojidos en los comboboxes y llama a calcRoce
    global coeficiente
    caja = varCaja.get()
    suelo = varSuelo.get()
    coeficiente = 0
    if caja and suelo:
        coeficiente = calcRoce(caja, suelo)
    if coeficiente:
        labelRr.configure(text=f'El coeficiente de roce es {coeficiente}')
    return coeficiente

def calcRoce(caja, suelo): # "Calcula" el coeficiente de roce
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
                            text_color='white', font=("Perpetua",23))
labelTitleM.place(relx=0.5, anchor='center', y=50)
btnSS = ctk.CTkButton(frameMenu, text="Screenshot", command=screenshot)
btnRun = ctk.CTkButton(frameMenu, text='Run', command=BtnRun)
btnStop = ctk.CTkButton(frameMenu,text='Reseteo Manual', command=posIni)
btnSS.place(relx=0.5, anchor='center', y=130)
btnRun.place(relx=0.5, y=180, anchor='center')
btnStop.place(relx = 0.5,y = 230,anchor = 'center')
# Modelo Matematico
# -------------------------------------------------------------#
# Elementos Caja
# -------------------------------------------------------------#
posIniX = 271
posIniY = 250
labelTitleC = ctk.CTkLabel(canvasCaja, text='TRABAJO Y ENERGIA', 
                           text_color='black', font=("Algerian",20))
labelFN = ctk.CTkLabel(canvasCaja, text='',
                        text_color='black')
labelDl = ctk.CTkLabel(canvasCaja, text='Desplazamiento: ', font=(
    'Times new roman', 15), text_color='black')
fig = canvasCaja.create_rectangle(
    posIniX, posIniY, 451, 400, fill='#ff6a36')
suelo = canvasCaja.create_rectangle(0,400,720,500,fill='#A18072',outline='#A18072')
# -------------------------------------------------------------#
# Elementos Parametros
# -------------------------------------------------------------#
entryF = ctk.CTkEntry(framePmt)
entryD = ctk.CTkEntry(framePmt)
entryA = ctk.CTkEntry(framePmt, placeholder_text='0 - 180°')
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
labelAngle = ctk.CTkLabel(framePmt, text='Solo se pueden ingresas angulos entre 0 y 180', 
                          text_color='black', fg_color='#f1cc7a')
# -------------------------------------------------------------#
# Elementos Menu Calculos
# -------------------------------------------------------------#
labelTitleTyEc = ctk.CTkLabel(frameMenuCalc, text='¿Que desea calcular?', 
                              text_color='white', fg_color='#2f3123', font= ("Helvetica",14))

selectVar = tk.StringVar()
toggleManual = tk.IntVar()
checkRoce = tk.IntVar(value=0)
rbtn1 = ctk.CTkRadioButton(
    frameMenuCalc, text='Trabajo ', value='FDA', variable=selectVar)
rbtn2 = ctk.CTkRadioButton(
    frameMenuCalc, text='Energia Cinetica', value='MV', variable=selectVar)
rbtn3 = ctk.CTkRadioButton(
    frameMenuCalc, text='Trabajo segun \u0394Ec', value='VEc', variable=selectVar)
rbtn4 = ctk.CTkRadioButton(
    frameMenuCalc, text='Desplazamiento manual',variable=selectVar,value='Manual')
switchMM = ctk.CTkSwitch(
    frameMenuCalc, text="Modelo Matematico", variable=formulasVar, command=formulas)
switchSimb = ctk.CTkSwitch(
    frameMenuCalc, text="Simbologia",variable=simbologiaVar,command=formulas)
switchRoce = ctk.CTkSwitch(frameMenuCalc,text='Implementar Roce', variable=checkRoce, text_color= "Yellow", font=("Calisto MT",12))
labelTitleC.place(relx=0.5, anchor='center', y=50)
labelTitleTyEc.place(relx=0.5, anchor='center', y=50)
rbtn1.place(x=30, y=100)
rbtn2.place(x=30, y=140)
rbtn3.place(x=30, y=180)
rbtn4.place(x=30, y=220)
# Rastro de Variables
selectVar.trace('w', refreshPmt)
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
# -------------------------------------------------------------#
# Estilizado
# -------------------------------------------------------------#
def style():
    menuSideBtns = [btnSS, btnRun, btnStop]
    for btn in menuSideBtns:
        btn.configure(font=("Arial",14), fg_color=("White"), bg_color=("Gray"), text_color=("Black"), hover_color=("gray"), corner_radius=0)
    calcMenuBtns = [rbtn1, rbtn2, rbtn3, rbtn4]
    colorsBtn = ['Yellow', 'Light Green', 'dark Orange', 'Light Blue']
    for btn,color in zip(calcMenuBtns,colorsBtn):
        btn.configure(fg_color=color,text_color='Yellow',font=("Arial",14))
    entrys = [entryF, entryD, entryA, entryM, entryV, entryVf, entryVi]
    for entry in entrys:
        entry.configure(fg_color='white',border_color='gray',text_color='black')
    switchs= [switchSimb, switchRoce, switchMM]
    for switch in switchs:
        switch.configure(text_color='Yellow', font=("Arial",14), progress_color='Yellow')
# -------------------------------------------------------------#
# Validaciones
# -------------------------------------------------------------#
def checkEntrys(text): #Impide que el usuario ingrese letras en los entrys
    if text.isdigit() or text == '':
        return True
    else:
        return False
def checkAngle(text): # Limita el angulo ingresado a un numero entre 0 y 180
    roce = checkRoce.get()
    if text == '':
        return True 
    try:
        angulo = float(text)
        if 0 <= angulo <= 180:
            return True
        else:
            return False
    except ValueError:
        return False
def validate(widget, function): #Valida los entrys
    validation = widget.register(function)
    widget.configure(validate = 'key', validatecommand = (validation, '%P'))

def applyValidate(): #Aplica las validaciones
    entrys = [entryF, entryD, entryA, entryM, entryV, entryVf, entryVi]
    for entry in entrys:
        if entry == entryA:
            validate(entry, checkAngle)
        else:
            validate(entry, checkEntrys)    
applyValidate()
style()
win.mainloop()