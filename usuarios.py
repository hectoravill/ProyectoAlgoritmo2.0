import uuid
class Usuario:

    def __init__(self,identificacion,nombre,email,n_usuario,tipo):
        self.id= identificacion
        self.nombre= nombre
        self.email= email
        self.n_usuario= n_usuario
        self.tipo= tipo
    
    @classmethod
    def crear_usuario(self,usuarios):
        identificacion = str(uuid.uuid4())
        nombre = input("Ingrese el nombre:")
        
        n = 'y'
        while n =='y':
            email = input("Ingrese su email:")
            if "@" and ".com" or ".ve" in email:
                print("Email validado")
                n = 'n'
            else:
                print("Email invalido")
        
        a = 'y'
        while a == 'y':
            username = input("Ingrese un nombre de usuario:")
            for user in usuarios:
                if username == user['n_usuario']:
                    print("Nombre de usuario ingresado ya esta en uso")
            else:
                print("Nombre de usuario validado")
                a = 'n'
        opciones = ['musician','listener']

        
        b = 'y'
        while b =='y':
            tipo = input("Ingrese el tipo(musico o escucha):")
            if tipo == "escucha":
                tipo = opciones[1]
                print("Tipo escucha sleccionado")
                b ='n'
            elif tipo == "musico":
                tipo = opciones[0]
                print("Tipo musico seleccionado")
                b = 'n'
            else: 
                print("Ingrese un tipo valido (musico o escucha)")
        nuevo_usuario = {
            'id':identificacion,
            'nombre': nombre,
            'email': email,
            'n_usuario': username,
            'tipo':tipo 
            }    
        usuarios.append(nuevo_usuario)
        return usuarios
#Esta funcion sirve para crear los usuarios
    @classmethod
    def buscar_nombre(cls, usuarios):
        nombre = input("Ingrese el nombre de usuario:")
        for usuario in usuarios:
            if usuario['n_usuario'] == nombre:
                return usuario
              
        else:
            print("El usuario buscado no existe")
            return
#Esta funcion sirve para buscar el nombre de usuario en usuarios.json
    @classmethod         
    def update_info(cls,usuario,users):
        while True:
            id_user = usuario['id']
            for user in users:
                if user['id'] == id_user:
                    opcion = input("<<<Actualizar Usuario>>>\n1. Nombre\n2. Correo\n3. Nombre de Usuario\n4. Tipo de usuario\n5. Salir\n>>>")
    
                    if opcion == '1':
                        new_name = input("Ingrese el nuevo nombre: ")
                        user['nombre'] = new_name 
                        print("Nombre actualizado")
                    elif opcion == '2':
                        new_email = input("Ingrese el nuevo email: ")
                        if any(u['email'] == new_email for u in users):
                            print("Ya hay un usuario registrado con este email")
                        elif "@" in new_email:
                            user['email'] = new_email
                            print("Correo electrónico actualizado")
                        else:
                            print("Correo inválido")
                    elif opcion == '3':
                        new_username = input("Ingrese el nuevo nombre de usuario: ")
                        if any(u['n_usuario'] == new_username for u in users):
                            print("Nombre de usuario ingresado ya está en uso")
                        else:
                            user['n_usuario'] = new_username
                            print("Nombre de usuario actualizado")
                    elif opcion == '4':
                        new_type = input("Seleccione el tipo de cuenta (escucha o musico): ")
                        if new_type in ['listener', 'musician']:
                            user['tipo'] = new_type
                            print("Tipo de cuenta actualizado")
                        else:
                            print("Tipo no válido")
                    elif opcion == '5':
                        return users
                    else:
                        print("Hubo un error. Seleccione una opción válida.")
#Esta funcion actualiza los datos del usuario en usuarios.json               
    @classmethod     
    def delete_user(cls, usuario,users):
        username= usuario['n_usuario']
        usuario_eliminar =None
        for user in users:
            if user['n_usuario'] == username :
                usuario_eliminar= user
        
                users.remove(usuario_eliminar)
        else:
            print("Perfil no encontrado")
        return users
