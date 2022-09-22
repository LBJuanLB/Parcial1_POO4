#Se llama a la clase contacto para poder crear la agenda
from Contacto import Contacto

class Agenda:
    def __init__(self):
        self.Agenda=[]
    
    #Metodo para agregar un contacto
    def Agregar_contacto(self):
        print("[AGREGAR NUEVO CONTACTO]")
        telefono=input("Telefono:")
        #Llama al metodo "Esta_contacto" para verificar que no vaya a ingresar un numero repetido
        if self.Esta_contacto(telefono) == True:
            print("Ese numero de telefono ya ha sido agregado a la agenda")
            self.Buscar_telefono(telefono)
        else:
            nombre=input("Nombre:")
            email=input("Email:")
            contacto = Contacto(nombre,telefono,email)
            self.Agenda.append(contacto)
            print("El contacto ha sido agregado con exito!!")
    
    #Metodo para ver si un numero de telefono ya esta guardado en la agenda 
    def Esta_contacto(self,telefono):
        for Contacto in self.Agenda:
            if Contacto._telefono == telefono:
                return True
        return False
    
    #Metodo para mostrar la informacion de un contacto
    def Mostrar_contacto(self,contacto):
        for conctactos in self.Agenda:
            if conctactos == contacto:
                print("Nombre:",contacto._nombre)
                print("Telefono:",contacto._telefono)
                print("Email:",contacto._email)
                print()

    #Metodo que muestra todos los contactos de la agenda    
    def Listar_contactos(self):
        i = 1
        for Contactos in self.Agenda:
            print("[ CONTACTO",i,"]")
            self.Mostrar_contacto(Contactos)
            i=i+1

    #Metodo para buscar un contacto por el numero telefonico, y mostrar su informacion
    def Buscar_telefono(self,telefono):
        encontrado=0
        for contactos in self.Agenda:
            if contactos._telefono == telefono:
                encontrado=1
                self.Mostrar_contacto(contactos)
                break
        if encontrado == 0:
            print("No se encontró a ningun contacto con el numero:",telefono)

    #Metodo para buscar un contacto por el nombre, y mostrar su informacion
    def Buscar_nombre(self,nombre):
        encontrado=0
        for contactos in self.Agenda:
            if contactos._nombre == nombre:
                encontrado=encontrado+1
                self.Mostrar_contacto(contactos)
        if encontrado == 0:
            print("No se encontró a ningun contacto con el nombre de:",nombre)
        print("Se encontró un total de",encontrado,"contactos con ese nombre guardado")

    #Metodo que une los metodos "Buscar_telefono" y "Buscar_nombre" para preguntarle al usuario
    #por cual desea buscar al contacto
    def Buscar_contacto(self):
        op=1
        while(0<op and op<4):
            print("[ BUSCAR CONTACTO ]")
            print("1. Buscar por nombre")
            print("2. Buscar por telefono")
            print("3. Volver")
            op=int(input("Ingrese una opcion: "))
            print()
            if op == 1:
                nombre=input("Nombre del contacto a buscar: ")
                self.Buscar_nombre(nombre)
            elif op == 2:
                telefono=input("Telefono del contacto a buscar:")
                self.Buscar_telefono(telefono)
            elif op == 3:
                break
            print()
    
    #Metodo para editar un contacto ya ingresado
    def Editar_contacto(self):
        print("[ EDITAR CONTACTO ]")
        telefono=input("Ingrese el numero de telefono del contacto que quieres editar: ")
        #Verifica que el contacto este en la agenda
        if self.Esta_contacto(telefono)==True:
            for contacto in self.Agenda:
                if contacto._telefono==telefono:
                    op=1
                    #Muestra menu para saber que va a editar el usuario
                    while(0<op and op<6):
                        print("Numero a editar: ",telefono)
                        print("1. Mostrar informacion actual")
                        print("2. Editar nombre")
                        print("3. Editar numero")
                        print("4. Editar correo")
                        print("5. salir")
                        op=int(input("Ingrese una de las opciones: "))
                        
                        #Muestra la informacion del numero a editar
                        if op == 1:
                            self.Buscar_telefono(telefono)
                        #Edita el nombre del contacto
                        if op == 2:
                            nombre=input("Nuevo nombre:")
                            contacto._nombre=nombre
                            print("El nombre ha sido cambiado con exito!")
                        #Edita el numero telefonico
                        if op == 3:
                            Newtelefono=input("Nuevo numero telefonico:")
                            if self.Esta_contacto(Newtelefono)==True:
                                print("Ya existe un contacto con ese numero telefonico")
                            else:
                                contacto._telefono=Newtelefono
                                telefono=Newtelefono
                                print("El numero ha sido cambiado con exito!")
                        #Edita el email
                        if op == 4:
                            email=input("Nuevo email:")
                            contacto._email=email
                        #Sale editar el contacto
                        if op == 5:
                            print("Cambios guardados!")
                            break
        else:
            print("El contacto con el numero",telefono,"no está en la agenda")