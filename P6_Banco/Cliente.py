#Clase cliente con los atributos id, nombre y cantidad
class Cliente:
    def __init__(self,id,nombre,cantidad):
        self.id=id
        self.nombre=nombre
        self.cantidad=float(cantidad)

    #Metodo depositar
    def depositar(self,cantidad):
        #Verifica que el dinero a depositar sea mayor a 0
        if cantidad > 0:
            self.cantidad=self.cantidad+cantidad
            print("Se ha depositado con exito: $",cantidad)
        else:
            print("No se pudo depositar, ingreso un valor incorrecto.")
    #Metodo para extraer
    def extraer(self,cantidad):
        #Balance indica el la cantidad de dinero que queda en la cuenta luego de retirar
        balance= self.cantidad-cantidad
        #Si el balance es mayor o igual a 0, se puede realizar la operacion
        if balance>=0:
            print("Se ha retirado con exito: $",cantidad)
            self.cantidad=balance
        else:
            print("No tiene el suficiente saldo para retirar $",cantidad)
    #Metodo para mostrar el total de dinero del cliente
    def mostrar_total(self):
        print()
        print("Total: $",self.cantidad)
        print()