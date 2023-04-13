#import functools
from timeit import default_timer
import threading

class Memoria:
    def __init__(self):
        self.PC = 0
        self.memoria = [0]

    def fetch(self):
        self.PC += 1
        print( f"PC: ", str(self.PC))

    def cargar(self, n):
        self.memoria.append(n)
        print(str(n) + " cargado correctamente ")

    def agregar(self,n,valor):
        value = self.memoria[n]
        self.memoria[n] = valor+value
    
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
    
    def round_robin(self, procesos, quantum):
        tiempo_total = 0
        procesos_restantes = len(procesos)
        cola_procesos = procesos.copy()
        while procesos_restantes > 0:
            for i in range(len(cola_procesos)):
                if cola_procesos[i]['tiempo'] > 0:
                    if cola_procesos[i]['tiempo'] > quantum:
                        tiempo_total += quantum
                        cola_procesos[i]['tiempo'] -= quantum
                    else:
                        tiempo_total += cola_procesos[i]['tiempo']
                        cola_procesos[i]['tiempo'] = 0
                        procesos_restantes -= 1
                else:
                    procesos_restantes -= 1
        return tiempo_total

procesos = [{'nombre': 'C1', 'tiempo': 8},
            {'nombre': 'C2', 'tiempo': 4},
            {'nombre': 'C3', 'tiempo': 9},
            {'nombre': 'C4', 'tiempo': 5},
            {'nombre': 'C5', 'tiempo': 2}]

def ejecutar():
    memoria = Memoria()
    print(memoria.round_robin(procesos, 5))


if __name__ == '__main__':
    ejecutar()


