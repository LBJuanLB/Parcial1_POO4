#Clase cuenta que recibe titular y cantidad
class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
    
    #Metodo para imprimir los datos
    def imprimir(self):
        print("Titular:",self.titular)
        print("Cantidad:",self.cantidad)

#Clase CajaAhorro que hereda de la clase cuenta
class CajaAhorro(Cuenta):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
    
    def MostrarInformacion(self):
        super().imprimir()

#Clase PlazoFijo que hereda de la clase cuenta y tiene atributos propios, plazo e interes.
class PlazoFijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
    
    #Metodo para calcular el importe del interes
    def ImporteInteres(self):
        importe=self.cantidad*self.interes/100
        return importe
    
    #Metodo para mostrar informacion
    def Mostrar_Plazo(self):
        super().imprimir
        print("Plazo:",self.plazo)
        print("Interes:",self.interes)
        print("Interes total:",self.ImporteInteres())
    
print("Cuenta")
cuenta=Cuenta("Juan Espinosa",241000)
cuenta.imprimir()

print("Caja ahorro")
caja=CajaAhorro("Pablo",305949)
caja.imprimir()

print("Plazo fijo")
plazo=PlazoFijo("Juan Espinosa",241000,30,5)
plazo.Mostrar_Plazo()