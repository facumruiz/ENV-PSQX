import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import cv2
import imutils
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Canvas, Button, Frame, Label,Tk
from PIL import ImageTk, Image
import runpy
import pyrebase
import pyautogui

from win32api import GetSystemMetrics

firebaseConfig = {
  "apiKey": "AIzaSyCCxVHVH3Y4tH9Xxj3ul41Oumgw0fLH1e0",
  "authDomain": "psqapp-98466.firebaseapp.com",
  "databaseURL": "psqapp-98466",
  "storageBucket": "psqapp-98466.appspot.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()

try:

  email = input("Email: ")
  contra = input("contraseña: ")

  auth.sign_in_with_email_and_password(email,contra)

  root = tk.Tk()
  root.title("HOW APP")
  root.geometry("1280x736")
  root.configure(background="black")
  root.resizable(0, 0)

  nombre1, apellido1, edad1, correo1, telefono1, repe = [], [], [], [], [], []


  class Example(Frame):
      x=920
      y=545

      def __init__(self, master, *pargs):
          Frame.__init__(self, master, *pargs)

          fondo22 = tk.PhotoImage(file="howlogo.png")
          cap = None
          cap2 = None

          def agregar_datos():
              global nombre1, apellido1, dni1, correo1, telefono1, repe

              nombre1.append(ingresa_nombre.get())
              apellido1.append(ingresa_apellido.get())
              edad1.append(ingresa_edad.get())
              correo1.append(ingresa_correo.get())
              telefono1.append(ingresa_telefono.get())
              repe.append(ingresa_repe.get())

              ingresa_nombre.delete(0, END)
              ingresa_apellido.delete(0, END)
              ingresa_edad.delete(0, END)
              ingresa_correo.delete(0, END)
              ingresa_telefono.delete(0, END)
              ingresa_repe.delete(0, END)

              datos = {'DIA': nombre1, 'T1': apellido1, 'T2': edad1, 'T3': correo1, 'T4': telefono1,
                       'Repeticiones': repe}
              nom_excel = str("datatime.xlsx")
              df = pd.DataFrame(datos, columns=['DIA', 'T1', 'T2', 'T3', 'T4', 'Repeticiones'])
              df.to_excel(nom_excel, index=False)

          def grafico1():
              global exl1, df, valores, gp, canvas, df1, ax1, bar1

              exl1 = "datatime.xlsx"
              df = pd.read_excel(exl1)

              valores = df[["DIA", "T4", "Repeticiones"]]
              #df1 = valores.plot.bar(x="DIA", y="T4", rot=10)
              #plt.show()
              repeti = df[["Repeticiones"]]
              print(repeti)

              figure1 = plt.Figure(figsize=(4, 3.5), dpi=70, )
              ax1 = figure1.add_subplot(111)
              bar1 = FigureCanvasTkAgg(figure1, root)
              bar1.get_tk_widget().place(x=20, y=60)
              df1 = valores[['DIA', 'Repeticiones']].groupby('DIA').sum()
              df1.plot(kind='bar', color='blue', legend=False, ax=ax1)


              ax1.grid(color='grey', linestyle='-.')
              figure1.set_facecolor("indigo")
              ax1.xaxis.label.set_color('white')
              ax1.spines['bottom'].set_color('white')
              ax1.spines['top'].set_color('white')
              ax1.xaxis.label.set_color('white')
              ax1.tick_params(axis='x', colors='white')
              ax1.tick_params(axis='y', colors='white')
              ax1.patch.set_facecolor("white")
              ax1.set_title('Repeticiones por dia', color="white")

          def grafico2():
              global exl1, df, valores, gp, canvas, df1, ax1, bar1

              exl1 = "datatime.xlsx"
              df = pd.read_excel(exl1)
              df1 = df.min(axis=1)
              print(df1)
              df['mejor_tiempo'] = df.min(axis=1)
              print(df)

              valores = df[["DIA", "mejor_tiempo"]]
              mt = df[["mejor_tiempo"]]
              print(mt)
              #df1 = valores.plot.bar(x="DIA", y="mejor_tiempo", rot=10)

              #plt.show()

              figure1 = plt.Figure(figsize=(4, 3.5), dpi=70)
              ax1 = figure1.add_subplot(111)
              bar1 = FigureCanvasTkAgg(figure1, root)
              bar1.get_tk_widget().place(x=980, y=300)
              df1 = valores[['DIA', 'mejor_tiempo']].groupby('DIA').sum()
              df1.plot(kind='bar', color='purple', legend=False, ax=ax1)


              ax1.grid(color='grey', linestyle='-.')
              figure1.set_facecolor("indigo")
              ax1.xaxis.label.set_color('white')
              ax1.spines['bottom'].set_color('white')
              ax1.spines['top'].set_color('white')
              ax1.xaxis.label.set_color('white')
              ax1.tick_params(axis='x', colors='white')
              ax1.tick_params(axis='y', colors='white')
              ax1.patch.set_facecolor('white')
              ax1.set_title('Mejor tiempo por dia', color="white")

          def grafico3():
              global exl1, df, valores, gp, canvas, df1, ax1, bar1, tiempos

              exl1 = "datatime.xlsx"
              df = pd.read_excel(exl1)
              df['mejor_tiempo'] = df.max(axis=1)
              print(df)

              repeti = df[["Repeticiones"]]
              print(repeti)

              tiempos = df[["T1", "T2", "T3", "T4"]]
              print(tiempos)

              #df1 = tiempos.plot.bar(rot=10)

              #plt.show()

              figure1 = plt.Figure(figsize=(4, 3.5), dpi=70, edgecolor='white')
              ax1 = figure1.add_subplot(111)
              bar1 = FigureCanvasTkAgg(figure1, root)
              bar1.get_tk_widget().place(x=980, y=63)
              tiempos.plot(kind='bar', legend=True, ax=ax1)

              figure1.set_facecolor("white")
              ax1.grid(color='grey', linestyle='-.')
              figure1.set_facecolor("indigo")
              ax1.xaxis.label.set_color('white')
              ax1.tick_params(axis='x', colors='white')
              ax1.tick_params(axis='y', colors='white')
              ax1.patch.set_facecolor("white")
              ax1.set_title('Tiempos por dia', color="white")
              ax1.xaxis.label.set_color('white')
              ax1.spines['bottom'].set_color('white')
              ax1.spines['top'].set_color('white')

          def todosgraficos():
              global exl1, df, valores, gp, canvas, df1, ax1, bar1, todo, dia, mt

              exl1 = "datatime.xlsx"
              df = pd.read_excel(exl1)
              df['mejor_tiempo'] = df.min(axis=1)


              repeti = df[["Repeticiones"]]
              print(repeti)

              todo = df[["DIA","T1", "T2", "T3", "T4", "Repeticiones", "mejor_tiempo"]]
              print(todo)

              dia = df[["DIA"]]
              print(dia)

              mt = df[["mejor_tiempo"]]
              print(mt)

              repe = df[["Repeticiones"]]
              print(repe)

              todo = df[["T1", "T2", "T3", "T4"]]
              print(todo)

              fig, ax = plt.subplots(3)
              fig.set_facecolor("indigo")
              ax[0].plot(dia,mt, 'tab:green')
              ax[0].set_title('Mejor Tiempo por dia', color="white")
              ax[0].grid()
              ax[0].tick_params(axis='x', colors='white')
              ax[0].tick_params(axis='y', colors='white')

              ax[1].plot(dia,repe)
              ax[1].set_title('Repeticiones por dia', color="white")
              ax[1].grid()
              ax[1].tick_params(axis='x', colors='white')
              ax[1].tick_params(axis='y', colors='white')

              ax[2].plot(todo)
              ax[2].set_title('Todos los tiempos', color="white")
              ax[2].grid()
              ax[2].tick_params(axis='x', colors='white')
              ax[2].tick_params(axis='y', colors='white')




              plt.show()




          def iniciar():
              global cap
              cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
              visualizar()

          def visualizar():
              global cap
              if cap is not None:
                  ret, frame = cap.read()
                  if ret == True:
                      frame = imutils.resize(frame, width=730)
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
                          frame = imutils.resize(frame, width=1500)
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
              root2.configure(bg='white')

              lblVideo.pack()
              btnIniciar2 = Button(root2, text="Iniciar", fg='white', bg='indigo', width=20, command=iniciar)
              btnIniciar2.place(x=28, y=470)
              btnFinalizar2 = Button(root2, text="Finalizar", fg='white', bg='indigo', width=20, command=finalizar)
              btnFinalizar2.place(x=28, y=500)
              fondo2 = tk.Label(root2, image=fondo22).place(x=0, y=0)

          cap = None
          cap2 = None

          lblVideo = Label(root)
          lblVideo.place(x=300, y=70)
          file_frame = tk.LabelFrame(bg='MediumPurple4')
          file_frame.place(height=180, width=1230, rely=0.72, relx=0.02)
          file_frame1 = tk.LabelFrame(bg='MediumPurple4')
          file_frame1.place(height=210, width=275, rely=0.43, relx=0.02)
          position = tk.LabelFrame(file_frame, bg='MediumPurple4', fg='white')
          position.place(height=170, width=720, relx=0.005, rely=0.015)
          LABEL = tk.Label(position, bg='indigo', fg='white', bd='8',
                           text='POR FAVOR INGRESE SU TIEMPO Y REPETICIONES POR EJERCICIO')
          LABEL.place(rely=0, relx=0)
          positiontiempo = tk.Label(position, bg='MediumPurple4', fg='white')
          positiontiempo.place(height=120, width=360, relx=0.1, rely=0.25)

          nombre = Label(positiontiempo, text='DIA', bg='indigo', fg='white').grid(row=1, column=0)
          ingresa_nombre = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_nombre.grid(row=1, column=2)

          nombre = Label(positiontiempo, text='REPETICIONES', bg='indigo', fg='white').grid(row=1, column=4)
          ingresa_repe = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_repe.grid(row=1, column=5)

          apellido = Label(positiontiempo, text='T1', bg='indigo', fg='white').grid(row=2, column=0)
          ingresa_apellido = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_apellido.grid(row=2, column=2)

          edad = Label(positiontiempo, text='T2', bg='indigo', fg='white').grid(row=3, column=0)
          ingresa_edad = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_edad.grid(row=3, column=2)

          correo = Label(positiontiempo, text='T3', bg='indigo', fg='white').grid(row=4, column=0)
          ingresa_correo = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_correo.grid(row=4, column=2)

          telefono = Label(positiontiempo, text='T4', bg='indigo', fg='white').grid(row=5, column=0)
          ingresa_telefono = Entry(positiontiempo, width=13, font=('Arial', 8))
          ingresa_telefono.grid(row=5, column=2)

          agregar = tk.Button(positiontiempo, width=10, text='Guardar', fg='white', bg='indigo', bd=5,
                              command=agregar_datos)
          agregar.place(rely=0.50, relx=0.53)

          button3 = tk.Button(position, width=10, text="Grafico 1", bg='mediumpurple', fg='white', bd=5,
                              command=lambda: grafico3())
          button3.place(rely=0.25, relx=0.70)

          button4 = tk.Button(position, width=10, text="Grafico 2", bg='mediumpurple', fg='white', bd=5,
                              command=lambda: grafico2())
          button4.place(rely=0.45, relx=0.70)

          button5 = tk.Button(position, width=10, text="Grafico 3", bg='mediumpurple', fg='white', bd=5,
                              command=lambda: grafico1())
          button5.place(rely=0.65, relx=0.70)

          button6 = tk.Button(position, width=10, text="Graficos", bg='mediumpurple', fg='white', bd=5,
                              command=lambda: todosgraficos())
          button6.place(rely=0.45, relx=0.85)

          btnIniciar = Button(file_frame, text="Iniciar", fg='white', bg='indigo', width=10, command=iniciar)
          btnIniciar.place(rely=0.45, relx=0.85)

          lb1 = Label(root, text='NOMBRE', bg='indigo', fg='white').place(rely=0.02, relx=0.30)
          entry1 = Entry(root, width=13, font=('Arial', 8))
          entry1.place(rely=0.02, relx=0.35)

          lb2 = Label(root, text='EJERCICIO', bg='indigo', fg='white').place(rely=0.02, relx=0.45)
          entry2 = Entry(root, width=13, font=('Arial', 8))
          entry2.place(rely=0.02, relx=0.5)

          def start():
              global running
              if not running:
                  update()
                  running = True

          # pause function
          def pause():
              global running
              if running:
                  stopwatch_label.after_cancel(update_time)
                  running = False

          # reset function
          def reset():
              global running
              if running:
                  stopwatch_label.after_cancel(update_time)
                  running = False
              global minutes, seconds
              minutes, seconds = 0, 0
              stopwatch_label.config(text='00:00')

          # update stopwatch function
          def update():
              global hours, minutes, seconds
              seconds += 1
              if seconds == 60:
                  minutes += 1
                  seconds = 0
              if minutes == 60:
                  hours += 1
                  minutes = 0
              minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
              seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
              # update timer label after 1000 ms (1 second)
              stopwatch_label.config(text=minutes_string + ':' + seconds_string)
              # after each second (1000 milliseconds), call update function
              # use update_time variable to cancel or pause the time using after_cancel
              global update_time
              update_time = stopwatch_label.after(1000, update)

          # label to display time
          stopwatch_label = Label(file_frame1, text='00:00', font=('Arial', 40))
          stopwatch_label.pack()

          # start, pause, reset, quit buttons
          start_button = tk.Button(file_frame1, text='start', height=3, width=6, font=('Arial'), command=start)
          start_button.place(rely=0.5, relx=0.2)
          pause_button = tk.Button(file_frame1, text='pause', height=3, width=6, font=('Arial'), command=pause)
          pause_button.place(rely=0.5, relx=0.4)
          reset_button = tk.Button(file_frame1, text='reset', height=3, width=6, font=('Arial'), command=reset)
          reset_button.place(rely=0.5, relx=0.6)
          self.image = Image.open("C:fondorespo.png")
          self.img_copy = self.image.copy()

          self.background_image = ImageTk.PhotoImage(self.image)

          self.background = Label(self, image=self.background_image)
          self.background.pack(fill=BOTH, expand=YES)
          self.background.bind('<Configure>', self._resize_image)

      def _resize_image(self, event):

          new_width = event.width
          new_height = event.height

          self.image = self.img_copy.resize((new_width, new_height))

          self.background_image = ImageTk.PhotoImage(self.image)
          self.background.configure(image=self.background_image)


  e = Example(root)
  e.pack(fill=BOTH, expand=YES)
  root.mainloop()


except:
  print("Contraseña o Email invalido")