#Esta funcion elimina el usuario de usuarios.json
    @staticmethod
    def listen_music_album(albums):
        album_name = input("Ingrese el nombre del album:")
        for album in albums:
            if album_name == album['name']:
                canciones = album['tracklist']
                print("Tracklist:")
                for track in canciones:
                    print(f"- {track['name']}")
                
                opcion_cancion = input("Ingrese el nombre de la cancion que desee escuchar:")
                
                for track in canciones:
                    if opcion_cancion == track['name']:
                        print(f" Escuchando {track['name']}")
                        if 'streams' in track:
                            track['streams'] +=1
                        else: 
                            track['streams'] =1
                        return albums
                else:
                    print(f"{opcion_cancion} no se encontro")
                return    
        else:
            print(f"No se encontro un album con el nombre: {album_name}")
#Esta funcion permite "escuchar" una cancion desde un album
    def listen_song(albums):
        song = input("Ingresa el nombre de la cancion:")
        for album in albums:
            tracks = album['tracklist']
            for track in tracks:
                if song == track['name']:
                    print(f"Escuchando {song}")
                    if 'streams' in track:
                        track['streams'] +=1
                    else: 
                        track['streams'] =1
                    return albums
        else:
            print(f"{song} no se encontro ")
            return
                
#Esta funcion permite "escuchar" una cancion    
    def song_musician(albums,usuarios):
        name = input("Ingrese el nombre del artista:")
        found_user = None
        for user in usuarios:
            if name.lower().strip()== user['nombre'].lower().strip():
                found_user = user 
            if found_user:
                artist_albums = []
                for album in albums:
                    if album['artist'] == found_user['id']:
                        artist_albums.append(album)
                
                if artist_albums:
                    print("Albums del artista:")
                    for album in artist_albums:
                        print(f" - {album['name']}")
                        
                    album_name = input("Escriba el album que quiere abrir:").strip().lower()
                    for album in artist_albums:
                        if album_name == album['name']:
                            tracklist = album['tracklist']
                            for track in tracklist:
                                print(f" - {track['name']}")
                    
                            song = input("Ingrese la cancion que desea escuchar:")

                            for track in tracklist:
                                if song.lower().strip() == track['name']:
                                    print(f"Escuchando {song} ")
                                    if 'streams' in track:
                                        track['streams'] += 1
                                    else:
                                        track['streams'] = 1
                            return albums
                    else:
                        print(f"{album_name} no se encontro")
                    return
        else:
            print("Usuario buscado no es un artista o no existe")
        return
#La funcion song_musician la usaba para pasar a "escuchar" directamente la cancion de un artista sin antes pasar por otras opciones  
    
    def song_playlist(fplaylist, playlists, albums):
        p_name = fplaylist['name']
        for playlist in playlists:
            if p_name == playlist['name']:
                for track_id in playlist['track']:
                    for album in albums:
                        for track in album['tracklist']:
                            if track_id == track['id']:
                                song = input("Ingrese la canción que desea escuchar: ")
                                if song.lower() == track['name'].lower():
                                    print(f"Escuchando {track['name']}")
                                    track['streams'] = track.get('streams', 0) + 1
                                    return albums
                else:
                    print(f"No se encontró la canción en la lista de reproducción {p_name}")
                return 
        else:
            print(f"No se encontró la lista de reproducción {p_name} en las playlist.")
        return
                                
            

    def create_playlist(playlists,albums,usuario):
        id_user = usuario['id']
        name_playlist = input("Ingrese el nombre de la playlist:")
        description = input("Ingrese la descripcion:")
        amount = int(input("Ingrese la cantidad de canciones que desea agregar:"))
        track = []
        for _ in range(amount):
            song = input("Ingrese el nombre de la cancion:")
            for album in albums:
                for trac in album['tracklist']:
                    if song == trac['name']:
                        track.append(trac['id'])
            print(track)
        playlists.append({
            "id": str(uuid.uuid4()),
            "name": name_playlist,
            "description": description,
            "creator": id_user,
            "track": track
        })
        return playlists
