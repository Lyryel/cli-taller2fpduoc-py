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
        try: 
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
        except Exception as e: 
            print(f"Hubo un error inesperado {e}")

def matricular():
    global cupos_niños, cupos_adultos

    print("""Para que la matrícula sea exitosa se debe cumplir lo siguiente:
  - el código del usuario no debe estar repetido y debe tener un largo de 6 caracteres,
  - el nombre debe contener sólo letras.
  - el tipo de inscripción solo permite “N” (Niños) o “A” (Adultos),
  - el código de verificación debe tener un largo mínimo de 4 caracteres, incluir al menos 1 letra mayúscula, al menos 1 número y no puede contener espacios.""")

    codigo = input("ingresar codigo: ")
    # Validaciones 
    for usuario in usuarios:
        if codigo == usuario["codigo"]:
            print("el código del usuario no debe estar repetido")
            return
    if len(codigo) != 6:
        print("El codigo debe tener un largo de 6 caracteres")  
        return
    
    nombre_de_usuario = input("ingresar nombre de usuario: ")
    if not nombre_de_usuario.isalpha():
        print("El nombre debe contener sólo letras.")
        return

    tipo_de_inscripcion = input("ingrese el tipo de inscripción N o A: ") #  - el tipo de inscripción solo permite “N” (Niños) o “A” (Adultos)#
    if tipo_de_inscripcion.upper() not in ["N","A"]: 
        print("El tipo de inscripción es sólo N o A")
        return
    
    # Validaciones codigo de verificacion
    """- el código de verificación debe tener un 
    largo mínimo de 4 caracteres,
    incluir al menos 1 letra mayúscula, 
    al menos 1 número y 
    no puede contener espacios."""
    codigo_de_verificacion = input("ingrese un codigo de verificacion de 4 caracteres: ")   # Validaciones
    if len(codigo_de_verificacion) != 4: 
        print("El código de verificación debe tener al menos 4 caracteres.")
    if ' ' in codigo_de_verificacion:
        print("El código de verificación no puede contener espacios.")
        return
    if not any(c.isupper() for c in codigo_de_verificacion):
        print("El código de verificación debe incluir al menos una letra mayúscula.")
        return
    if not any(c.isdigit() for c in codigo_de_verificacion):
        print("El código de verificación debe incluir al menos un número.")
        return
    
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
    
    print("*Matricula exitosa*")

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
            print("Usuario eliminado...")
            return  
    print("usuario no encontrado")          

def cupos_disponibles():
    print(f"cupos disponibles niños: {cupos_niños}")
    print(f"cupos disponibles adultos: {cupos_adultos}")

def salir():
    print("Programa finalizado...")
    exit(0)

main() 


