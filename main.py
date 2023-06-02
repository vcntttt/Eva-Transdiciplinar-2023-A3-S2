import tkinter as tk
from tkinter import ttk
nRes = [1200, 800]
# Dimensiones (ojo, no son coordenadas, es lo que miden los espacios)
# Menu --> 200x800
# Caja Objeto --> 640x500
# Caja Parametros --> 640x300
# Ambos graficos son de 400x400
# -----------------------------------------------------------#
# Tkinter base
# -----------------------------------------------------------#
win = tk.Tk()
win.title('Proyecto Transdiciplinario: Trabajo y Energia')
win.geometry(f'{nRes[0]}x{nRes[1]}')
win.resizable(False, False)
# -----------------------------------------------------------#
# Lienzo del menu
# -----------------------------------------------------------#
canvasMenu = tk.Canvas(win, width=200, height=800)
canvasMenu.place(x=0, y=0)
canvasMenu.create_rectangle(
    0, 0, 200, 800, fill='lightgray', outline=canvasMenu['background'])
# -----------------------------------------------------------#
# Lienzo base
# -----------------------------------------------------------#
canvasCaja = tk.Canvas(win, width=640, height=500)
canvasCaja.place(x=201, y=0)
canvasCaja.create_rectangle(
    0, 0, 640, 500, fill='white', outline=canvasMenu['background'])
fig = canvasCaja.create_rectangle(
    231, 250, 411, 400, fill='red', outline=canvasMenu['background'])
canvasCaja.create_rectangle(
    0, 400, 640, 500,fill='#A18072', outline=canvasMenu['background'])
# Movimiento Caja
def mueveCaja(movimiento):
    canvasCaja.move(fig,movimiento,0)
    return
# Boton 'Run'
ButtonRun = ttk.Button(canvasCaja, text='Run', command=lambda:mueveCaja(movimiento=10))
canvasCaja.create_window(320,450,window=ButtonRun,width=100, height=40)
# -----------------------------------------------------------#
# Lienzo Parametros
# -----------------------------------------------------------#
canvasPmt = tk.Canvas(win, width=640, height=300)
canvasPmt.place(x=201, y=501)
canvasPmt.create_rectangle(
    0, 0, 640, 300, fill='lightblue', outline=canvasMenu['background'])
win.mainloop()