#Esta funcion permite crear una playlist

    def login(usuarios):
        n_user = input("Ingrese su nombre de usuario:")
        email = input("Ingrese su email:")
        for user in usuarios:
            if n_user == user['n_usuario'] and email == user['email']:
                print(f"Bienvenido {user['nombre']}")
                return user
        else:
            print(f"{n_user} o {email} son incorrectos")
            return 
#Esta funcion permite hacer el login
    def like_artista(usuario,users):
        id_user = usuario['id']
        for user in users:
            if user['id'] == id_user:
                like_artist = input("Ingrese el nombre de usuario del artista que desea likear:")
                for user in users:
                    if user['n_usuario'] == like_artist and user['tipo'] == 'musician':
                        if 'liked_artist' not in user:
                            usuario['liked_artist'] = []
                        if user['id'] in usuario['liked_artist']:
                            print("No puede darle like 2 veces")
                        else:
                            usuario['liked_artist'].append(user['n_usuario'])
                else:
                    print("El nombre del artista no es el correcto o el usuario no es un artista")
        return users
#Esta funcion permite dar like a un artista, no la utilice al final        
    def like_song(usuario,users,albums):
        usuario_like = usuario['n_usuario']
        for user in users:
            if user['n_usuario'] == usuario_like:   
                song = input("Ingrese el nombre de la cancion que desea likear:")
                for album in albums:
                    for track in album['tracklist']:
                        if track['name'] == song:
                            print("Cancion guardada")
                            if 'liked_songs' not in user:
                                user['liked_songs'] = []
                            if track['name'] in user['liked_songs']:
                                print("No puede darle like dos veces")
                            else:
                                user['liked_songs'].append(track['name'])
                return users
#Esta funcion permite darle like a una cancion
    def made_playlist(usuario,users,playlists):
        usuario_id = usuario['id']
        for user in users:
            if user['id'] == usuario_id:
                for playlist in playlists:
                    if usuario_id == playlist['creator']:
                        print("<<<Playlists>>>")
                        print(f" -{playlist['name']} ")
                else:
                    print("El usuario no tiene playlists creadas")
                return
#Esta funcion permite ver las playlists creadas por los usuarios
    def show_artist_albums(usuario,albums):
        user_id = usuario['id']
        for album in albums:
            if album['artist'] == user_id:
                
                print(f"- {album['name']}")          
            
        return 
#Muestra los albums de un artista
    def show_artist_tracklist_album(usuario,albums):
        
        user_id = usuario['id']
        album_name = input("Ingrese el nombre del álbum que quiere visualizar: ")
        
        for album in albums:
            if album['artist'] == user_id and album['name'] == album_name:
                print("<<<Tracklist>>>")
                for track in album['tracklist']:
                    print(f"- {track['name']}")
                return
        else:
            print("El álbum ingresado no existe o no pertenece al artista.")
#Muestra el tracklist del album de un artista
    def like_album_in_artist(usuario,users,albums):

        usuario_like = usuario['n_usuario']
        for user in users:
            if user['n_usuario'] == usuario_like:   
                song = input("Ingrese el nombre del album que desea likear:")
                for album in albums:
                    
                    if album['name'] == song:
                        print("Album guardado")
                        if 'liked_albums' not in user:
                                user['liked_albums'] = []
                        if album['name'] in user['liked_albums']:
                            print("No puede darle like dos veces")
                        else:
                            user['liked_albums'].append(album['name'])
                return users
#Permite darle like al album de un artista 
    def search_playlist(playlists):
        n_playlist = input("Ingrese el nombre de la playlist:")
        for playlist in playlists:
            if playlist['name'] == n_playlist:
                return playlist
        else:
            print("No existe una playlist con ese nombre")
            return 
#Busca la playlist
    def like_playlist(usuario,fplaylist,playlists,users):
        usuario_like = usuario['n_usuario']
        n_playlist = fplaylist['name']
        for user in users:

            if user['n_usuario'] == usuario_like:   
                
                for playlist in playlists:
                    if playlist['name'] == n_playlist:   
                        print("Playlist guardada")
                        if 'liked_playlists' not in user:
                            user['liked_playlists'] = []
                        if playlist['name'] in user['liked_playlists']:
                            print("No puede darle like dos veces")
                        else:
                            user['liked_playlists'].append(playlist['name'])
                return users
