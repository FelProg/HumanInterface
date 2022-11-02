import os
#declaracion de variables
opcion,Led1,Led2,Led3,Led4,all="0","off","off","off","off","on"
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
        if Led1 == "off":
            Led1 = "on"
        else:
            Led1 = "off"
    elif opcion == "2":
        if Led2 == "off":
            Led2 = "on"
        else:
            Led2 = "off"
    elif opcion == "3":
        if Led3 == "off":
            Led3 = "on"
        else:
            Led3 = "off"
    elif opcion == "4":
        if Led4 == "off":
            Led4 = "on"
        else:
            Led4 = "off"
    elif opcion == "5":
        if all == "off":
            all,Led4,Led3,Led2,Led1 = "on","off","off","off","off"
        else:
            all,Led4,Led3,Led2,Led1 = "off","on","on","on","on"
    elif opcion == "6":
        print("\n\tGracias por utilizar el sistema")
    else:
        print("\n\tLa opcion seleccionada no esta disponible\n")
    
   


            
    
        



