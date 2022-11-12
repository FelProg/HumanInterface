#import
from tkinter import *
from tkinter import messagebox, Button
from tkinter.font import BOLD,Font
from PIL import Image,ImageTk

ventana_Principal = Tk()

#declarar funcion
def ConmutarLED(boton, numeroLED) : 
    # print("Presionaron un boton")
    # messagebox.showinfo("Informacion","Boton encendido")
    if boton["text"] == "Apagar LED "+ numeroLED :
        boton["text"] = "Encender LED "+ numeroLED
    else:
        boton["text"] = "Apagar LED "+ numeroLED
        

etiqueta_Titulo = Label(ventana_Principal, text="")

boton_Led1 = Button(text="apagar LED 1",command=lambda: ConmutarLED(boton_Led1,"1"))
boton_Led1.place(x=16, y=60)

boton_Led2 = Button(text="apagar LED 2",command=lambda: ConmutarLED(boton_Led2,"2"))
boton_Led2.place(x=16, y=92)

boton_Led3 = Button(text="apagar LED 3",command=lambda: ConmutarLED(boton_Led3,"3"))
boton_Led3.place(x=16, y=124)

boton_Led4 = Button(text="apagar LED 4",command=lambda: ConmutarLED(boton_Led4,"4"))
boton_Led4.place(x=16, y=156)

boton_ConmutarTodos = Button(text="conmutar todos")
boton_ConmutarTodos.place(x=16, y=188)


boton_Salir = Button(text="salir")
boton_Salir.place(x=16, y=220)


ventana_Principal.geometry("660x440")
ventana_Principal.title("Sistema para el control de iluminacion casero")

etiqueta_Titulo.place(x=8, y=8)

ventana_Principal.mainloop()