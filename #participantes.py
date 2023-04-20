#participantes
import os
import time
import random

tiempo=[5,4,3,2,1,]
pers=[]
premio=0
premiop2=0
premiop3=0
premiop4=0
premiop5=0
def subasta():
    tiempo=[5,4,3,2,1,0]
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
    while True:
     print("_-------------------------------_")
     print("nuestro primer objeto es un anillo de diamate ")
     print("comenzamos con $6,000")
     print("_-------------------------------_")
     oferta=int(input("cuanto vas a ofrecer?--->"))
     print(pat1,"ofrece")
     print(oferta)
     pers.append(oferta)

     a2=random.randint(5000,10000)
     print(pat2,"ofrece")
     print(a2) 
     pers.append(a2)

     a3=random.randint(5000,10000)
     print(pat3,"ofrece")
     print(a3)
     pers.append(a3)

     a4=random.randint(5000,10000)
     print(pat4,"ofrece")
     print(a4)
     pers.append(a4) 

     a5=random.randint(5000,10000)
     print(pat5,"ofrece")
     print(a5)
     pers.append(a5)
     
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

    while True:
     print("_-------------------------------_")
     print("nuestro segundo objeto es una pintura antigua ")
     print("comenzamos con $3000")
     print("_-------------------------------_")
     oferta=int(input("cuanto vas a ofrecer?--->"))
     print(pat1,"ofrece")
     print(oferta)
     pers.append(oferta)

     a2=random.randint(5000,10000)
     print(pat2,"ofrece")
     print(a2) 
     pers.append(a2)

     a3=random.randint(5000,10000)
     print(pat3,"ofrece")
     print(a3)
     pers.append(a3)

     a4=random.randint(5000,10000)
     print(pat4,"ofrece")
     print(a4)
     pers.append(a4) 

     a5=random.randint(5000,10000)
     print(pat5,"ofrece")
     print(a5)
     pers.append(a5)
     
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

    while True:
     print("_-------------------------------_")
     print("nuestro tercer objeto es una libro que relata del año 1780 ")
     print("comenzamos con $2000")
     print("_-------------------------------_")
     if premio >= 3:
      print("Este participante ya no puede participar mas")
     elif premio <= 2:
      oferta=int(input("cuanto vas a ofrecer?--->"))
      print(pat1,"ofrece")
      print(oferta)
      pers.append(oferta)

     if premiop2 >= 3:
      print("Este participante ya no puede participar mas")
     elif premiop2 <= 2:
      a2=random.randint(5000,10000)
      print(pat2,"ofrece")
      print(a2) 
      pers.append(a2)

     if premiop3 >= 3:
      print("Este participante ya no puede participar mas")
     elif premiop3 <=2:
      a3=random.randint(5000,10000)
      print(pat3,"ofrece")
      print(a3)
      pers.append(a3)

     if premiop4 >= 3:
      print("Este participante ya no puede participar mas")
     elif premiop4 <=2:
      a4=random.randint(5000,10000)
      print(pat4,"ofrece")
      print(a4)
      pers.append(a4) 

     if premiop5 >= 3:
      print("Este participante ya no puede participar mas")
     elif premiop5 <=2:
      a5=random.randint(5000,10000)
      print(pat5,"ofrece")
      print(a5)
      pers.append(a5)
      
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

    while True:
     print("_-------------------------------_")
     print("nuestro cuarto objeto es un smartphone lleno de piedras preciosas ")
     print("comenzamos con $7000")
     print("_-------------------------------_")
     if premio >= 3:
       print("El participante",pat1," ya no puede participar mas")
     elif premio <= 2:
      oferta=int(input("cuanto vas a ofrecer?--->"))
      print(pat1,"ofrece")
      print(oferta)
      pers.append(oferta)

     if premiop2 >= 3:
       print("Este participante ya no puede participar mas")
     elif premiop2 <= 2:
      a2=random.randint(5000,10000)
      print(pat2,"ofrece")
      print(a2) 
      pers.append(a2)

     if premiop3 >= 3:
       print("Este participante ya no puede participar mas")
     elif premiop3 <= 2:
      a3=random.randint(5000,10000)
      print(pat3,"ofrece")
      print(a3)
      pers.append(a3)

     if premiop4 >= 3:
       print("Este participante ya no puede participar mas")
     elif premiop4 <= 2:
       a4=random.randint(5000,10000)
       print(pat4,"ofrece")
       print(a4)
       pers.append(a4) 
     if premiop5 >= 3:
       print("Este participante ya no puede participar mas")
     elif premiop5 <= 2:
       a5=random.randint(5000,10000)
       print(pat5,"ofrece")
       print(a5)
       pers.append(a5)
     
     if premio >= 3:
       print("ya no puedes aportar -_- vete ")
       opc=input(("presione n para continuar----->"))
       oferta=1
       break
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

    while True:
     print("_-------------------------------_")
     print("nuestro ultimo objeto es un caja llena de reliquias antiguas ")
     print("comenzamos con $7000")
     print("_-------------------------------_")
     ops=input("quieres dejar la subasta s/n--->")
     if ops =="n":
        if premio >= 3:
         print("Este participante ya no puede participar mas")
        elif premio <= 2:
         oferta=int(input("cuanto vas a ofrecer?--->"))
        print(pat1,"ofrece")
        print(oferta)
        pers.append(oferta)

        if premiop2 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop2 <= 2:
         a2=random.randint(5000,10000)
        print(pat2,"ofrece")
        print(a2) 
        pers.append(a2)

        if premiop3 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop3 <= 2:
         a3=random.randint(5000,10000)
        print(pat3,"ofrece")
        print(a3)
        pers.append(a3)

        if premiop4 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop4 <= 2:
         a4=random.randint(5000,10000)
        print(pat4,"ofrece")
        print(a4)
        pers.append(a4) 

        if premiop5 >= 3:
         print("Este participante ya no puede participar mas")
        elif premiop5 <= 2:
         a5=random.randint(5000,10000)
         print(pat5,"ofrece")
         print(a5)
         pers.append(a5)
        
        if premio >= 3:
         print("ya no puedes aportar -_- vete ")
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