from tkinter import *
from tkinter import messagebox as mb
from tkinter.font import Font
import mysql.connector

boot = Tk()
boot.geometry("150x100")
boot.title("Restaurarnte")
font = Font(family="Roboto Cn", size=10,slant="italic")
fonot = Font(family="Roboto Cn", size=10,weight="bold")

ensalada = StringVar()
hamburguesa = StringVar()
churrasco = StringVar()

coca = StringVar()
cuatro = StringVar()
pepsi = StringVar()

primeB = StringVar()
SegundoC = StringVar()
TercerTo = StringVar()

id_bebidas = {"Coca-cola":1,"Cuatro":2,"Pepsi":3}
id_comidas = {"Ensalada":1,"Hamburguesa":2,"Churrasco":3}

connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

def conectarBBdd():
    try:

        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS resta DEFAULT CHARACTER SET 'utf8mb4';")

        cursor.execute("USE resta;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bebida(
                ID_B INT AUTO_INCREMENT PRIMARY KEY,
                nombre_b VARCHAR(40),
                precio_b DOUBLE(10,2)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comida(
                ID_C INTEGER AUTO_INCREMENT PRIMARY KEY,
                nombre_c VARCHAR(50),
                presio_c DOUBLE(10,2)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu(
                ID_m INTEGER AUTO_INCREMENT PRIMARY KEY,
                ID_C INTEGER,
                ID_B INTEGER,
                Cantidad_C INTEGER,
                Cantidad_B INTEGER,
                Foreign Key (ID_C) REFERENCES comida(ID_C),
                Foreign Key (ID_B) REFERENCES bebida(ID_B)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orden(
                ID_O INTEGER AUTO_INCREMENT PRIMARY KEY,
                ID_m INTEGER,
                TotalOrden DOUBLE(10,2),
                Foreign Key (ID_m) REFERENCES menu(ID_m)
            );
        """)

        cursor.execute("INSERT INTO comida(nombre_c,presio_c) VALUES('Ensalada',10.000) ON DUPLICATE KEY UPDATE ID_C=ID_C;")
        cursor.execute("INSERT INTO comida(nombre_c,presio_c) VALUES('Hamburguesa',30.000) ON DUPLICATE KEY UPDATE ID_C=ID_C;")
        cursor.execute("INSERT INTO comida(nombre_c,presio_c) VALUES('Churrasco',20.000) ON DUPLICATE KEY UPDATE ID_C=ID_C;")

        cursor.execute("INSERT INTO bebida(nombre_b,precio_b) VALUES('Coca-cola',3.000) ON DUPLICATE KEY UPDATE ID_B=ID_B;")
        cursor.execute("INSERT INTO bebida(nombre_b,precio_b) VALUES('Cuatro',2.000) ON DUPLICATE KEY UPDATE ID_B=ID_B;")
        cursor.execute("INSERT INTO bebida(nombre_b,precio_b) VALUES('Pepsi',2.000) ON DUPLICATE KEY UPDATE ID_B=ID_B;")

        connection.commit()
        print("Base de datos y tablas creadas exitosamente.")

    except mysql.connector.Error as error:
        print("Error al conectar o crear la base de datos:", error)


def obtener_id_bebida():

    global id_bebida
    global cantidad_bebida

    id_bebida = 0
    cantidad_bebida = 0

    selec_bebida = obtener_bebida()
    if selec_bebida == "Coca-cola":
        id_bebida = 1
    elif selec_bebida == "Cuatro":
        id_bebida = 2
    elif selec_bebida == "Pepsi":
        id_bebida = 3
    
    cantidad_bebida = obtenerCbebida(selec_bebida)

    print("Ejo es",id_bebida,"Ejopno es: ",cantidad_bebida)

    return id_bebida, cantidad_bebida

def obtener_id_comida():

    global id_comida
    global cantidad_comida

    id_comida = 0
    cantidad_comida = 0

    selec_comida = obtener_comida()
    if selec_comida == "Ensalada":
        id_comida = 1
    elif selec_comida == "Hamburguesa":
        id_comida = 2
    elif selec_comida == "Churrasco":
        id_comida = 3
    
    cantidad_comida = obtenerCcomida(selec_comida)

    print("Ejo es",id_comida,"Cantidad es: ",cantidad_comida)

    return id_comida, cantidad_comida

def obtener_comida():
    if ensalada.get():
        return "Ensalada"
    elif hamburguesa.get():
        return "Hamburguesa"
    elif churrasco.get():
        return "Churrasco"
    else:
        return 0

def obtenerCcomida(selec_comida):
    if selec_comida == "Ensalada":
        valor_ensa= ensalada.get()
        return float(valor_ensa) if valor_ensa else 0.0 
    elif selec_comida == "Hamburguesa":
        valor_hambu = hamburguesa.get()
        return float(valor_hambu) if valor_hambu else 0.0 
    elif selec_comida == "Churrasco":
        valor_chus = churrasco.get()
        return float(valor_chus) if valor_chus else 0.0  
    else:
        return 0 if selec_comida else 0.0

def obtener_bebida():
    if coca.get():
        return "Coca-cola"
    elif cuatro.get():
        return "Cuatro"
    elif pepsi.get():
        return "Pepsi"
    else:
        return 0

def obtenerCbebida(selec_bebida):
    if selec_bebida == "Coca-cola":
        valor_coca = coca.get()
        return float(valor_coca) if valor_coca else 0.0 
    elif selec_bebida == "Cuatro":
        valor_cuatro = cuatro.get()
        return float(valor_cuatro) if valor_cuatro else 0.0 
    elif selec_bebida == "Pepsi":
        valor_pepsi = pepsi.get()
        return float(valor_pepsi) if valor_pepsi else 0.0  
    else:
        return 0 if selec_bebida else 0.0
    
def comida():

    una = Toplevel(boot)
    una.title("Comidas")
    una.iconbitmap('PNG/rest.ico')


    global ventana
    ventana = Frame(una)
    ventana.pack()

    #Ensalada

    bed = PhotoImage(file="PNG/ensalada.png")
    unoB = Label(ventana, image=bed)
    unoB.grid(row=0, column=0)

    ensa = Label(ventana,text="Ensalada: $10.000", font=font)
    ensa.grid(row=1,column=0)

    cantiEnsa = Entry(ventana,textvariable=ensalada)
    cantiEnsa.grid(row=0,column=1)

    #Hamburguesa

    bed2 = PhotoImage(file="PNG/hamburguesa.png")
    unoB2 = Label(ventana, image=bed2)
    unoB2.grid(row=2, column=0)

    ensa2 = Label(ventana,text="Hamburguesa: $30.000",font=font)
    ensa2.grid(row=3,column=0)

    cantiEnsa2 = Entry(ventana,textvariable=hamburguesa)
    cantiEnsa2.grid(row=2,column=1)

    #Churrasco

    bed3 = PhotoImage(file="PNG/churrasco.png")
    unoB3 = Label(ventana, image=bed3)
    unoB3.grid(row=4, column=0)

    ensa3 = Label(ventana,text="Churrasco: $20.000",font=font)
    ensa3.grid(row=5,column=0)

    cantiEnsa3 = Entry(ventana,textvariable=churrasco)
    cantiEnsa3.grid(row=4,column=1)

    besbi = Button(una,text="Bebidas",font=fonot,command=lambda: [ensalada.set(cantiEnsa.get()), hamburguesa.set(cantiEnsa2.get()), churrasco.set(cantiEnsa3.get()), bebdia(),obtener_id_comida()])
    besbi.pack()

    mainloop()

def bebdia():

    dos = Toplevel(boot)
    dos.title("Bebidas")
    dos.iconbitmap('PNG/bed.ico')

    global ventana2
    ventana2 = Frame(dos)
    ventana2.pack()

#Cocacola

    bed5 = PhotoImage(file="PNG/Coca.png")
    unoB5 = Label(ventana2, image=bed5)
    unoB5.grid(row=0, column=0)

    ensa5 = Label(ventana2,text="Coca-cola: $3.000",font=font)
    ensa5.grid(row=1,column=0)

    global cantiEnsa5
    cantiEnsa5 = Entry(ventana2,textvariable="coca")
    cantiEnsa5.grid(row=0,column=1)

    #Cuatro

    bed7 = PhotoImage(file="PNG/cuatro.png")
    unoB7 = Label(ventana2, image=bed7)
    unoB7.grid(row=2, column=0)

    ensa7 = Label(ventana2,text="Cuatro: $2.000",font=font)
    ensa7.grid(row=3,column=0)

    global cantiEnsa7
    cantiEnsa7 = Entry(ventana2,textvariable="cuatro")
    cantiEnsa7.grid(row=2,column=1)

    #Pepsi

    bed6 = PhotoImage(file="PNG/pepsi.png")
    unoB6 = Label(ventana2, image=bed6)
    unoB6.grid(row=4, column=0)

    ensa6 = Label(ventana2,text="Pepsi: $2.000",font=font)
    ensa6.grid(row=5,column=0)

    global cantiEnsa6
    cantiEnsa6 = Entry(ventana2,textvariable="pepsi")
    cantiEnsa6.grid(row=4,column=1)

    envia = Button(dos,text="Enviar pedido",font=fonot,command=lambda: [coca.set(cantiEnsa5.get()), cuatro.set(cantiEnsa7.get()), pepsi.set(cantiEnsa6.get()), obtener_id_bebida(),cargar_pedido(),ventana.destroy(),ventana2.destroy()])
    envia.pack()

    mainloop()

def MosPedido():
    tres = Toplevel(boot)
    tres.title("Pedidos")
    tres.iconbitmap('PNG/chec.ico')

    ventana3 = Frame(tres,width=1000,height=500)
    ventana3.pack()

    Textoxd = Label(ventana3,text="Ingrese el numero de su pedido ",font=font)
    Textoxd.grid(row=0,column=0,sticky="e",padx=10,pady=10)

    global generarPedido
    generarPedido = Entry(ventana3)
    generarPedido.grid(row=1,column=0,sticky="e",padx=10,pady=10)

    ButtP = Button(ventana3,text="Generar Orden",command=leer)
    ButtP.grid(row=2,column=0,sticky="e",padx=10,pady=10)

    global primeB
    global SegundoC
    global TercerTo


    beb = Label(ventana3,text="Bebida: ")
    beb.grid(row=3,column=0,sticky="e",padx=10,pady=10)
    primeB = Label(ventana3)
    primeB.grid(row=3,column=1,sticky="e",padx=10,pady=10)

    comi = Label(ventana3,text="Comida: ")
    comi.grid(row=4,column=0,sticky="e",padx=10,pady=10)
    SegundoC = Label(ventana3)
    SegundoC.grid(row=4,column=1,sticky="e",padx=10,pady=10)

    tota = Label(ventana3,text="Total a Pagar: ")
    tota.grid(row=5,column=0,sticky="e",padx=10,pady=10)
    TercerTo = Label(ventana3)
    TercerTo.grid(row=5,column=1,sticky="e",padx=10,pady=10)


    mainloop()

def insertar_pedido(id_comida, id_bebida, cantidad_comida, cantidad_bebida):
    try:
        cursor = connection.cursor()

        sql = "INSERT INTO menu(ID_C, ID_B, Cantidad_C, Cantidad_B) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_comida, id_bebida, cantidad_comida, cantidad_bebida))

        id_menu = cursor.lastrowid

        total_pedido = (cantidad_comida * obtener_precio_comida(id_comida)) + (cantidad_bebida * obtener_precio_bebida(id_bebida))

        sql = "INSERT INTO orden(ID_m, TotalOrden) VALUES (%s, %s)"
        cursor.execute(sql, (id_menu, total_pedido))

        mb.showinfo("Orden numero",cursor.lastrowid)

        connection.commit()
        print("Pedido insertado correctamente en la base de datos.")

    except mysql.connector.Error as error:
        print("Error al insertar el pedido en la base de datos:", error)

def obtener_precio_comida(id_comida):
    cursor = connection.cursor()
    sql = "SELECT presio_c FROM comida WHERE ID_C = %s"
    cursor.execute(sql, (id_comida,))
    precio = cursor.fetchone()[0]
    return precio

def obtener_precio_bebida(id_bebida):
    cursor = connection.cursor()
    sql = "SELECT precio_b FROM bebida WHERE ID_B = %s"
    cursor.execute(sql, (id_bebida,))
    precio = cursor.fetchone()[0]
    return precio

def cargar_pedido():
    id_comida, cantidad_comida = obtener_id_comida()
    id_bebida, cantidad_bebida = obtener_id_bebida()

    insertar_pedido(id_comida, id_bebida, cantidad_comida, cantidad_bebida)
    mb.showinfo("BBDD","Datos insertados")

def leer():
  leerpedi = connection.cursor()
  leerpedi.execute("SELECT bebida.nombre_b, comida.nombre_c, orden.TotalOrden FROM orden INNER JOIN menu on menu.ID_m = orden.ID_m INNER JOIN bebida on bebida.ID_B = menu.ID_B INNER JOIN comida on comida.ID_C = menu.ID_C WHERE orden.ID_O = " + generarPedido.get())
  pedido = leerpedi.fetchall()

  # Update the text of the labels using their widget instances
  for todo in pedido:
    primeB.config(text=todo[0])  # Set the text of the primeB label
    SegundoC.config(text=todo[1])  # Set the text of the SegundoC label
    TercerTo.config(text=todo[2])  # Set the text of the TercerTo label

  connection.commit()
     
menu = Frame(boot)
menu.pack()


menus = Button(menu,text="Abrir Menu",font=fonot,command=comida)
menus.pack(ipadx=23,pady=3,)

pedido = Button(menu,text="Mirar Pedido",font=fonot,command=MosPedido)
pedido.pack(ipadx=19,pady=3)

conectBBDD = Button(menu,text="Conectar BBDD",font=fonot,command=conectarBBdd)
conectBBDD.pack(ipadx=12.5, pady=3)


mainloop()


