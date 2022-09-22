#Clase calculadora que realiza suma, resta, multiplicacion y division a dos numeros
class Calculadora:
    def __init__(self):
        self.num1=float(input("Ingrese el primer numero: "))
        self.num2=float(input("Ingrese el segundo numero: "))
    
    #Metodos de las operaciones suma, resta, multiplicacion y division
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2
    
    #Metodo para imprimir los resultados
    def resultados(self):
        print("\t[CALCULADORA]")
        print("Suma: ",self.num1,"+",self.num2,"=",self.suma())
        print("Resta: ",self.num1,"-",self.num2,"=",self.resta())
        print("Multiplicacion: ",self.num1,"*",self.num2,"=",self.multiplicacion())
        print("Division: ",self.num1,"/",self.num2,"=",self.division())

operacion= Calculadora()
operacion.resultados()