from Agenda import Agenda
#Menu de la agenda
if __name__=='__main__':
    agenda = Agenda()

    op=1

    while (0<op and op<6):
        print("[--------AGENDA--------]")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Salir")

        op=int(input("Ingrese una opcion:"))
        print()
        if op == 1:
            agenda.Agregar_contacto()
        elif op == 2:
            agenda.Listar_contactos()
        elif op == 3:
            agenda.Buscar_contacto()
        elif op == 4:
            agenda.Editar_contacto()
        elif op == 5:
            print("Ha salido de la agenda... Que tenga un buen dia!")
            break
        print()