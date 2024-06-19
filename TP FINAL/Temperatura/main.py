from tkinter import PhotoImage, messagebox, Label, Tk, StringVar, CENTER, ttk, Entry, Button


def validarNumero(inicio):
    if (not inicio.isdigit()):   #pregunto si no es dígito
       messagebox.showerror(title="ERROR", message="La temperatura inicial debe ser un valor numérico")

def fromRankine(inicio, fin):
    if(fin == "Rankine"):
        return inicio * 1
    elif (fin == "Celsius"):
        return (inicio - 491.67) * 5/9
    elif (fin == "Fahrenheit"):
        return inicio - 459.67
    elif (fin == "Kelvin"):
        return inicio * 5/9 
    else: 
        messagebox.showwarning(title="ADVERTENCIA", message="Seleccione una Unidad de temperatura final")
        return('')

def fromCelsius(inicio, fin):
    if(fin == "Rankine"):
        return (inicio * 9/5) + 491.67
    elif (fin == "Celsius"):
        return inicio * 1
    elif (fin == "Fahrenheit"):
        return (inicio * 9/5) + 32
    elif (fin == "Kelvin"):
        return inicio + 273.15
    else: 
        messagebox.showwarning(title="ADVERTENCIA", message="Seleccione una Unidad de temperatura final")
        return('')
    
def fromFahrenheit(inicio, fin):
    if(fin == "Rankine"):
        return inicio + 459.67
    elif (fin == "Celsius"):
        return (inicio - 32) * 5/9
    elif (fin == "Fahrenheit"):
        return inicio * 1
    elif (fin == "Kelvin"):
        return ((inicio - 32) * 5/9 ) + 273.15
    else: 
        messagebox.showwarning(title="ADVERTENCIA", message="Seleccione una Unidad de temperatura final")
        return('')

def fromKelvin(inicio, fin):
    if(fin == "Rankine"):
        return inicio * 9/5,
    elif (fin == "Celsius"):
        return inicio - 273.15 
    elif (fin == "Fahrenheit"):
        return ((inicio - 273.15) * 9/5) + 32
    elif (fin == "Kelvin"):
        return inicio * 1
    else: 
        messagebox.showwarning(title="ADVERTENCIA", message="Seleccione una Unidad de temperatura final")
        return('')


def convertir():
    global inicio  
    if(sInicio.get() == ""):
        messagebox.showwarning(title="ADVERTENCIA", message="Seleccione una Unidad de temperatura inicial")
        return
    
    validarNumero(inicio.get())
    if(sInicio.get() == "Rankine"):
        tFinal.set(fromRankine(eval(inicio.get()), sFin.get()))
    elif (sInicio.get() == "Celsius"):
         tFinal.set(fromCelsius(eval(inicio.get()), sFin.get()))
    elif (sInicio.get() == "Fahrenheit"):
        tFinal.set(fromFahrenheit(eval(inicio.get()), sFin.get()))
    elif (sInicio.get() == "Kelvin"):
        tFinal.set(fromKelvin(eval(inicio.get()),sFin.get()))    

def limpiar():  
    global inicio
    global fin 
    inicio.set('')
    fin.set('')

#unidades = [{'key':'Celsius', 'value':10},{'key':'Celsius', 'value':10},{'key':'Celsius', 'value':10},{'key':'Celsius', 'value':10}]

ventana = Tk()
ventana.configure(background='#f2f2f2')
ventana.title('Conversor de Temperatura v1.0')
ventana.resizable(False,False)

img = PhotoImage(file='Tecno3F/Inicial/TP FINAL/Temperatura/temp.png')
ventana.tk.call('wm', 'iconphoto', ventana._w, img)

ventana.update_idletasks()
width = 570
frm_width = ventana.winfo_rootx() - ventana.winfo_x()
win_width = width + 2*frm_width
height = 220
titlebar_height = ventana.winfo_rooty() - ventana.winfo_y()
win_height = height + titlebar_height + frm_width
x = ventana.winfo_screenwidth()//2 - win_width//2
y = ventana.winfo_screenheight()//2 - win_height//2
ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))
ventana.deiconify()

titulo = Label(ventana, text="Conversor de Temperatura ")
titulo.grid(row=1, column=0, columnspan=8, ipadx=10, ipady=5, pady=15)

tInicio = StringVar()
tInicio.set('')

sInicio = ttk.Combobox(ventana,
    state="readonly",
    values=["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
)
sInicio.grid(row=4 , column=0, columnspan=2, ipadx=10, padx=20, ipady=5, pady=10)
inicio = Entry(ventana, width=23, textvariable=tInicio)
inicio.grid(row=6 , column=0, columnspan=3, ipadx=10, padx=20, ipady=5, pady=10)

btn1 = Button(ventana, text='Convertir' , bg='purple' , fg='white',width=15 , height=2, command= lambda: convertir())
btn1.grid(row=4 , column=3, ipadx=7)

tFinal = StringVar()
tFinal.set('')

sFin = ttk.Combobox(ventana,
    state="readonly",
    values=["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
)
sFin.grid(row=4, column=4, columnspan=2, ipadx=10, padx=20, ipady=5, pady=10)
fin = Entry(ventana, width=23,textvariable=tFinal,state='disabled')
fin.grid(row=6, column=4, columnspan=3, ipadx=10, padx=20, ipady=5, pady=20)


footer = Label(ventana, text="Tecno 3F - Python Inicial - 2024")
footer.grid(row=10, column=0, columnspan=3, ipady=5, pady=10)
footer = Label(ventana, text="Baglivo Matías & Pinasco Marina")
footer.grid(row=10, column=5, columnspan=3, pady=10)


ventana.mainloop()