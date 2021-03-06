from Verificaciones import validReal
from Verificaciones import validText
import time
from  colorama  import  init
init(autoreset=True)

#Diccionarios de Rutas

rutas={"B11":["Sena","Alqueria","Venecia","Madelena","Portal del Sur"],
"M47":["Comuneros","Cll30 Sur","Cll38a Sur","Alqueria","Sevillana","Madelena","Perdomo","Portal del Sur",],
"4":["Comuneros","Santa Isabel","Sena","Cll 30 Sur","Cll 38a Sur","General Santander","Alqueria","Venecia","Sevillana","Madelena","Perdomo","Portal del Sur"],
"B12":["Comuneros","General Santander","Perdomo","Portal del Sur"],
"D22":["Sena","General Santander","Sevillana","Portal del Sur"],
"E44":["Comuneros","Santa Isabel","Alqueria"],
"K43":["Sena","General Santander", "Venecia"],
"G11":["Sena","Alqueria","Venecia ","Madelena ","Portal del Sur"],
"G47":["Comuneros","Cll30 Sur","Cll38a Sur","Alqueria","Sevillana ","Madelena","Perdomo","Portal del Sur",],
"G22":["Sena","General Santander","Sevillana","Portal del Sur"],
"G44":["Comuneros","Santa Isabel","Alqueria"],
"G43":["Sena","General Santander", "Venecia"]}

n={
"Portal del Sur":["4","M47","B11","B12","D22"],"Perdomo":["4","M47","B12"],
"Madelena":["4","B11","M47"],
"Sevillana":["4","D22","M47"],
"Venecia":["4","k43","B11"],
"Alqueria":["4","B11","M47","E44"],
"General Santander":["4","D22","B12","k43"],
"Cll38a Sur":["4","M47"],
"Cll30 Sur":["4","M47"],
"Sena":["4","B11","D22","k43"],
"Santa Isabel":["4","E44"],
"Comuneros":["4","M47","B12","E44"]}

rutasur={
"Portal del Sur":["4","G47","G11","G12","G22"],"Perdomo":["4","G47","G12"],
"Madelena":["4","G11","G47"],
"Sevillana":["4","G22","G47"],
"Venecia":["4","G43","G11"],
"Alqueria":["4","G11","G47","G44"],
"General Santander":["4","G22","G12","G43"],
"Cll38a Sur":["4","G47"],
"Cll30 Sur":["4","G47"],
"Sena":["4","G11","G22","G43"],
"Santa Isabel":["4","G44"],
"Comuneros":["4","G47","G12","G44"]}

p={
"Portal del Sur":["4","G47","G11","G12","G22"],"Perdomo":["4","G47","G12"],
"Madelena":["4","G11","G47"],
"Sevillana":["4","G22","G47"],
"Venecia":["4","G43","G11"],
"Alqueria":["4","G11","G47","G44"],
"General Santander":["4","G22","G12","G43"],
"Cll38a Sur":["4","G47"],
"Cll30 Sur":["4","G47"],
"Sena":["4","G11","G22","G43"],
"Santa Isabel":["4","G44"],
"Comuneros":["4","G47","G12","G44"]}

rutanorte={
"Portal del Sur":["4","M47","B11","B12","D22"],"Perdomo":["4","M47","B12"],
"Madelena":["4","B11","M47"],
"Sevillana":["4","D22","M47"],
"Venecia":["4","k43","B11"],
"Alqueria":["4","B11","M47","E44"],
"General Santander":["4","D22","B12","k43"],
"Cll38a Sur":["4","M47"],
"Cll30 Sur":["4","M47"],
"Sena":["4","B11","D22","k43"],
"Santa Isabel":["4","E44"],
"Comuneros":["4","M47","B12","E44"]}

