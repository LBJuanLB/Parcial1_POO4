#Importamos la clase cliente
from Cliente import Cliente

class Banco:
    def __init__(self):
        self.Clientes=[]
    
    #Metodo para ingresar un nuevo cliente
    def nuevo_cliente(self):
        id=input("ID:")
        #Comprueba que la id del cliente no este repetida
        if self.comprobar_cliente(id)==True:
            print("Ya existe un cliente con esa ID")
        else:
            nombre=input("Nombre:")
            cantidad=float(input("Cantidad:"))
            cliente=Cliente(id,nombre,cantidad)
            self.Clientes.append(cliente)
    
    #Metodo para verificar si el cliente ya esta o no
    def comprobar_cliente(self,id):
        for clientes in self.Clientes:
            if clientes.id == id:
                return True
        return False

    #Metodo para acceder a los metodos del cliente
    def operar(self):
        print("[ OPERACIONES ]")
        id=input("Ingrese el id del cliente:")
        for clientes in self.Clientes:
            if clientes.id == id:
                op=1
                while (0<op and op<5):
                    print("[ OPERACIONES ]")
                    print("Hola",clientes.nombre,", que operacion desea realizar:")
                    print("1. Consultar saldo")
                    print("2. Depositar")
                    print("3. Retirar")
                    print("4. Volver")
                    op=int(input("Ingrese una opcion:"))
                    if op == 1:
                        Cliente.mostrar_total(clientes)
                    elif op == 2:
                        cantidad=float(input("Ingrese la cantidad a depositar:"))
                        Cliente.depositar(clientes,cantidad)
                    elif op == 3:
                        cantidad=float(input("Ingrese la cantidad a retirar:"))
                        Cliente.extraer(clientes,cantidad)
                    elif op == 4:
                        break
    
    #Metodo para consultar el deposito total que hay en el banco
    def deposito_total(self):
        Total=0
        for clientes in self.Clientes:
            Total=Total+clientes.cantidad
        print("El dinero total que hay en el banco es de: ",Total)

#Menu del banco
if __name__=='__main__':
    banco = Banco()

    op=1

    while (0<op and op<5):
        print("[--------BANCO--------]")
        print("1. Añadir cliente")
        print("2. Operaciones")
        print("3. Deposito total")
        print("4. Salir")

        op=int(input("Ingrese una opcion:"))
        print()
        if op == 1:
            banco.nuevo_cliente()
        elif op == 2:
            banco.operar()
        elif op == 3:
            banco.deposito_total()
        elif op == 4:
            break
        print()