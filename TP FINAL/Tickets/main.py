import pickle, sys, os, random

def altaTicket(archivo):

        print("Ingrese los siguientes datos para generar el ticket: ")
        numero = random.randrange(1000, 9999) #con esto crean un numero random, pero deben asignarlo a una variable                
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese un asunto: ")
        problema = input("Describa el problema: ")

        tk = {
                "numero" : numero,
                "nombre" : nombre,
                "sector" : sector,
                "asunto" : asunto,
                "mensaje" : problema
        }     
        guardarTicket(archivo,tk)
        print("""
        ==============================================================
                        Se generó el siguiente ticket
        ==============================================================  
        """)
        imprimirTicket(tk)
        print("""
        ==============================================================
                Recuerde su número de ticket para futuras consultas
        ==============================================================              
        """)             


def guardarTicket(archivo, ticket):   
        archi = archivo + str(ticket["numero"]) + ".txt"
        with open(archi, "wb") as f:
                pickle.dump(ticket, f)

"""      
Con este comando van a generar y guardar el archivo
la palabra guardar es una variable que debe contener el nombre del archivo
la palabra ticket es una variable que contendra el diccionario (Objeto)
"""
def leerTicket(archivo):
        if (os.path.isfile(archivo)): # la palabra ruta obtendra el nombre del archivo y verificara que exista
                with open(archivo, "rb") as f:
                        tk = pickle.load(f)
                        print("""
        ==============================================================
                        Ticket consultado
        ==============================================================  
        """)
                        imprimirTicket(tk)
                        print("""
        ==============================================================                                          
        """)
        else:
                print("Número de ticket no encontrado.")

"""        
similar a lo anterior, la palabra abrir contendra el nombre del archivo a abrir 
la palabra ticket es el diccionario donde se guardara ese objeto        
"""


def imprimirTicket(ticket):
        print(f"""
        Su nombre: {ticket["nombre"]}                          N° Ticket:  {ticket["numero"]} 
        Sector: {ticket["sector"]} 
        Asunto: {ticket["asunto"]} 

        Mensaje: {ticket["mensaje"]} 
        """)
               
        

# sys.exit() #con este comando cierra la ejecucion del programa

#defino el nombre del archivo de tickets
nombreArchivo = "tickets"

os.system("cls") #para limpiar depende la terminal que usen en sus sistema puede variar clear se utiliza en linux y cls creo que en windows

seguir = True
mostrarMenu = True
while seguir:
        if (mostrarMenu):
                opcion = input("""
Bienvenido al sistema de Tickets de Tecno 3F - Python Inicial - 2024
Alumnos: Baglivo Matías & Pinasco Marina
                               
Seleccione una opción:
        1 - Generar un nuevo ticket
        2 - Leer un ticket
        3 - Salir
        """)        

        #validar que opción sea un número
        if (not opcion.isdigit()):   #pregunto si no es dígito
                print("Debe ingresar un valor numérico entre 1 y 3.") 
        elif (int(opcion) == 3):
                confirmacion = input("Confirme que desea salir del sistema. S/N : ")
                if (confirmacion.lower() == 's'):
                        seguir = False
                        os.system("cls") #para limpiar depende la terminal que usen en sus sistema puede variar clear se utiliza en linux y cls creo que en windows                     
        elif (int(opcion) == 1):
                altaTicket(nombreArchivo)
                rta= input("Desea generar un nuevo ticket?  (s/n)")
                if (rta.lower() == 's'):
                        mostrarMenu = False                        
                else:
                        mostrarMenu = True

        elif (int(opcion) == 2):           
                nro = input("Inserte el número de ticket a consultar: "); 
                archi = nombreArchivo + nro + ".txt"
                leerTicket(archi)
                rta= input("Desea leer otro ticket?  (s/n)")
                if (rta.lower() == 's'):
                        mostrarMenu = False                        
                else:
                        mostrarMenu = True
        else:
                print("La opción seleccionada no es válida. Debe ingresar un valor numérico entre 1 y 3.")
                
