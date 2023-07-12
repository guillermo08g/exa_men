import numpy as np
ubicaciones=np.zeros((10,10), dtype=str)
asistentes= []
ganancias_totales=0 
def tipo_ubicaciones():
 for i in range(len(ubicaciones)):
  for j in range(len(ubicaciones[i])):
    if i*10+j+1<=20:
      ubicaciones[i][j]=f'PLATINUM'
    elif i*10+j+1<=50:
      ubicaciones[i][j]=f'GOLD'
    else:
      ubicaciones[i][j]=f'SILVER'
def comprar_entrada():
  if len(asistentes)>=100:
    print("Lo sentimos todas las entradas ya han sido vendidas")
    return
  cantidad_entradas=input("Ingrese la cantidad de entradas (1 o 3)")
  if cantidad_entradas not in ('1','2','3'):
    print("Cantidad de entradas invalida, Seleccione 1 o 3.")
    return
  cantidad_entradas = int(cantidad_entradas)
  print("----Escenario----")
  mostrar_escenario()
  for _ in range(cantidad_entradas):
    num_asiento=int(input(" Ingrese el numero del asiento: ")) 
    if num_asiento<1 or num_asiento>100:
      print("Porfavor ingrese un numero del 1 al 100")
      return
    fila=(num_asiento-1)//10
    columna=(num_asiento-1)%10
    ubicacion= ubicaciones[fila][columna]
    if ubicacion=='X':
      print("Este asiento no esta disponible,porfavor seleccione otro")
      return
      ubicaciones[fila][columna]='X'
    nombre=str(input("Ingrese su nombre: "))
    if nombre is not str:
      print("Porfavor ingrese un nombre. \nSu opción no ha sido guardada. ")
      ubicaciones[fila][columna]=0
      return
    run=input("Ingrese su run (sin puntos ni guión)")
    if run is not int:
      print("Porfavor ingrese un numero. \nSu opción no ha sido guardada. ")
      ubicaciones[fila][columna]=0
      return
    asistentes.append((nombre,run))
    precio=obtener_precio(ubicacion)
    if precio is not None:
       actualizar_ganancias_totales(precio)
  print("Entradas compradas exitosamente.")
def obtener_precio(tipo_ubicaciones):
  if tipo_ubicaciones=='Platinum':
    return 120000
  if tipo_ubicaciones=='Gold':
    return 80000
  if tipo_ubicaciones=='Silver':
    return 50000 
def actualizar_ganancias_totales(precio):
  global ganancias_totales
  ganancias_totales += precio
def mostrar_escenario():
  num_asiento=1
  for i in range(len(ubicaciones)):
    for j in range(len(ubicaciones[i])):
      if ubicaciones[i][j]=='X':
       print('X',end='  ')
      else:
        print(f"{num_asiento:2d}",end=' ')
        num_asiento+=1
    print()
def mostrar_asistentes():
  print("Lista de asistentes: ")
  for asistente in asistentes:
    nombre, run= asistente
    print(f"Nombre: {nombre},RUN: {run}")
def mostrar_ganancias_totales():
  print(f"Ganancias totales: {ganancias_totales}")
def iniciar():
  while True: 
    print("-----Bienvenido a Creativos.cl-----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print()
    opcion=input("Seleccione una opcion: ")
    if opcion=="1":
     comprar_entrada()
    elif opcion=="2":
     mostrar_escenario()
    elif opcion=="3":
     mostrar_asistentes()
    elif opcion=="4":
     mostrar_ganancias_totales()
    elif opcion=="5":
     print("Gracias por usar nuestro sistema")
     break
    else:
      print("Opcion invalida. Por favor seleccione una opción válida")
tipo_ubicaciones()
iniciar()
