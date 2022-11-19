#import
from tkinter import *
from tkinter import messagebox, Button
from tkinter.font import BOLD,Font
from PIL import Image,ImageTk
import serial


#instancia del puerto serial
#arduino = serial.Serial("COM4",9600) #9600 caracteres por segundo
arduino = serial.Serial("/dev/cu.usbmodem14101")

#instancia de Tk
ventana = Tk()

#variables de estilo
fontSize= 20;
fontFamily='Arial'
windowSize = "800x600"

windowColor = '#f0f0f0' #white
border_color = Frame(ventana, background="orange")

#variables de proporcion para la imagen casa.
imgHeight = 550
imgWidth = int(imgHeight * 0.58)

#configuración de ventana principal
ventana.geometry(windowSize)
ventana.configure(bg=windowColor)
ventana.title("Interfaz de control de iluminacion diseñada para la clase del Dr. Abríl - Por Germán Félix")
ventana.frame()

#importacion de imagenes
image1 = Image.open("house.png")   #importar imagen
image1 = image1.resize((imgWidth,imgHeight), Image.Resampling.LANCZOS) #redimensionar la imagen
casa = ImageTk.PhotoImage(image1) #convierte imagen a un objeto ImageTk

image2 = Image.open("lightBulb.jpg")   
image2 = image2.resize((30,30), Image.Resampling.LANCZOS) 
focoSala = ImageTk.PhotoImage(image2) 
led1 = 'a'

image3 = Image.open("lightBulb.jpg")   
image3 = image3.resize((30,30), Image.Resampling.LANCZOS) 
comedor = ImageTk.PhotoImage(image3) 
led2 = 'b'

image4 = Image.open("lightBulb.jpg")   
image4 = image4.resize((30,30), Image.Resampling.LANCZOS) 
cocina = ImageTk.PhotoImage(image4) 
led3 = 'c'

image5 = Image.open("lightBulb.jpg")   
image5 = image5.resize((30,30), Image.Resampling.LANCZOS) 
cochera = ImageTk.PhotoImage(image5) 
led4 = 'd'

#variables de imagenes
Casa = Label(ventana, image=casa)
FocoSala = Label(ventana, image=focoSala)
FocoComedor = Label(ventana, image=comedor)
FocoCocina = Label(ventana, image=cocina)
FocoCochera = Label(ventana, image=cochera)

#colocacion de la imagen Casa centrada en lado derecho horizontal y verticalmente
Casa.place(x=400+((400-imgWidth)//2), y=((600-imgHeight)//2))

#configuración de frame lateral izquierdo
LSide_Frame = Frame() #creacion del frame
LSide_Frame.pack() #empaquetamiento de Frame
LSide_Frame.config(width="400",height="600",bg="#94856a",bd= 2,relief="flat") 
LSide_Frame.place(relx=0, rely=0)

#configuracion del frame que contiene los labels
Labels_Frame = Frame()
Labels_Frame.pack();
Labels_Frame.config()
Labels_Frame = Frame(highlightbackground="white", highlightthickness=1, width="300",height="150",bg="#000600",bd=1,relief="sunken")
Labels_Frame.place(anchor='w', relx=0.06, rely=0.15)

#configuracion del frame que decora los botones
Control_Frame = Frame()
Control_Frame.pack();
Control_Frame.config()
Control_Frame = Frame(highlightbackground="white", highlightthickness=1, width="300",height="400",bg="#000600",bd=1,relief="sunken")
Control_Frame.place(anchor='w', relx=0.06, rely=0.65)

#texto descriptivo
label = Label(Labels_Frame, text="Sistema de control", fg='white', bg='#000600', font=(fontFamily, fontSize))
label.place(anchor='w', relx=0.15, rely=0.25)
label = Label(Labels_Frame, text="de iluminación", fg='white', bg='#000600', font=(fontFamily, fontSize))
label.place(anchor='w', relx=0.15, rely=0.55)
label = Label(Labels_Frame, text="Zona comercial - Prototipo - V1.0", fg='#e1e1e1', bg='#000600', font=(fontFamily, fontSize-10))
label.place(anchor='w', relx=0.15, rely=0.80)


#funcion para ocultar o mostrar imagen al presionar un boton
def borrarOmostrar(Ubi,UbiX,UbiY,Led, iluminar = None):
    if iluminar == 1:
        Ubi.place(x=UbiX,y=UbiY)
        arduino.write(bytes(Led.lower(), 'utf-8'))
    elif iluminar == 2:
        Ubi.place_forget()
        arduino.write(bytes(Led.upper(), 'utf-8'))
    elif Ubi.place_info() != {}:
        Ubi.place_forget()
        # convierte el string enviado a Led a tipo byte mayuscula para apagarlo
        arduino.write(bytes(Led.upper(), 'utf-8'))
    else:
        Ubi.place(x=UbiX, y=UbiY)
       # convierte el string enviado a Led a tipo byte minuscula para encenderlo
        arduino.write(bytes(Led.lower(), 'utf-8'))

#el boton llama a borrarOmostrar con los parametros(imagen que mostrará, posicion donde se mostrará)
BotonSala = Button(Control_Frame,    text="Cocina", bg='#ffed00',fg="#000600", font=(fontFamily, fontSize-7), width="10",height="3"
,command=lambda: borrarOmostrar(FocoCocina, 400+130, 150, led1))
BotonComedor = Button(Control_Frame, text="Comedor", bg='#ffed00',fg="#000600",font=(fontFamily, fontSize-7),width="10",height="3"
,command=lambda: borrarOmostrar(FocoComedor, 400+130, 230,led2))
BotonCocina = Button(Control_Frame, text="Sala", bg='#ffed00',fg="#000600",font=(fontFamily, fontSize-7),width="10",height="3"
,command=lambda: borrarOmostrar(FocoSala, 400+250, 350,led3))
BotonCochera = Button(Control_Frame, text="Cochera", bg='#ffed00',fg="#000600",font=(fontFamily, fontSize-7),width="10",height="3"
,command=lambda: borrarOmostrar(FocoCochera, 400+250, 450,led4))
BotonDesactivar = Button(Control_Frame, text="Desactivar", bg='#ffed00',fg="#000600",font=(fontFamily, fontSize-7),width="22",height="3"
        ,command=lambda: 
        {
            borrarOmostrar(FocoCochera, "", "",led4, 2), 
            borrarOmostrar(FocoSala, ""+"", "",led1, 2),
            borrarOmostrar(FocoComedor, ""+"", "",led2, 2),
            borrarOmostrar(FocoCocina, ""+"", "",led3, 2)
        })
BotonEncender = Button(Control_Frame, text="Activar", bg='#ffed00',fg="#000600",font=(fontFamily, fontSize-7),width="22",height="3"
        ,command=lambda: 
        {
            borrarOmostrar(FocoCochera, 400+250, 450,led4, 1), 
            borrarOmostrar(FocoSala, 400+250, 350,led1, 1),
            borrarOmostrar(FocoComedor, 400+130, 230,led2, 1),
            borrarOmostrar(FocoCocina, 400+130, 150,led3, 1)
        })

#posicion de los botones
BotonSala.place(anchor='w', relx=0.15, rely=0.2)
BotonComedor.place(anchor='w', relx=0.15, rely=0.4)
BotonCocina.place(anchor='w', relx=0.51, rely=0.2)
BotonCochera.place(anchor='w', relx=0.51, rely=0.4)
BotonDesactivar.place(anchor="w", relx=0.15, rely=0.6)
BotonEncender.place(anchor="w", relx=0.15, rely=0.8)

ventana.mainloop()
#mainloop siempre al final