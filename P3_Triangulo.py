'''
Clase triangulo que recibe el tamaño de sus tres lados y nos dice 
si es equilátero, isóceles o escaleno.
'''
class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        """Inicializador de la clase Triangulo
        Args:
            self.lado1 (float): Lado 1 del triangulo
            self.lado2 (float): Lado 2 del triangulo
            self.lado3 (float): Lado 3 del triangulo
        """
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    
    #Getters 
    def get_lado1(self):
        return self.lado1
    def get_lado2(self):
        return self.lado2
    def get_lado3(self):
        return self.lado3

    #Setters
    def set_lado1(self,l1):
        if l1>0:
            self.lado1=l1
        else:
            l1=self.ingrese_lado()
            self.lado1=l1
    def set_lado2(self,l2):
        if l2>0:
            self.lado2=l2
        else:
            l2=self.ingrese_lado()
            self.lado2=l2
    def set_lado3(self,l3):
        if l3>0:
            self.lado3=l3
        else:
            l3=self.ingrese_lado()
            self.lado3=l3

    #Metodo para verificar que se ingrese un lado de tamaño valido
    def ingrese_lado(self):
        x=0
        while(x==0):
            print("El tamaño del lado no puede ser menor que 0")
            lado=float(input("Ingrese el tamaño del lado:"))
            if lado>0:
                x=1
                return lado
    
    #Metodo que retorna el lado con mayor tamaño
    def lado_mayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            return self.lado1
        elif self.lado2 >= self.lado3:
            return self.lado2
        else:
            return self.lado3
    
    #Metodo que retorna el tipo de triangulo
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return("El triangulo es equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return("El triangulo es isósceles")
        else:
            return("El triangulo es escaleno")
    
    #Se encarga de mostrar la informacion
    def __repr__(self):
        return f'Los lados del triangulo son: {self.lado1,self.lado2,self.lado3}, {self.tipo_triangulo()} y el lado con mayor longitud es {self.lado_mayor()}\n'

triangulo1 = Triangulo(8.5,8,8)
print(triangulo1)

triangulo1.set_lado1(3)
print(triangulo1)

triangulo1.set_lado2(3)
triangulo1.set_lado3(-3)
print(triangulo1)
