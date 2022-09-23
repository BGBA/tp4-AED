import pickle


class Proyectos():
    def __init__(self,nombre_usuario,repositorio,fecha_actualizacion,lenguaje,likes,tags,url):
        self.Nombre_usuario = nombre_usuario
        self.Repositorio = repositorio
        self.Fecha_actualizacion = fecha_actualizacion
        self.Lenguaje = lenguaje
        self.Likes = likes
        self.Tags = tags
        self.Url = url


def Display(proyecto):
    print('Nombre de usuario:', proyecto.Nombre_usuario, end=' ')
    print("Repositorio:", proyecto.Repositorio, end=' ')
    print("Fecha de actualizacion:", proyecto.Fecha_actualizacion, end=', ')
    print("Lenguaje:", proyecto.Lenguaje, end=' ')
    print("Likes:", proyecto.Likes, end=' ')
    print("Tags:", proyecto.Tags, end=' ')
    print("Url:", proyecto.Url, end=' ')


def Test():
    print("priueba de generacion de registros")
    m = open("proyectos.csv", mode="rt", encoding="utf8")
    a = pickle.load(m)
    Display(a)
