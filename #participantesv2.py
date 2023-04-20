#participantes
import os
import time


tiempo=[5,4,3,2,1,]
pers=[]
premio=0
premiop2=0
premiop3=0
premiop4=0
premiop5=0
def subasta():
    tiempo=[5,4,3,2,1,]
    pers=[]
    print("bienvenido incribase para iniciar la subasta")
    pat1=input(("ingrese su nombre---->"))
    pat2=input(("ingrese su nombre---->"))
    pat3=input(("ingrese su nombre---->"))
    pat4=input(("ingrese su nombre---->"))
    pat5=input(("ingrese su nombre---->"))
    o=(input("todo listo oprima enter para continuar____"))
    os.system("cls")
    premio=0
    premiop2=0
    premiop3=0
    premiop4=0
    premiop5=0

    print("_-------------------------------_")
    print("nuestro primer objeto es un anillo de diamate ")
    print("comenzamos con $6,000")
    print("_-------------------------------_")
    while True:
     
     print(pat1)
     oferta=(input("cuanto vas a ofrecer?--->"))
     if oferta.isnumeric():
      print(pat1,"ofrece",oferta)
      pers.append(oferta)
      print("el nuevo valor del reloj es de",oferta)
     else:
       print("caracter invalido")
     


     print("----------------------------------------------")

     print(pat2)
     a2=(input("cuanto vas a ofrecer?--->"))
     if a2.isnumeric():
      print(pat2,"ofrece",a2)
      pers.append(a2)
     else:
       print("caracter invalido")

     if a2 >= oferta:
       oferta=a2
       print("el nuevo valor del reloj es de",oferta)
     else:
      print("el valor de el reloj sigue igual",oferta)

     print("----------------------------------------------")

     print(pat3)
     a3=(input("cuanto vas a ofrecer?--->"))
     if a3.isnumeric():
      print(pat3,"ofrece",a3)
      pers.append(a3)
     else:
       print("caracter invalido")

     if a3 >= oferta:
       oferta=a3
       print("el nuevo valor del reloj es de",oferta)
     else:
      print("el valor de el reloj sigue igual",oferta)
      
      
     print("----------------------------------------------")

     print(pat4)
     a4=(input("cuanto vas a ofrecer?--->"))
     if a4.isnumeric():
      print(pat4,"ofrece",a4)
      pers.append(a4)
     else:
       print("caracter invalido")

     if a4 >= oferta:
       oferta=a4
       print("el nuevo valor del reloj es de",oferta)
     else:
      print("el valor de el reloj sigue igual",oferta)
      
     print("----------------------------------------------")

     print(pat5)
     a5=(input("cuanto vas a ofrecer?--->"))
     if a5.isnumeric():
      print(pat5,"ofrece",a5)
      pers.append(a5)
     else:
       print("caracter invalido")

     if a5 >= oferta:
       oferta=a5
       print("el nuevo valor del reloj es de",oferta)
     else:
      print("el valor de el reloj sigue igual",oferta)
      print("----------------------------------------------")

      opc=input(("quieres hacer otra puja s/n----->"))
     if opc =="n":
        os.system("cls")
        for n in tiempo:
         print(n)
         time.sleep(1)
        print("!Listo se acabo el tiempo!")
        o=max(pers)
        int(o)
        if o == oferta:
            print("vendido a ",pat1,"por",oferta)
            premio=premio+1 
            break
        elif o ==a2:
            print("vendido a ",pat2,"por",a2)
            premiop2=premiop2+1
            break
        elif o ==a3:
            print("vendido a ",pat3,"por",a3)
            premiop3=premiop3+1
            break
        elif o ==a4:
            print("vendido a ",pat3,"por",a4)
            premiop4=premiop4+1
            break
        elif o ==a5:
            print("vendido a ",pat5,"por",a5) 
            premiop5=premiop5+1
            break
     elif opc=="s":
       os.system("cls")
  
    pers.clear
    
    print("_-------------------------------_")
    print("nuestro segundo objeto es una pintura antigua ")
    print("comenzamos con $3000")
    print("_-------------------------------_")
    while True:
     
     print(pat1)
     oferta=(input("cuanto vas a ofrecer?--->"))
     if oferta.isnumeric():
      print(pat1,"ofrece",oferta)
      pers.append(oferta)
      print("el nuevo valor de la pintura es de",oferta)
     else:
       print("caracter invalido")

     print("----------------------------------------------")

     print(pat2)
     a2=(input("cuanto vas a ofrecer?--->"))
     if a2.isnumeric():
      print(pat2,"ofrece",a2)
      pers.append(a2)
     else:
       print("caracter invalido")

     if a2 >= oferta:
       oferta=a2
       print("el nuevo valor de la pintura es de",oferta)
     else:
      print("el valor de la pintura sigue igual",oferta)

     print("----------------------------------------------")

     print(pat3)
     a3=(input("cuanto vas a ofrecer?--->"))
     if a3.isnumeric():
      print(pat3,"ofrece",a3)
      pers.append(a3)
     else:
       print("caracter invalido")

     if a3 >= oferta:
       oferta=a3
       print("el nuevo valor de la pintura es de",oferta)
     else:
      print("el valor de la pintura sigue igual",oferta)
      
      
     print("----------------------------------------------")

     print(pat4)
     a4=(input("cuanto vas a ofrecer?--->"))
     if a4.isnumeric():
      print(pat4,"ofrece",a4)
      pers.append(a4)
     else:
       print("caracter invalido")

     if a4 >= oferta:
       oferta=a4
       print("el nuevo valor de la pintura es de",oferta)
     else:
      print("el valor de la pintura sigue igual",oferta)
      
     print("----------------------------------------------")

     print(pat5)
     a5=(input("cuanto vas a ofrecer?--->"))
     if a5.isnumeric():
      print(pat5,"ofrece",a5)
      pers.append(a5)
     else:
       print("caracter invalido")

     if a5 >= oferta:
       oferta=a5
       print("el nuevo valor de la pintura es de",oferta)
     else:
      print("el valor de la pintura sigue igual",oferta)
      print("----------------------------------------------")

      opc=input(("quieres hacer otra puja s/n----->"))
     if opc =="n":
        os.system("cls")
        for n in tiempo:
         print(n)
         time.sleep(1)
        print("!Listo se acabo el tiempo!")
        o=max(pers)
        int(o)
        if o == oferta:
            print("vendido a ",pat1,"por",oferta)
            premio=premio+1 
            break
        elif o ==a2:
            print("vendido a ",pat2,"por",a2)
            premiop2=premiop2+1
            break
        elif o ==a3:
            print("vendido a ",pat3,"por",a3)
            premiop3=premiop3+1
            break
        elif o ==a4:
            print("vendido a ",pat3,"por",a4)
            premiop4=premiop4+1
            break
        elif o ==a5:
            print("vendido a ",pat5,"por",a5) 
            premiop5=premiop5+1
            break
     elif opc=="s":
       os.system("cls")
   
    pers.clear
    
    print("_-------------------------------_")
    print("nuestro tercer objeto es una libro que relata del año 1780 ")
    print("comenzamos con $2000")
    print("_-------------------------------_")
    while True:
     
     print(pat1)
     oferta=(input("cuanto vas a ofrecer?--->"))
     if oferta.isnumeric():
      print(pat1,"ofrece",oferta)
      pers.append(oferta)
      print("el nuevo valor de la pintura es de",oferta)
     else:
       print("caracter invalido")

     print("----------------------------------------------")

     print(pat2)
     a2=(input("cuanto vas a ofrecer?--->"))
     if a2.isnumeric():
      print(pat2,"ofrece",a2)
      pers.append(a2)
     else:
       print("caracter invalido")

     if a2 >= oferta:
       oferta=a2
       print("el nuevo valor del libro es de",oferta)
     else:
      print("el valor del libro sigue igual",oferta)

     print("----------------------------------------------")

     print(pat3)
     a3=(input("cuanto vas a ofrecer?--->"))
     if a3.isnumeric():
      print(pat3,"ofrece",a3)
      pers.append(a3)
     else:
       print("caracter invalido")

     if a3 >= oferta:
       oferta=a3
       print("el nuevo valor del libro es de",oferta)
     else:
      print("el valor del libro sigue igual",oferta)
      
      
     print("----------------------------------------------")

     print(pat4)
     a4=(input("cuanto vas a ofrecer?--->"))
     if a4.isnumeric():
      print(pat4,"ofrece",a4)
      pers.append(a4)
     else:
       print("caracter invalido")

     if a4 >= oferta:
       oferta=a4
       print("el nuevo valor del libro es de",oferta)
     else:
      print("el valor del libro sigue igual",oferta)
      
     print("----------------------------------------------")

     print(pat2)
     a5=(input("cuanto vas a ofrecer?--->"))
     if a5.isnumeric():
      print(pat5,"ofrece",a5)
      pers.append(a5)
     else:
       print("caracter invalido")

     if a5 >= oferta:
       oferta=a5
       print("el nuevo valor del libro es de",oferta)
     else:
      print("el valor de el libro sigue igual",oferta)
      print("----------------------------------------------")

      opc=input(("quieres hacer otra puja s/n----->"))
     if opc =="n":
        os.system("cls")
        for n in tiempo:
         print(n)
         time.sleep(1)
        print("!Listo se acabo el tiempo!")
        o=max(pers)
        int(o)
        if o == oferta:
            print("vendido a ",pat1,"por",oferta)
            premio=premio+1 
            break
        elif o ==a2:
            print("vendido a ",pat2,"por",a2)
            premiop2=premiop2+1
            break
        elif o ==a3:
            print("vendido a ",pat3,"por",a3)
            premiop3=premiop3+1
            break
        elif o ==a4:
            print("vendido a ",pat3,"por",a4)
            premiop4=premiop4+1
            break
        elif o ==a5:
            print("vendido a ",pat5,"por",a5) 
            premiop5=premiop5+1
            break
     elif opc=="s":
       os.system("cls")

    pers.clear

    print("_-------------------------------_")
    print("nuestro cuarto objeto es un smartphone lleno de piedras preciosas ")
    print("comenzamos con $7000")
    print("_-------------------------------_")
    while True:
     
     ops=input("quieres dejar la subasta s/n")
     if ops =="n":
        if premio >= 3:
         print("Este participante ya no puede participar mas")
        elif premio <= 2:
         print(pat1)
         oferta=(input("cuanto vas a ofrecer?--->"))
         if oferta.isnumeric():
          print(pat1,"ofrece",oferta)
          pers.append(oferta)
          print("el nuevo valor del smartphone es de",oferta)
         else:
          print("caracter invalido")

        if premiop2 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop2 <= 2:
         a2=(input("cuanto vas a ofrecer?--->"))
         if a2.isnumeric():
            print(pat2,"ofrece",a2)
            pers.append(a2)
         else:
           print("caracter invalido")
         
         if a2 >= oferta:
            oferta=a2
            print("el nuevo valor del smartphone es de",oferta)
         else:
           print("el valor del smartphone sigue igual",oferta)
           

        if premiop3 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop3 <= 2:
         a3=(input("cuanto vas a ofrecer?--->"))
         if a3.isnumeric():
           print(pat3,"ofrece",a3)
           pers.append(a3)
         else:
          print("caracter invalido")

         if a3 >= oferta:
           oferta=a3
           print("el nuevo valor del smartphone es de",oferta)
         else:
          print("el valor del smartphone sigue igual",oferta)

        if premiop4 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop4 <= 2:
         a4=(input("cuanto vas a ofrecer?--->"))
         if a4.isnumeric():
           print(pat4,"ofrece",a4)
           pers.append(a4)
         else:
          print("caracter invalido")

         if a4 >= oferta:
          oferta=a4
          print("el nuevo valor del smartphone es de",oferta)
         else:
          print("el valor de el smartphone sigue igual",oferta)

        if premiop5 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop5 <= 2:
         a5=(input("cuanto vas a ofrecer?--->"))
         if a5.isnumeric():
           print(pat5,"ofrece",a5)
           pers.append(a5)
         else:
          print("caracter invalido")
          
         if a5 >= oferta:
          oferta=a5
          print("el nuevo valor del smartphone es de",oferta)
         else:
          print("el valor de el smartphone sigue igual",oferta)
        
        elif premio <= 2:
         opc=input(("quieres hacer otra puja s/n----->"))
        if opc =="n":
           os.system("cls")
           for n in tiempo:
               print(n)
               time.sleep(1)
           print("!Listo se acabo el tiempo!")
           o=max(pers)
           int(o)
           if o == oferta:
                print("vendido a ",pat1,"por",oferta)
                premio=premio+1
           elif o ==a2:
                print("vendido a ",pat2,"por",a2)
                premiop2=premiop2+1
                break
           elif o ==a3:
                print("vendido a ",pat3,"por",a3)
                premiop3=premiop3+1
                break
           elif o ==a4:
                print("vendido a ",pat3,"por",a4)
                premiop4=premiop4+1
                break
           elif o ==a5:
                print("vendido a ",pat5,"por",a5) 
                premiop5=premiop5+1
                break
     elif opc=="s":
      os.system("cls")
     print("gracias por haber participado bye")
     break

    
    pers.clear

    print("_-------------------------------_")
    print("nuestro ultimo objeto es un caja llena de reliquias antiguas ")
    print("comenzamos con $7000")
    print("_-------------------------------_")
    while True:
     
     ops=input("quieres dejar la subasta s/n")
     if ops =="n":
        if premio >= 3:
         print("Este participante ya no puede participar mas")
        elif premio <= 2:
         print(pat1)
         oferta=(input("cuanto vas a ofrecer?--->"))
         if oferta.isnumeric():
          print(pat1,"ofrece",oferta)
          pers.append(oferta)
          print("el nuevo valor del reloj es de",oferta)
         else:
          print("caracter invalido")

        if premiop2 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop2 <= 2:
         a2=(input("cuanto vas a ofrecer?--->"))
         if a2.isnumeric():
            print(pat2,"ofrece",a2)
            pers.append(a2)
         else:
           print("caracter invalido")
         
         if a2 >= oferta:
            oferta=a2
            print("el nuevo valor de la caja es de",oferta)
         else:
           print("el valor de la caja sigue igual",oferta)

        if premiop3 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop3 <= 2:
         a3=(input("cuanto vas a ofrecer?--->"))
         if a3.isnumeric():
           print(pat3,"ofrece",a3)
           pers.append(a3)
         else:
          print("caracter invalido")

         if a3 >= oferta:
           oferta=a3
           print("el nuevo valor de la caja es de",oferta)
         else:
          print("el valor de la caja sigue igual",oferta)

        if premiop4 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop4 <= 2:
         a4=(input("cuanto vas a ofrecer?--->"))
         if a4.isnumeric():
           print(pat4,"ofrece",a4)
           pers.append(a4)
         else:
          print("caracter invalido")

         if a4 >= oferta:
          oferta=a4
          print("el nuevo valor de la caja es de",oferta)
         else:
          print("el valor de la caja sigue igual",oferta)

        if premiop5 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop5 <= 2:
         a5=(input("cuanto vas a ofrecer?--->"))
         if a5.isnumeric():
           print(pat5,"ofrece",a5)
           pers.append(a5)
         else:
          print("caracter invalido")
          
         if a5 >= oferta:
          oferta=a5
          print("el nuevo valor de la caja es de",oferta)
         else:
          print("el valor de la caja sigue igual",oferta)
        
        elif premio <= 2:
         opc=input(("quieres hacer otra puja s/n----->"))
        if opc =="n":
           os.system("cls")
           for n in tiempo:
               print(n)
               time.sleep(1)
           print("!Listo se acabo el tiempo!")
           o=max(pers)
           int(o)
           if o == oferta:
                print("vendido a ",pat1,"por",oferta)
                premio=premio+1
           elif o ==a2:
                print("vendido a ",pat2,"por",a2)
                premiop2=premiop2+1
                break
           elif o ==a3:
                print("vendido a ",pat3,"por",a3)
                premiop3=premiop3+1
                break
           elif o ==a4:
                print("vendido a ",pat3,"por",a4)
                premiop4=premiop4+1
                break
           elif o ==a5:
                print("vendido a ",pat5,"por",a5) 
                premiop5=premiop5+1
                break
     elif opc=="s":
      os.system("cls")
     print("gracias por haber participado bye")
     break
    


    
    







subasta()