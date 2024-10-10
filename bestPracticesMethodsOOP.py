class Alumno:
    # Crea la función constructor con atributos vacíos
    def __init__(self, nombre="", apellido_paterno="", apellido_materno="", no_control=0, semestre=1):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos para establecer (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    # Método para obtener el nombre completo
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"


# Diccionario para almacenar los alumnos
registro_alumno = {}

# Bucle para ingresar datos de 3 alumnos
for i in range(3):
    alumno = Alumno()  # Crear instancia de Alumno
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i + 1}: ")
    apellido_materno = input(f"Ingrese el apellido materno del alumno {i + 1}: ")
    no_control = int(input(f"Ingrese el número de control del alumno {i + 1}: "))
    semestre = int(input(f"Ingrese el semestre del alumno {i + 1}: "))

    # Asignar valores al alumno
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

    # Guardar el alumno en el diccionario
    registro_alumno[i] = alumno

# Mostrar los nombres completos de los alumnos registrados
for i in range(3):
    print(f"Nombre completo del alumno {i + 1}: {registro_alumno[i].get_nombre_completo()}")
