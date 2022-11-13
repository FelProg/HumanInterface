import os
import serial
#declaracion de variables
opcion,Led1,Led2,Led3,Led4,all="0","apagado","apagado","apagado","apagado","encendido"
arduino = serial.Serial("COM4",9600) #9600 caracteres por segundo
while opcion !="6":
    os.system("cls")
    print("\n\n\tSistema para el control de iluminación casero")
    print("\tPor: Germán Félix 1.0\n\n")
    print("\tMenu principal: \n")
    print("\t1. Led 1 "+Led1)
    print("\t2. Led 2 "+Led2)
    print("\t3. Led 3 "+Led3)
    print("\t4. Led 4 "+Led4)
    print("\t5. Todos "+all)
    print("\t6. Salir\n")
    opcion=input("\t Ingrese la opción deseada:  ")

    if opcion == "1":
        if Led1 == "apagado":
            Led1 = "encendido"
            arduino.write(b'a')
        else:
            Led1 = "apagado"
            arduino.write(b'A')
    elif opcion == "2":
        if Led2 == "apagado":
            Led2 = "encendido"
            arduino.write(b'b')
        else:
            Led2 = "apagado"
            arduino.write(b'B')
    elif opcion == "3":
        if Led3 == "apagado":
            Led3 = "encendido"
            arduino.write(b'c')
        else:
            Led3 = "apagado"
            arduino.write(b'C')
    elif opcion == "4":
        if Led4 == "apagado":
            Led4 = "encendido"
            arduino.write(b'd')
        else:
            Led4 = "apagado"
            arduino.write(b'D')
    elif opcion == "5":
        if all == "apagado":
            all,Led4,Led3,Led2,Led1 = "encendido","apagado","apagado","apagado","apagado"

            arduino.write(b'E')
        else:
            all,Led4,Led3,Led2,Led1 = "apagado","encendido","encendido","encendido","encendido"
            arduino.write(b'e')
    elif opcion == "6":
        print("\n\tGracias por utilizar el sistema")
    else:
        print("\n\tLa opcion seleccionada no esta disponible\n")
arduino.close()
   


            
    
        



