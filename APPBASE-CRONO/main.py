#APP CON CRONO Y CAM, FUNCIONAN MAL
import pandas as pd
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

fondo = tk.PhotoImage(file="fondo.png")
fondo1 = tk.Label(root, image=fondo).place(x=0, y=0)

mi = 0
se = 0
ml = 0
contar = 0
click_lectura = 0
clik_stop = 0
clik_inicio = 0

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

def grafico():
    global exl1, df, valores, gp, canvas, df1, ax1, bar1

    exl1 = "datatime.xlsx"
    df = pd.read_excel(exl1)

    valores = df[["DIA","T4"]]

    df1 = valores.plot.bar(x="DIA", y="T4", rot = 10)
    plt.show()


    figure1 = plt.Figure(figsize=(4.8, 4.3), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().place(x=780, y=300)
    df1 = valores[['DIA','T4']].groupby('DIA').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Ultimo tiempo por dia')


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/Desktop",
                                          title="Seleccionar DATATIME",
                                          filetype=(("xlsx files", "datatime.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == "datatime.xlsx":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row)
    return None

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


def crono():
    global crono, mi, se, ml, contar, clik_stop, clik_inicio
    ventana = Tk()
    ventana.config(bg='black')
    ventana.geometry('500x250')
    ventana.title('Cronometro')
    ventana.minsize(width=500, height=250)

    ventana.columnconfigure(0, weight=2)
    ventana.rowconfigure(0, weight=2)
    ventana.columnconfigure(1, weight=2)
    ventana.rowconfigure(0, weight=2)
    ventana.columnconfigure(2, weight=2)
    ventana.rowconfigure(0, weight=2)
    ventana.columnconfigure(1, weight=2)
    ventana.rowconfigure(1, weight=1)
    ventana.columnconfigure(1, weight=2)
    ventana.rowconfigure(1, weight=1)

    frame1 = Frame(ventana)
    frame1.grid(column=0, row=0, sticky='snew')
    frame2 = Frame(ventana)
    frame2.grid(column=1, row=0, sticky='snew')
    frame3 = Frame(ventana)
    frame3.grid(column=2, row=0, sticky='snew')
    frame4 = Frame(ventana, bg='gray10')
    frame4.grid(row=1, columnspan=3, sticky='snew')
    frame5 = Frame(ventana, bg='black')
    frame5.grid(row=2, columnspan=3, sticky='snew')

    # ---

    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(0, weight=1)
    frame3.columnconfigure(0, weight=1)
    frame3.rowconfigure(0, weight=1)
    frame4.columnconfigure(0, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame5.columnconfigure(0, weight=1)
    frame5.rowconfigure(0, weight=1)

    canvas1 = Canvas(frame1, bg='gray40', width=200, height=200, highlightthickness=0)
    canvas1.grid(column=0, row=0, sticky='nsew')
    canvas2 = Canvas(frame2, bg='gray30', width=200, height=200, highlightthickness=0)
    canvas2.grid(column=0, row=0, sticky='nsew')
    canvas3 = Canvas(frame3, bg='gray20', width=200, height=200, highlightthickness=0)
    canvas3.grid(column=0, row=0, sticky='nsew')

    texto1 = canvas1.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')
    texto2 = canvas2.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')
    texto3 = canvas3.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')

    texto_minutos = canvas1.create_text(1, 1, text='Minutos', font=('Arial', 12, 'bold'), fill='White')
    texto_segundos = canvas2.create_text(1, 1, text='Segundos', font=('Arial', 12, 'bold'), fill='White')
    texto_milisegundos = canvas3.create_text(1, 1, text='Milisegundos', font=('Arial', 10, 'bold'), fill='White')

    circulo1 = canvas1.create_oval(10, 10, 100, 100, outline='red2', width=10)
    circulo2 = canvas2.create_oval(10, 10, 100, 100, outline='medium spring green', width=10)
    circulo3 = canvas3.create_oval(10, 10, 100, 100, outline='magenta2', width=10)

    mi = 0
    se = 0
    ml = 0
    contar = 0
    click_lectura = 0
    clik_stop = 0
    clik_inicio = 0

    def iniciar_pausar():
        global mi, se, ml, contar, clik_stop, clik_inicio
        ml = ml + 1
        if ml == 999:
            ml = 0
            se = se + 1
            if se == 59:
                se = 0
                mi = mi + 1

        contar = inicio.after(1, iniciar_pausar)

        clik_inicio = inicio.grid_forget()
        if clik_inicio is None:
            stop.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
            stop.config(bg='orange', text='DETENER')

    def stop_boton():
        global contar, clik_stop

        clik_stop = stop.grid_forget()
        if clik_stop is None:
            inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
            inicio.config(bg='aqua', text='CONTINUAR')
            inicio.after_cancel(contar)

    def vueltas():
        global mi, se, ml, click_lectura

        click_lectura = click_lectura + 1
        if click_lectura == 1:
            lectura1.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
        elif click_lectura == 2:
            lectura2.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
        elif click_lectura == 3:
            lectura3.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
        elif click_lectura == 4:
            lectura4.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
        elif click_lectura == 5:
            lectura5.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
        elif click_lectura == 6:
            lectura6.config(text='{} → {}:{}:{}'.format(click_lectura, mi, se, ml), fg='white', bg='gray10')
            click_lectura = 0

    def reiniciar():
        global mi, se, ml, contar, click_lectura
        mi = 0
        se = 0
        ml = 0
        click_lectura = 0
        inicio.after_cancel(contar)
        lectura1.configure(text='Lectura 1', fg='white', bg='gray10')
        lectura2.configure(text='Lectura 2', fg='white', bg='gray10')
        lectura3.configure(text='Lectura 3', fg='white', bg='gray10')
        lectura4.configure(text='Lectura 4', fg='white', bg='gray10')
        lectura5.configure(text='Lectura 5', fg='white', bg='gray10')
        lectura6.configure(text='Lectura 6', fg='white', bg='gray10')

        stop.grid_forget()
        inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
        inicio.config(bg='green2', text='INICIAR')

    def coordenadas():
        x = canvas1.winfo_width()
        y = canvas1.winfo_height()

        x1 = int(x - 0.1 * x - 0.1 * y + 25)
        y1 = int(y - 0.1 * x - 0.1 * y + 20)
        x2 = int(x - 0.4 * x - 0.4 * y - 15)
        y2 = int(y - 0.4 * x - 0.4 * y - 30)

        tamano = int(y1 * 0.2 + x1 * 0.1 + 10)
        tamano_texto = int(y1 * 0.02 + x1 * 0.02 + 3)

        # print(x1, y1, x2, y2)
        canvas1.coords(circulo1, x1, y1, x2, y2)
        canvas2.coords(circulo2, x1, y1, x2, y2)
        canvas3.coords(circulo3, x1, y1, x2, y2)

        # cordenas numeros
        z1 = int(x1 * 0.6 - 10)
        z2 = int(y1 * 0.6 - 10)

        # coordenadas texto
        w1 = int(x1 * 0.49 + 8)
        w2 = int(y1 * 0.8 + 10)

        canvas1.coords(texto1, z1, z2)
        canvas2.coords(texto2, z1, z2)
        canvas3.coords(texto3, z1, z2)

        canvas1.itemconfig(texto1, font=('Arial', tamano, 'bold'), text=mi)
        canvas2.itemconfig(texto2, font=('Arial', tamano, 'bold'), text=se)
        canvas3.itemconfig(texto2, font=('Arial', tamano, 'bold'), text=ml)

        canvas1.coords(texto_minutos, w1, w2)
        canvas2.coords(texto_segundos, w1, w2)
        canvas3.coords(texto_milisegundos, w1, w2)

        canvas1.itemconfig(texto_minutos, font=('Arial', tamano_texto, 'bold'))
        canvas2.itemconfig(texto_segundos, font=('Arial', tamano_texto, 'bold'))
        canvas3.itemconfig(texto_milisegundos, font=('Arial', tamano_texto, 'bold'))

        canvas1.after(1000, coordenadas)

    frame4.columnconfigure(0, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(1, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(2, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(3, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(4, weight=1)
    frame4.rowconfigure(0, weight=1)
    frame4.columnconfigure(5, weight=1)
    frame4.rowconfigure(0, weight=1)

    lectura1 = Label(frame4, text='Lectura 1', fg='white', bg='gray10')
    lectura1.grid(column=0, row=0, sticky='nsew')
    lectura2 = Label(frame4, text='Lectura 2', fg='white', bg='gray10')
    lectura2.grid(column=1, row=0, sticky='nsew')
    lectura3 = Label(frame4, text='Lectura 3', fg='white', bg='gray10')
    lectura3.grid(column=2, row=0, sticky='nsew')
    lectura4 = Label(frame4, text='Lectura 4', fg='white', bg='gray10')
    lectura4.grid(column=3, row=0, sticky='nsew')
    lectura5 = Label(frame4, text='Lectura 5', fg='white', bg='gray10')
    lectura5.grid(column=4, row=0, sticky='nsew')
    lectura6 = Label(frame4, text='Lectura 6', fg='white', bg='gray10')
    lectura6.grid(column=5, row=0, sticky='nsew')

    frame5.columnconfigure(0, weight=1)
    frame5.rowconfigure(0, weight=1)
    frame5.columnconfigure(1, weight=1)
    frame5.rowconfigure(0, weight=1)
    frame5.columnconfigure(2, weight=1)
    frame5.rowconfigure(0, weight=1)

    stop = Button(frame5, text='DETENER', relief="raised", bd=5, bg='orange', font=('Arial', 12, 'bold'), width=20,
                  command=stop_boton)
    stop.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

    inicio = Button(frame5, text='INICIAR', relief="raised", bd=5, bg='green2', font=('Arial', 12, 'bold'), width=20,
                    command=iniciar_pausar)
    inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

    vuelta = Button(frame5, text='VUELTA', relief="raised", bd=4, bg='blue2', font=('Arial', 12, 'bold'), width=20,
                    command=vueltas)
    vuelta.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

    fin = Button(frame5, text='RESTABLECER', relief="raised", bd=4, bg='red2', font=('Arial', 12, 'bold'), width=20,
                 command=reiniciar)
    fin.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')

    coordenadas()

    crono.mainloop()

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
    ventana.mainloop()



cap = None
cap2 = None
btnIniciar1 = Button(root, text="Ampliar", width=10, command=ventanacam)
btnIniciar1.place(x=650, y=370)
btnIniciar = Button(root, text="Iniciar", width=10, command=iniciar)
btnIniciar.place(x=650, y=470)
btnFinalizar = Button(root, text="Finalizar", width=10, command=finalizar)
btnFinalizar.place(x=650, y=500)
btncrono = Button(root, text="Cronometro", width=10, command=crono)
btncrono.place(x=650, y=520)

lblVideo = Label(root)
lblVideo.place( x=30, y=95)


file_frame = tk.LabelFrame(root, text="Ingresar datos de tiempo", bg='MediumPurple4', fg='white')
file_frame.place(height=180, width=480, rely=0.13, relx=0.61)

frame1 = tk.LabelFrame(root, text="Excel Data", bg='MediumPurple4', fg='white')
frame1.place(height=170, width=730, rely=0.75, relx=0.02)


nombre = Label(root, text ='DIA',  bg='indigo', fg='white').place(rely=0.16, relx=0.65)
ingresa_nombre = Entry(root,  width=13, font = ('Arial',8))
ingresa_nombre.place(rely=0.16, relx=0.67)

apellido = Label(root, text ='T1', bg='indigo', fg='white').place(rely=0.20, relx=0.65)
ingresa_apellido = Entry(root, width=13, font = ('Arial',8))
ingresa_apellido.place(rely=0.20, relx=0.67)

edad = Label(root, text ='T2', bg='indigo', fg='white').place(rely=0.24, relx=0.65)
ingresa_edad = Entry(root,  width=13, font = ('Arial',8))
ingresa_edad.place(rely=0.24, relx=0.67)

correo = Label(root, text ='T3', bg='indigo', fg='white').place(rely=0.28, relx=0.65)
ingresa_correo = Entry(root,  width=13, font = ('Arial',8))
ingresa_correo.place(rely=0.28, relx=0.67)

telefono = Label(root, text ='T4', bg='indigo', fg='white').place(rely=0.32, relx=0.65)
ingresa_telefono = Entry(root, width=13, font = ('Arial',8))
ingresa_telefono.place(rely=0.32, relx=0.67)

agregar = Button(root, width=7, text='Guardar',fg= 'white', bg='indigo',bd=5, command =agregar_datos)
agregar.place(rely=0.16, relx=0.80)
"""
guardar = Button(root, width=7, text='Guardar',fg= 'white', bg='indigo',bd=5, command =guardar_datos)
guardar.place(rely=0.91, relx=0.80)
"""

# Buttons
button1 = tk.Button(file_frame, text="Buscar Archivo", bg='mediumpurple', fg='white', command=lambda: File_dialog())
button1.place(rely=0.50, relx=0.68)

button2 = tk.Button(file_frame, text="Cargar Datos" ,bg='mediumpurple', fg='white', command=lambda: Load_excel_data())
button2.place(rely=0.50, relx=0.48)

button3 = tk.Button(file_frame, text="Graficar" ,bg='mediumpurple', fg='white', command=lambda: grafico())
button3.place(rely=0.70, relx=0.48)

# The file/file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0.93, relx=0)


## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


root.mainloop()