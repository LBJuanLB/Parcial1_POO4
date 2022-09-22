#Clase alumno con atributos de nombre y nota del alumno
class Alumno:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota
    
    #Getters
    def get_nombre(self):
        return self._nombre
    def get_nota(self):
        return self._nota

    #Setters
    def set_nombre(self,nombre):
        self._nombre=nombre
    def set_nota(self,nota):
        #Verificar que la nota que se ingrese este entre 0 y 5
        if(nota>=0 and nota<=5):
            self._nota=nota
        else:
            x=0
            while(x==0):
                print("Nota invalida, el rango es de 0 a 5.")
                y= float(input("Intente otra vez: "))
                if (y>=0 and y<=5):
                    self._nota=y
                    x=1

    #Metodo aprobado que indica si el estudiante aprobó o no
    def aprobado(self,nota):
        if nota >= 3:
            print("El estudiante ha aprobado")
        else:
            print("El estudiante no ha aprobado")
    
    #Metodo para imprimir la informacion
    def imprimir(self):
        print("INFORMACION DEL ESTUDIANTE")
        print("Nombre:",self._nombre)
        print("Nota:",self._nota)
        self.aprobado(self._nota)
        print()

alumno1 = Alumno("Juan",2.4)
alumno1.imprimir()

alumno2 = Alumno("",-1)
alumno2.set_nombre("Jose")
alumno2.set_nota(-4)
alumno2.imprimir()