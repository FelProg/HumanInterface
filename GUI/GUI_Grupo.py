
from tkinter import *
from tkinter import messagebox, Button
from tkinter.font import BOLD,Font
from PIL import Image,ImageTk
import serial

error = 0
ventana_Principal = Tk()
try:
    arduino =serial.Serial("/dev/cu.usbmodem14101",9600)
except:
    error = 1

#declarar funcion
def ConmutarLED(boton, numeroLED, letra) : 
   
    if boton["text"] == "Apagar LED "+ numeroLED :
        boton["text"] = "Encender LED "+ numeroLED
        arduino.write(bytes(letra.upper(), 'utf-8'))
    else:
        boton["text"] = "Apagar LED "+ numeroLED
        arduino.write(bytes(letra, 'utf-8'))

def Salir() :
    ventana_Principal.destroy()

def EncenderTodos():
    arduino.write(bytes("a",'utf-8'))
    boton_Led1["text"] = "Apagar LED 1"
    arduino.write(bytes("b",'utf-8'))
    boton_Led2["text"] = "Apagar LED 2"
    arduino.write(bytes("c",'utf-8'))
    boton_Led3["text"] = "Apagar LED 3"
    arduino.write(bytes("d",'utf-8'))
    boton_Led4["text"] = "Apagar LED 4"

def ApagarTodos() :
    arduino.write(bytes("A",'utf-8'))
    boton_Led1["text"] = "Apagar LED 1"
    arduino.write(bytes("B",'utf-8'))
    boton_Led2["text"] = "Apagar LED 2"
    arduino.write(bytes("C",'utf-8'))
    boton_Led3["text"] = "Apagar LED 3"
    arduino.write(bytes("D",'utf-8'))
    boton_Led4["text"] = "Apagar LED 4"


etiqueta_Titulo = Label(ventana_Principal, text="")

boton_Led1 = Button(text="apagar LED 1",command=lambda: ConmutarLED(boton_Led1,"1","a"))
boton_Led1.place(x=16, y=60)

boton_Led2 = Button(text="apagar LED 2",command=lambda: ConmutarLED(boton_Led2,"2","b"))
boton_Led2.place(x=16, y=92)

boton_Led3 = Button(text="apagar LED 3",command=lambda: ConmutarLED(boton_Led3,"3","c"))
boton_Led3.place(x=16, y=124)

boton_Led4 = Button(text="apagar LED 4",command=lambda: ConmutarLED(boton_Led4,"4","d"))
boton_Led4.place(x=16, y=156)

boton_ApagarTodos = Button(text="Apagar Todos" ,command=ApagarTodos)
boton_ApagarTodos.place(x=16, y=188)

boton_EncenderTodos = Button(text="Encender Todos", command=EncenderTodos)
boton_EncenderTodos.place(x=16, y=220)

if error == 1:
    boton_Led1["state"] = "disabled"
    boton_Led2["state"] = "disabled"
    boton_Led3["state"] = "disabled"
    boton_Led4["state"] = "disabled"
    boton_EncenderTodos["state"] = "disabled"
    boton_ApagarTodos["state"] = "disabled"

    label_Error = Label(text = "Error: no se cuenta con acceso al control de la casa")
    label_Error.place(x=16, y=290)

boton_Salir = Button(text="salir", command=Salir)
boton_Salir.place(x=16, y=256)


ventana_Principal.geometry("660x440")
ventana_Principal.title("Sistema para el control de iluminacion casero")

etiqueta_Titulo.place(x=8, y=8)

ventana_Principal.mainloop()