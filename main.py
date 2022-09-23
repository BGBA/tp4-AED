from registro import Proyectos
from registro import Display
def Mostrar_menu():
    menu = """
    1) Cargar Datos 
    2) Filtrar por tag 
    3) Filtrar por Lenguaje 
    4) Filtrar por poplaridad 
    5) Buscar proyecto 
    6) Guardar populares 
    7) Mostrar archivo 
    8) Salir 
    """
    print(menu)


def Mostrar_datos(lista_proyectos):
    for proyecto in lista_proyectos:
        Display(proyecto)

#punto 1
def Cargar_datos(lista_proyectos):
    file = "proyectos.csv"
    archivo = open(file, mode="rt", encoding="utf8")
    first = True
    for i in archivo:
        if first:
            first = False
            pass
        else:
            linea = i.split("|")
            proyecto = Proyectos(linea[0], linea[1], linea[3], linea[4], linea[5], linea[6], linea[7])
            lista_proyectos.append(proyecto)
    archivo.close()
    return file

#punto 2
def get_estrellas(proyecto):
    x = float((proyecto.Likes).split("k")[0])*1000
    estrellas = 0
    if 0 < int(x) < 10000:
        estrellas = 1
    elif 10100 < int(x) < 20000:
        estrellas = 2
    elif 20100 < int(x) < 30000:
        estrellas = 3
    elif 30100 < int(x) < 40000:
        estrellas = 4
    elif int(x) > 40000:
        estrellas = 5
    return estrellas
def mostrar_punto2(proyecto):
    estrellas = "🌟"*get_estrellas(proyecto)
    return f'{proyecto.Repositorio:<30}{proyecto.Fecha_actualizacion:<14}{estrellas:<7}'
def Filtrar_por_tag(lista_proyectos, btag):
    first = True
    for proyecto in lista_proyectos:
        vectortags = proyecto.Tags.split(",")
        for tag in vectortags:
            if tag == btag.lower():
                if first==True:
                    print(f'{"Repositorio":<30}{"Fecha":<14}{"Estrellas":<5}')
                    first=False
                print(mostrar_punto2(proyecto))
#punto 3
def get_lenguajes(lista_proyectos):
    lista_lenguajes = []
    for proyecto in lista_proyectos:
        lista_lenguajes.append(proyecto.Lenguaje)
    return lista_lenguajes
def get_lenguajes_unicos(lista_proyectos):
    lenguajes_unicos = []
    lista_lenguajes = get_lenguajes(lista_proyectos)
    for lenguaje in lista_lenguajes:
        if lenguaje not in lenguajes_unicos:
            lenguajes_unicos.append(lenguaje)
    return lenguajes_unicos
def Filtrar_lenguaje(lista_proyectos):
    lenguajes = get_lenguajes(lista_proyectos)
    lenguajes_unicos = get_lenguajes_unicos(lista_proyectos)
    vuelta = 0
    conteo = [0] * len(lenguajes_unicos)
    for lenguajeu in lenguajes_unicos:
        a = lenguajes.count(lenguajeu)
        conteo[vuelta] += a
        vuelta += 1
    print(len(lenguajes_unicos),lenguajes_unicos)
    print(len(conteo),conteo)
    for i in range(len(conteo)):
        print("Lenguaje:",lenguajes_unicos[i],":",conteo[i])


def Principal():
    lista_proyectos = []
    opcion = 0
    while opcion != 8:
        Mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            file = Cargar_datos(lista_proyectos)
            print("Se cargaron los proyectos desde el archivo", str(file))
            pass
        elif opcion == 2:
            btag = str(input("Ingrese el tag que quiere buscar: "))
            Filtrar_por_tag(lista_proyectos, btag)
            pass
        elif opcion == 3:
            Filtrar_lenguaje(lista_proyectos)
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            break
        else:
            print("opcion incorrecta")
        

if __name__ == '__main__':
    Principal()