rutanortefin={
"Portal del Sur":["4","M47","B12","D22"],
"Perdomo":["4","B12","M47"],
"Madelena":["4","M47"],
"Sevillana":["4","D22","M47"],
"Venecia":["4","k42"],
"Alqueria":["4","M47"],
"General Santander":["4","D22","B12","k42"],
"Cll38a Sur":["4","M47"],
"Cll30 Sur":["4","M47"],
"Sena":["4","k42","D22"],
"Santa Isabel":["4"],
"Comuneros":["4","B12","M47"]}

rutasurfin={
"Portal del Sur":["4","G47","G12","G22"],
"Perdomo":["4","G12","G47"],
"Madelena":["4","G47"],
"Sevillana":["4","G22","G47"],
"Venecia":["4","G42"],
"Alqueria":["4","G47"],
"General Santander":["4","G22","G12","G42"],
"Cll38a Sur":["4","G47"],
"Cll30 Sur":["4","G47"],
"Sena":["4","G42","G22"],
"Santa Isabel":["4",],
"Comuneros":["4","G12","G47"]}

#Buses 

Buses=["4","B11","G11","B12","G12","M47","G47","D22","G22","k43","G43","E44","G44"]

class Usuario:
  def __init__(self,name,adress,age,fondos,IDE,edd):
    self.name=name
    self.edd=edd
    self.adress=adress
    self.age=age
    self.fondos=fondos
    self.IDE=IDE
    if(self.age<=17):
      self.ErrorDeEdad("m")
    if(self.age>=85):
      self.ErrorDeEdad("M")
  def ErrorDeEdad(self,longer):
    self.edd=True
    self.longer=longer
    if(self.longer=="m"):
      print("\033[5;31m"+"Usted es Demasiado Menor para Viajar Solo")
    if(self.longer=="M"):
      print("\033[5;31m"+"Usted es Demasiado Mayor para Viajar Solo")
    print("\033[0;36m"+"Inserte los datos del Acompañante que viajara con Usted")
    n=str(input("   Nombre:"))
    n=validText(n)
    a=str(input("   Apellido:"))
    a=validText(a)
    acc=n+" "+a
    print("Acompañante",acc,"asignado Correctamente!")
    print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
    asd=input("")
    self.acc=acc
  def AñadirFondos(self,cantAñadir):
    self.cantAñadir=cantAñadir
    self.fondos=self.fondos+self.cantAñadir
    print("\033[0;36m"+"Fondos Añadidos Correctamente!")
    print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
    asd=input("")
  def VerUsuario(self):
    print("\033[0;36m"+"Datos del Usuario:")
    print("   Nombre del Usuario:",self.name,"",self.adress)
    if(self.edd==True):
      if(self.longer=="M" or self.longer=="m"):
        print("   Nombre del Acompañante:",self.acc)
    print("   Numero de Identificacion:",self.IDE)
    print("   Fondos en la Cuenta: $",self.fondos)
    print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
    asd=input("")
  def VerRutas(self):
    print("\033[0;36m"+"\n   Lista de Rutas\n")
    for i in range (len(Buses)):
      print("Ruta:",Buses[i] )
    print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
    asd=input("")
    print("\n   1) Consultar paradas de la ruta ")
    print("   2) Regresar")
    

    versa=input(":")
    versa=int(validReal(versa))
    if(versa<=0 or versa>=3):
      print("\033[5;31m"+"Valor Incorrecto, Ingresa una Opcion Valida")
      self.VerRutas()
    if versa==1:
      beat=str(input("\033[0;36m"+"\nIngrese la Ruta:"))
      sonic=rutas.get(beat,"No se encontro la Ruta")
      if beat in rutas:
        g=1  
        for i in range (len(sonic)):
          print(g,"",sonic[i] )
          g=g+1
      else:
        print("\033[5;31m"+"Ruta no encontrada")
        return 
    if versa==2:
      return
    return
  def VerEstaciones(self):
    var=list(p.keys())
    print("")
    for i in range(len(var)):
      print(var[i]) 
    return
    
      
  def Viaje(self):
    if(self.fondos<=2300):
      print("\033[5;31m"+"No tienes suficiente Dinero")
      print("Ve y Recarga tu tarjeta para poder Viajar")
      print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
      asd=input("")
      return
    print("   Ingrese la hora de viaje en formato 24H")


    hour=input(":")
    hour=int(validReal(hour))
    if hour<5 or hour>23:
      print("No hay servicios disponibles a esa hora, recuerde que el sistema solo funciona de 5:00 a 23:00")
      print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
      asd=input("")
      return 
    #Aca me falta colocar los condicionales
    star=str(input("Ingrese Estacion de partida:"))
    finish=str(input("Ingrese Estacion de llegada:"))

    if star==finish:
      print("No puede tener el mismo lugar de partida y llegada")
      return 
    else:
      norte=list(rutanorte.keys())
    if star not in norte:
      print("Error, Estacion de salida no encontrada!")
      return
    if finish not in norte:
      print("Error, Estacion de llegada no encontrada!") 
      return 
    a=norte.index(star)
    b=norte.index(finish)

    final={}  
      
    if a<b:
      final=rutanorte      
    if a>b:
      final=rutasur

    out=final.get(star)
    arrive=final.get(finish)
    print("") 
    u=0
    for i in range(len(out)):
      if out[i] in arrive and u>=1:
        print("Tambien En la estacion de",star,"hasta la estacion de",finish,"puede tomar la ruta:",out[i],"que es mas rapida"  ) 
      if out[i] in arrive and u==0:        
        print("En la estacion de",star,"hasta la estacion de",finish,"puede tomar la ruta:",out[i] )
        u=u+1 
    print("\033[0;36m"+"Viajando")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("\033[0;36m"+"Viaje Terminado, se han retirado $2.300 de tus fondos")
    self.fondos=self.fondos-2300
    print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
    asd=input("")
    return    

