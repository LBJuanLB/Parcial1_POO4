#Clase contacto con la informacion nombre, telefono y email
class Contacto:
    def __init__(self,nombre,telefono,email):
        self._nombre=nombre
        self._telefono=telefono
        self._email=email

    def __str__(self):
        return 'Nombre: {0}\nTelefono: {1}n\Domicilio: {2}\n'.format(self.nombre, self.telefono, self.domicilio)