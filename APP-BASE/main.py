import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import cv2
import imutils
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Canvas, Button, Frame, Label,Tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1280x736")
root.title("PSQ-APP")
root.resizable(width=False, height=False)

fondo = tk.PhotoImage(file="C:/Users/FixError/Desktop/ej1/dist/main/fondo.png")
fondo1 = tk.Label(root, image=fondo).place(x=0, y=0)


nombre1,apellido1,edad1,correo1,telefono1 = [],[],[],[],[]

def agregar_datos():
	global nombre1, apellido1, dni1, correo1, telefono1

	nombre1.append(ingresa_nombre.get())
	apellido1.append(ingresa_apellido.get())
	edad1.append(ingresa_edad.get())
	correo1.append(ingresa_correo.get())
	telefono1.append(ingresa_telefono.get())

	ingresa_nombre.delete(0,END)
	ingresa_apellido.delete(0,END)
	ingresa_edad.delete(0,END)
	ingresa_correo.delete(0,END)
	ingresa_telefono.delete(0,END)

	datos = {'DIA':nombre1,'T1':apellido1, 'T2':edad1, 'T3':correo1, 'T4':telefono1 }
	nom_excel  = str("datatime.xlsx")
	df = pd.DataFrame(datos,columns =  ['DIA', 'T1', 'T2', 'T3', 'T4'])
	df.to_excel(nom_excel)

def grafico1():
    global exl1, df, valores, gp, canvas, df1, ax1, bar1

    exl1 = "datatime.xlsx"
    df = pd.read_excel(exl1)

    valores = df[["DIA","T4"]]

    df1 = valores.plot.bar(x="DIA", y="T4", rot = 10)
    plt.show()


    figure1 = plt.Figure(figsize=(4.8, 2.1), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().place(x=780, y=510)
    df1 = valores[['DIA','T4']].groupby('DIA').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Ultimo tiempo por dia')

def grafico2():
    global exl1, df, valores, gp, canvas, df1, ax1, bar1

    exl1 = "datatime.xlsx"
    df = pd.read_excel(exl1)

    valores = df[["DIA","T1"]]

    df1 = valores.plot.bar(x="DIA", y="T1", rot = 10)
    plt.show()


    figure1 = plt.Figure(figsize=(4.8, 2.1), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().place(x=780, y=300)
    df1 = valores[['DIA','T1']].groupby('DIA').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title()


def grafico3():
    global exl1, df, valores, gp, canvas, df1, ax1, bar1, tiempos

    exl1 = "datatime.xlsx"
    df = pd.read_excel(exl1)

    tiempos = df[["T1", "T2", "T3", "T4"]]
    print(tiempos)

    df1 = tiempos.plot.bar(rot = 10)
    plt.show()

    figure1 = plt.Figure(figsize=(4.8, 2), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().place(x=780, y=100)
    tiempos.plot(kind='bar', legend=True, ax=ax1)

def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()


def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=580)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()


def finalizar():
    global cap
    cap.release()



def ventanacam():
    global root2

    root2 = tk.Toplevel()
    root2.geometry("1280x736")

    def iniciar():
        global cap
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        visualizar()

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    def visualizar():
        global cap
        if cap is not None:
            ret, frame = cap.read()
            if ret == True:
                frame = imutils.resize(frame, width=1800)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                lblVideo.configure(image=img)
                lblVideo.image = img
                lblVideo.after(10, visualizar)
            else:
                lblVideo.image = ""
                cap.release()

    def finalizar():
        global cap
        cap.release()




    lblVideo = Label(root2)
    lblVideo.pack()
    btnIniciar2 = Button(root2, text="Iniciar", width=10, command=iniciar)
    btnIniciar2.place(x=650, y=470)
    btnFinalizar2 = Button(root2, text="Finalizar", width=10, command=finalizar)
    btnFinalizar2.place(x=650, y=500)




cap = None
cap2 = None
btnIniciar1 = Button(root, text="Ampliar", width=10, command=ventanacam)
btnIniciar1.place(x=650, y=370)
btnIniciar = Button(root, text="Iniciar", width=10, command=iniciar)
btnIniciar.place(x=650, y=470)
btnFinalizar = Button(root, text="Finalizar", width=10, command=finalizar)
btnFinalizar.place(x=650, y=500)


lblVideo = Label(root)
lblVideo.place( x=30, y=95)


file_frame = tk.LabelFrame(root, text="Ingresar datos de tiempo", bg='MediumPurple4', fg='white')
file_frame.place(height=180, width=730, rely=0.73, relx=0.02)

nombre = Label(file_frame, text ='DIA',  bg='indigo', fg='white').place(rely=0.1, relx=0.01)
ingresa_nombre = Entry(file_frame,  width=13, font = ('Arial',8))
ingresa_nombre.place(rely=0.1, relx=0.09)

apellido = Label(file_frame, text ='T1', bg='indigo', fg='white').place(rely=0.25, relx=0.01)
ingresa_apellido = Entry(file_frame, width=13, font = ('Arial',8))
ingresa_apellido.place(rely=0.25, relx=0.09)

edad = Label(file_frame, text ='T2', bg='indigo', fg='white').place(rely=0.40, relx=0.01)
ingresa_edad = Entry(file_frame,  width=13, font = ('Arial',8))
ingresa_edad.place(rely=0.40, relx=0.09)

correo = Label(file_frame, text ='T3', bg='indigo', fg='white').place(rely=0.55, relx=0.01)
ingresa_correo = Entry(file_frame,  width=13, font = ('Arial',8))
ingresa_correo.place(rely=0.55, relx=0.09)

telefono = Label(file_frame, text ='T4', bg='indigo', fg='white').place(rely=0.70, relx=0.01)
ingresa_telefono = Entry(file_frame, width=13, font = ('Arial',8))
ingresa_telefono.place(rely=0.70, relx=0.09)

agregar = tk.Button(file_frame, width=10, text='Guardar',fg= 'white', bg='indigo',bd=5, command=agregar_datos)
agregar.place(rely=0.45, relx=0.50)

button3 = tk.Button(file_frame,  width=10, text="Grafico 1" ,bg='mediumpurple', fg='white', bd=5, command=lambda: grafico1())
button3.place(rely=0.25, relx=0.70)

button4 = tk.Button(file_frame,  width=10, text="Grafico 2" ,bg='mediumpurple', fg='white', bd=5, command=lambda: grafico2())
button4.place(rely=0.45, relx=0.70)

button5 = tk.Button(file_frame,  width=10, text="Grafico 3" ,bg='mediumpurple', fg='white', bd=5, command=lambda: grafico3())
button5.place(rely=0.65, relx=0.70)



root.mainloop()