#Permite darle like a una playlist
    def show_playlist_tracks(fplaylist,playlists,albums):
        p_name = fplaylist['name']
        for playlist in playlists:
            if p_name == playlist['name']:
                for tracks in playlist['track']:
                    for album in albums:
                        for cancion in album['tracklist']:
                            if tracks == cancion['id']:
                                print(f" - {cancion['name']}")
        return
#Muestra el tracklist de una playlist
    def search_album(albums):
        n_album = input("Ingrese el nombre del album:")
        for album in albums:
            if album['name'] == n_album:
                return album
   
        else:
            print("El album buscado no existe")
            return
#Busca un album en albums.json  
    def show_tracklist_album(falbum,albums):
        n_album = falbum['name']
        for album in albums:
            if n_album == album['name']:
                for canciones in album['tracklist']:
                    print(f" - {canciones['name']}") 
                return
#Muestra el tracklist de un album
    def like_album(usuario,falbum,users,albums):
        usuario_like = usuario['n_usuario']
        n_playlist = falbum['name']
        for user in users:

            if user['n_usuario'] == usuario_like:   
                
                for album in albums:
                    if album['name'] == n_playlist:   
                        print("Album guardado")
                        if 'liked_albums' not in user:
                            user['liked_albums'] = []
                        if album['name'] in user['liked_albums']:
                            print("No puede darle like dos veces")
                        else:
                            user['liked_albums'].append(album['name'])
                return users
#Permite darle like a un album
    def like_song_in_album(usuario,falbum,users,albums):
        usuario_like = usuario['n_usuario']
        n_album = falbum['name']
        for user in users:
            if user['n_usuario'] == usuario_like:   
                song = input("Ingrese el nombre de la cancion que desea likear:")
                for album in albums:
                    if n_album == album['name']:
                        for track in album['tracklist']:
                            if track['name'] == song:
                                print("Cancion guardada")
                                if 'liked_songs' not in user:
                                    user['liked_songs'] = []
                                if track['name'] in user['liked_songs']:
                                    print("No puede darle like dos veces")
                                else:
                                    user['liked_songs'].append(track['name'])
                return users
#Permite darle like a una cancion en un album
    def remove_like(usuario,users):
        while True:
            id_user = usuario['id']
            for user in users:
                if user['id'] == id_user:
                    ya_casi_termino_8pm = input("Ingrese la opcion que desea:\n1. Eliminar cancion de guardados\n2. Eliminar album de guardados\n3. Eliminar playlists de guardados\n4. Salir\n>>>")
                    if ya_casi_termino_8pm == "1":
                        cancion = input("Ingrese la cancion que desea eliminar:")
                        if cancion in user['liked_songs']:
                            user['liked_songs'].remove(cancion)
                        else:
                            print("Cancion no esta en guardados")
                    elif ya_casi_termino_8pm =="2":
                        album = input("Ingrese la cancion que desea eliminar:")
                        if album in user['liked_albums']:
                            user['liked_albums'].remove(album)
                        else:
                            print("Album ingresado no esta guardado")
                    elif ya_casi_termino_8pm =="3":
                        playlist = input("Ingrese la playlist que desea eliminar:")
                        if playlist in user['liked_playlists']:
                            user['liked_playlists'].remove(playlist)
                        else:
                            print("Playlist no esta guardada")
                    elif ya_casi_termino_8pm =="4":
                        return users
#Quita cualquier cosa que haya sido "likeada"
class Escucha(Usuario):
    def __init__(self,identificacion,nombre,email,n_usuario):
        super().__init__(identificacion,nombre,email,n_usuario, tipo = 'listener')

class Musico(Usuario):
    def  __init__(self,identificacion,nombre,email,n_usuario):
        super().__init__(identificacion,nombre,email,n_usuario, tipo = 'musician')