def CrearUsuario():
  print("\033[0;36m"+"\nInserta Tus Datos:")
  nombre=input("    Nombre:")
  nombre=validText(nombre)
  apellido=input("    Apellido:")
  apellido=validText(apellido)
  edad=input("    Edad:")
  edad=int(validReal(edad))
  idnt=input("    Identificacion:")
  idnt=validReal(idnt)
  user=Usuario(nombre,apellido,edad,0,idnt,False)
  print("\033[0;36m"+"\nUsuario Creado Correctamente!")
  print("\033[5;33m"+"\n     (Presiona Enter para Continuar)")
  asd=input("")
  return user
  

def main():
  print("\033[0;36m"+"Bienvenido al Sistema MyEasyTransmi!\n")
  print("Crea tu Usuario para Comenzar")
  user=CrearUsuario()
  while(True):
    print("\033[0;36m"+"Elige una Opcion para Continuar:\n")
    print("   1) Ver mi Usuario")
    print("   2) Añadir Dinero a mi Cuenta")
    print("   3) Consultar Rutas")
    print("   4) Consultar Estaciones")
    print("   5) Realizar Viaje ")
  
    opt=input(":")
    opt=int(validReal(opt))
    #Opcion Incorrecta
    if(opt<=0 or opt>=6):
      print("\033[5;31m"+"Valor Incorrecto, Ingresa una Opcion Valida")
    #Opcion 1 - Ver Usuario
    elif(opt==1):
      user.VerUsuario()
    #Opcion 2 - Ingresar Dinero
    elif(opt==2):
      dinero=input("\033[0;36m"+"¿Cuanto Dinero quieres Ingresar?")
      dinero=int(validReal(dinero))
      user.AñadirFondos(dinero)
    #Opcion 3 - Ver Rutas
    elif(opt==3):
      user.VerRutas()
    #Opcion 4 - Ver Estaciones
    elif(opt==4):
      user.VerEstaciones()
    #Opcion 5 - Viaje
    elif(opt==5):
      user.Viaje()

main()
