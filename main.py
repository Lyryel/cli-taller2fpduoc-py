"""Haga un programa que permita generar un menú de gestión de matrículas para la
Biblioteca Pública.
TOTEM AUTOSERVICIO BIBLIOTECA PÚBLICA
1.- Matricular.
2.- Cancelar Matrícula.
3.- Cupos disponibles.
4.- Salir.

Todas las opciones del menú deben estar implementadas mediante funciones
separadas del código principal (main).

-  Al ingresar a la opción 1.- Matricular, se debe permitir ingresar código, nombre
    del usuario, tipo de inscripción y código de verificación por separado. Para que
    la matrícula sea exitosa se debe cumplir lo siguiente:
  - el código del usuario no debe estar repetido y debe tener un largo de 6 caracteres,
  - el nombre debe contener sólo letras.
  - el tipo de inscripción solo permite “N” (Niños) o “A” (Adultos),
  - el código de verificación debe tener un largo mínimo de 4 caracteres,
    incluir al menos 1 letra mayúscula, al menos 1 número y no puede
    contener espacios.

- Al ingresar a la opción 2.- Cancelar Matrícula, se debe permitir ingresar el
    código del usuario al que se le cancelará la matrícula. Se buscará el usuario, si
    existe, será eliminado de la colección y restaurado el stock. En caso de no
    existir dar un mensaje adecuado.

- Al ingresar la opción 3.- Cupos disponibles, el menú debe mostrar la cantidad
    de cupos restantes para cada una de las categorías. Para esto, se dispondrá de
    un cupo inicial de 25 participantes para Niños y 25 para Adultos.

- Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
    Programa finalizado...

    *En caso de ingresar una opción inexistente, dar el respectivo mensaje de error."""

usuarios = []
cupos_niños = 25
cupos_adultos = 25


def main():
    while True:
        print ("""Biblioteca Pública.
TOTEM AUTOSERVICIO BIBLIOTECA PÚBLICA
1.- Matricular.
2.- Cancelar Matrícula.
3.- Cupos disponibles.
4.- Salir.""")
        opcion = input("ingrese opcion: ")
        print(opcion)
        if opcion == "1":  
            matricular()
        if opcion == "2":
            cancelar_matricula()
        if opcion == "3":
            cupos_disponibles()
        if opcion == "4":
            salir()        

def matricular():
    global cupos_niños, cupos_adultos

    codigo = input("ingresar codigo: ")
    nombre_de_usuario = input("ingresar nombre de usuario: ")
    tipo_de_inscripcion = input("ingrese el tipo de inscripción N o A: ") #  - el tipo de inscripción solo permite “N” (Niños) o “A” (Adultos)#
    codigo_de_verificacion = input("ingrese un codigo de verificacion: ")
    usuario = {
        "codigo": codigo, 
        "nombre": nombre_de_usuario,
        "tipo_de_inscripcion": tipo_de_inscripcion,
        "codigo_de_verificacion": codigo_de_verificacion
    }
    usuarios.append(usuario)
    if tipo_de_inscripcion == "N":
        cupos_niños -= 1 

    if tipo_de_inscripcion == "A": 
        cupos_adultos -= 1

def cancelar_matricula():
    global cupos_niños, cupos_adultos

    codigo = input("ingresar codigo a eliminar: ")
    for usuario in usuarios: 
        if usuario["codigo"] == codigo:
            usuarios.remove(usuario)

            if usuario["tipo_de_inscripcion"] == "N":
                cupos_niños += 1 

            if usuario["tipo_de_inscripcion"] == "A": 
                cupos_adultos += 1          

def cupos_disponibles():
    print(f"cupos disponibles niños: {cupos_niños}")
    print(f"cupos disponibles adultos: {cupos_adultos}")

def salir():
    exit(0)

main() 


