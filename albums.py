import uuid 

class Album:
    def __init__(self,identificador,nombre,descrip,cover,genre,arts,tracklist,publi):
        self.id = identificador
        self.name = nombre
        self.description = descrip
        self.genre = genre
        self.artist = arts
        self.tracklist= tracklist
        self.published= publi
        self.cover = cover
    
    @staticmethod
    def create_album(lista_album, usuario,users):
        username = usuario['n_usuario']
        for user in users:
            if user['n_usuario'] == username and user['tipo'] == 'musician':
                user_id = user['id']
                nombre_album = input("Ingrese el nombre del álbum: ")
                descripcion = input("Ingrese la descripción del álbum: ")
                cover = input("Ingrese el enlace de la portada del álbum: ")
                publicacion = input("Ingrese la fecha de publicación del álbum: ")
                genero = input("Ingrese el género del álbum: ")
                tracklist = []
                while True:
                    nombre_cancion = input("Ingrese el nombre de la canción (deje en blanco para terminar): ")
                    if not nombre_cancion:
                        break
                    duracion = input("Ingrese la duración de la canción: ")
                    link = input("Ingrese el enlace de la canción: ")
                    cancion_id = str(uuid.uuid4())
                    tracklist.append({
                        "id": cancion_id,
                        "name": nombre_cancion,
                        "duration": duracion,
                        "link": link
                    })
                new_album = {
                    "id": str(uuid.uuid4()),
                    "name": nombre_album,
                    "description": descripcion,
                    "genre": genero,
                    "artist": user_id,
                    "tracklist": tracklist,
                    "published": publicacion,
                    "cover": cover
                }
                lista_album.append(new_album)
                return lista_album
        print("Usuario no encontrado o el usuario no es un músico.")
        return lista_album  
            
        


        

                    

                
        



