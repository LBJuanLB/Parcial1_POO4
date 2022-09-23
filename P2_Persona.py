#Clase persona con atributos de nombre y edad
class Persona:
    def __init__(self,nombre,edad):
    """Inicializador de la clase Persona
        Args:
            self._nombre (str): Nombre de la persona
            self._edad (int): Edad de la persona
        """
        self._nombre=nombre
        self._edad=edad

    #Getters    
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    
    #Setters
    def set_nombre(self,nombre):
        self._nombre=nombre
    def set_edad(self,edad):
        #Verificar que se ingrese una edad valida
        if edad>=0:
            self._edad=edad
        else:
            x=0
            while x==0:
                print("Edad invalida, tiene que ser mayor a 0")
                edad=int(input("Intente otra vez:"))
                if(edad>=0):
                    x=1
                    self._edad=edad

    #Metodo para indicar si la persona es mayor de edad o no
    def mayor_edad(self,edad):
        if(edad>=18):
            return("SI es mayor de edad")
        else:
            return("NO es mayor de edad")
    
    #Mostramos los datos
    def __repr__(self):
        return f'La persona {self._nombre} tiene {self._edad} años y {self.mayor_edad(self._edad)}\n'

persona1=Persona("Juan Espinosa",18)
print("Nombre: ",persona1.get_nombre())
print("Edad:",persona1.get_edad())
print(persona1)

persona1.set_edad(-45)
print(persona1)
