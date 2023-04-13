#import functools
from timeit import default_timer
import threading


class Memoria:
    def __init__(self, menu):
        self.PC = 0
        self.memoria = [0]
        self.menu = menu

    def fetch(self):
        self.PC += 1
        print( f"PC: ", str(self.PC))

    def cargar(self, n):
        self.memoria.append(n)
        print(str(n) + " cargado correctamente ")

    def agregar(self,n,valor):
        value = self.memoria[n]
        self.memoria[n] = valor+value

    def total(self):
        cuentas = ""
        for i in range(0,len(self.memoria)):
            cuentas =cuentas + "El precio total a pagar por el cliente " + str(i) +" es: " + str(self.memoria[i]) + ". \n"
        return cuentas
    
    def resta(self, num1,  num2):
        resultado = int(num1) - int(num2)
        self.cargar(resultado)
        return(resultado)

    def suma(self, num1,  num2):
        resultado = int(num1) + int(num2)
        self.cargar(resultado)
        return(resultado)

    def multiplicacion(self, num1,  num2 , posicion):
        resultado = int(num1) * int(num2)
        if (resultado>10**100000):
            self.interruptions(OverflowError, "El resultado de la multiplicacion es un numero muy extenso")
            return
        if(len(self.memoria)>posicion):
            self.agregar(posicion,resultado)
        else:
            self.cargar(resultado)
        return(resultado)

    def division(self, num1,  num2):
        resultado = int(num1) / int(num2)
        self.cargar(resultado)
        return(resultado)

    def IR(self, op,num1,num2,posicion):
        if op == "0001":
            self.cargar(num1)

        elif op == "0010":
            self.resta(num1, num2)

        elif op == "0011":
            self.suma(num1, num2)

        elif op == "0100":
            self.multiplicacion(num1, num2,posicion)

        elif op == "0101":
            #try:
                if(num2==0):
                    self.interruptions(ZeroDivisionError, "Interrupcion de desbordamiento")
                    return
                else:
                    self.division(num1, num2)
            #except ZeroDivisionError as error: #Desbordamiento
            #    print(error)
        self.fetch()
    
    def interruptions(self,error, error_message):
        if error == ZeroDivisionError:
            print("ZeroDivisionError:",error_message)
        elif error== OverflowError:
            print("OverflowError:",error_message)
        elif error ==IndexError:
            print("IndexError:",error_message)
    
    def imprimirMenu(self):
            inicioTotal = int(default_timer())
            clientes = True
            mas_clientes = True
            num_clientes = 1
            dict_clientes = {}
            cliente_actual = 0
            
            def interactuar_con_usuario(cliente_actual):
                inicio = int(default_timer())
                fin = 0
                while fin < 30:
                    dict_clientes[cliente_actual] = "no"
                    medio = int(default_timer())
                    fin= medio-inicio
                    print("**************cliente " + str(cliente_actual) +"****************")
                    print("*******************menu*********************")
                    lista_productos=list(map(lambda x: x["producto"], productos))
                    for i in lista_productos:
                        print(i)
                    print("salir\n********************************************")
                    eleccion = input("Ingrese el nombre del producto a ordenar\n").lower().rstrip()
                    if eleccion=="salir": 
                        dict_clientes[cliente_actual] = "si"
                        break
                    item = list(filter(lambda x:  x["producto"]==eleccion,productos))
                    if(len(item)==0):
                        self.interruptions(IndexError, "El producto seleccionado no esta en el menu")
                    else:
                        price=dict(item[0])["precio"]
                        while(True):
                            try:
                                cantidad = int(input("Ingrese la cantidad que desea ordenar\n"))
                                if (type(5)) == (type(cantidad)):
                                    break
                            except ValueError as e:
                                print(e)
                        self.IR("0100", price, cantidad,cliente_actual)

            while clientes:
                # Creamos un hilo para la interacción del usuario
                hilo_usuario = threading.Thread(target=interactuar_con_usuario, args=(cliente_actual,))
                hilo_usuario.start()
                
                # Esperamos a que el hilo termine su ejecución
                hilo_usuario.join()

                if(mas_clientes):
                    respuesta = input("¿Hay mas clientes?\nSi\nNo\n")
                    if respuesta.lower()=="si":
                        num_clientes+=1
                        cliente_actual+=1
                    else:
                        mas_clientes=False
                        clientes = self.validarFinCiclo(dict_clientes, num_clientes)
                        cliente_actual = self.validarClienteActual(dict_clientes, num_clientes)
                else:
                    clientes = self.validarFinCiclo(dict_clientes, num_clientes)
                    cliente_actual = self.validarClienteActual(dict_clientes, num_clientes)

    def validarFinCiclo(self, dict_clientes, num_clientes):
        for i in range(0,num_clientes):
            if (dict_clientes[i]).lower()=="no":
                return True
        return False    

    def validarClienteActual(self, dict_clientes, num_clientes):        
        for i in range(0,num_clientes):
            if dict_clientes[i]=="no":
                return i
productos =[
    {
        "producto": "hamburguesa",
        "precio": 20000 
    },
    {
        "producto": "perro",
        "precio": 18000 
    },
    {
        "producto": "salchipapas",
        "precio": 14000 
    },
    {
        "producto": "pizza",
        "precio": 25000 
    },
    {
        "producto": "arepa rellena",
        "precio": 11000 
    },    
    {
        "producto": "perra",
        "precio": 19000 
    },
    {
        "producto": "taco",
        "precio": 5000 
    }
]

def ejecutar():
    memoria = Memoria(productos)
    memoria.imprimirMenu()
    print(memoria.total())


if __name__ == '__main__':
    ejecutar()