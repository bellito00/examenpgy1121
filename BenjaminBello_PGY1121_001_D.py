from os import system
system("cls")
import time

Entradas=["1","2","3","4","5","6","7","8","9","10",
          "11","12","13","14","15","16","17","18","19","20",
          "21","22","23","24","25","26","27","28","29","30",
          "31","32","33","34","35","36","37","38","39","40",
          "41","42","43","44","45","46","47","48","49","50",
          "51","52","53","54","55","56","57","58","59","60",
          "61","62","63","64","65","66","67","68","69","70",
          "71","72","73","74","75","76","77","78","79","80",
          "81","82","83","84","85","86","87","88","89","90",
          "91","92","93","94","95","96","97","98","99","100"]
Registro=[]
Total=[]
ValorPlat=[]
ValorGold=[]
ValorSilver=[]
Platinum=[]
Gold=[]
Silver=[]
Cantidad=[]

def comprar():
    mostrar_ubicaciones()
    entrada=input("""
    Selecciona mediante el numero, la ubicacion que deseas comprar:
    (Si aparece una x significa que ese asiento ya esta comprado)

    Platinum: 120.000 (Asientos del 1 al 20)
    Gold: 80.000 (Asientos del 21 al 50)
    Silver: 50.000 (Asientos 51 al 100)

    """)
    if entrada in Entradas:
        print("Comprando asiento")
        id_entrada=int(entrada)
        Entradas[id_entrada-1]="X"
        if id_entrada>0 and id_entrada<21:
            tipo="Platinum"
            valor=120000
        elif id_entrada>20 and id_entrada<51:
            tipo="Gold"
            valor=80000
        elif id_entrada>50 and id_entrada<101:
            tipo="Silver"
            valor=50000
        while True:
            rut=input("Ingresa tu rut: (formato: 21038810)")
            if len(rut)==8 and rut.isnumeric():
                print(f"Rut ingresado correctamente: {rut}")
                break
            else:
                print("Ingresa correctamente el rut como se dice en el formato")
        datos=rut,id_entrada,tipo
        Total.append(valor)
        Registro.append(datos)
        Cantidad.append(1)
        if tipo=="Platinum":
            Platinum.append(1)
            ValorPlat.append(valor)
        elif tipo=="Gold":
            Gold.append(1)
            ValorGold.append(valor)
        elif tipo=="Silver":
            Silver.append(1)
            ValorSilver.append(valor)
        print(f"Asiento {id_entrada} del tipo {tipo} asignado correctamente al rut {rut}")
    else:
        print("No existe ninguno de los asientos que acabas de colocar o este no se encuentra disponible")


def mostrar_ubicaciones():
    print("Escenario")
    contador=0
    for i in Entradas:
        contador=contador+1
        print(i, end=" ")
        if contador==10:
            print("\n")
            contador=0

def asistentes():
    if Registro!=[]:
        Registro.sort()
        for i in Registro:
            print("")
            print(f"Asiento: {i[1]} ")
            print(f"Tipo de entrada: {i[2]} ")
            print(f"Rut asignado: {i[0]}")
            print("")
    else:
        print("Nadie a comprado ningun asiento todavia")

def ganancias():
    cantplatinum=sum(Platinum)
    cantgold=sum(Gold)
    cantsilver=sum(Silver)
    plataplat=sum(ValorPlat)
    platagold=sum(ValorGold)
    platasilver=sum(ValorSilver)
    cantidadtotal=sum(Cantidad)
    recaudacion=sum(Total)
    print(f"""
    Tipo Entrada: Platinum - Cantidad: {cantplatinum} - Total: {plataplat}
    Tipo Entrada: Gold - Cantidad: {cantgold} - Total: {platagold}
    Tipo Entrada: Silver - Cantidad: {cantsilver} - Total: {platasilver}
    Total de entradas vendidas: {cantidadtotal}
    Total de recaudacion: {recaudacion}
    """)

while True:
    opcion=input("""
    Bienvenido al sistema de compra de entradas de "Michael Jam"

    1.Comprar entradas
    2.Mostrar ubicaciones disponibles
    3.Ver listado de asistentes
    4.Mostar ganancias totales
    5.Salir


    """)
    match opcion:
        case "1":
            comprar()
        case "2":
            mostrar_ubicaciones()
        case "3":
            asistentes()
        case "4":
            ganancias()
        case "5":
            hora=time.asctime()
            print(f"""
            Finalizando programa...
            Benjamin Bello
            {hora}
            """)
            break
        case other:
            print("Opcion no valida")
