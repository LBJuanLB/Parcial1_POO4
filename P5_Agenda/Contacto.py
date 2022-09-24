#Clase contacto con la informacion nombre, telefono y email
class Contacto:
    def __init__(self,nombre,telefono,email):
        """Inicializador de la clase Contacto
        Args:
            self._nombre (str): Nombre del contacto
            self._telefono (str): Numero telefonico del contacto
            self._email (str): Email del contacto
        """
        self._nombre=nombre
        self._telefono=telefono
        self._email=email
    
    #Mostrar la informacion del contacto
    def __str__(self):
        return 'Nombre: {0}\nTelefono: {1}n\Domicilio: {2}\n'.format(self.nombre, self.telefono, self.domicilio)
