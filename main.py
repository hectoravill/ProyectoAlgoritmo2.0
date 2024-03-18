from usuarios import Musico,Escucha, Usuario
from funciones import guardar_data
from estadisticas import artist_most_streams
from playlist import Playlist
from albums import Album
import requests 
import json
#Esta funcion sirve para actualizar los datos en los archivos JSON
def actualizar_datos(datos_actualizados, archivo):
    try:
        with open(archivo, 'w') as file:
            json.dump(datos_actualizados, file, indent=4)
        print("")
    except Exception as e:
        print("Error al actualizar datos:", e)


#Esta funcion sirve para cargar los datos de los archivos JSON
def cargar_datos(route_archive):
    try:
        with open(route_archive,'r')as file:
            data_users = json.load(file)
    except FileNotFoundError:
        print(f"El archivo {route_archive} no existe")
        data_users = []
    except json.JSONDecodeError:
        print("Error al decodificar datos JSON")
        data_users = []    
    return data_users
   
link_album = " https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
link_playlist= " https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"
link_users= " https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"

arch_users = "usuarios.json"
arch_albums = "albums.json"
arch_playlist = "playlist.json"

response_users = requests.get(link_users)
response_albums = requests.get(link_album)
response_playlist = requests.get(link_playlist)

data_playlist = response_playlist.json()
data_album = response_albums.json()
data_users = response_users.json()

lista_usuario =[]
lista_album = []
lista_playlist =[]
#Aqui se reordenan los archivos
for user in data_users:
   if user['type'] == 'musician':
      musico = Musico(user['id'],user['name'],user['email'],user['username'])
      lista_usuario.append(musico)
   elif user['type'] == 'listener':
      escucha = Escucha(user['id'],user['name'],user['email'],user['username'])
      lista_usuario.append(escucha)

for album in data_album:
   album = Album(album['id'],album['name'],album['description'],album['cover'],album['genre'],album['artist'],album['tracklist'],album['published'])
   lista_album.append(album)

for playlist in data_playlist:
   playlist = Playlist(playlist['id'],playlist['name'],playlist['description'],playlist['creator'],playlist['tracks'])
   lista_playlist.append(playlist)

#En esta parte se tienen los datos originales, si opcion = si entonces se cargan los datos originales,si se pone cualquier otra cosa, se continua con los archivos como estaban  
opcion = input("Desea guardar los datos originales?: ")
if opcion == "si":
   guardar_data(lista_playlist, arch= arch_playlist)
   guardar_data(lista_album, arch= arch_albums)
   guardar_data(lista_usuario, arch= arch_users)

#Este es el menu
def menu():
   while True:
        
        albums_json = cargar_datos(arch_albums)
        playlist_json = cargar_datos(arch_playlist)
        usuarios_json = cargar_datos(arch_users)
        
        op = input('''<<<METROTIFY>>>\nBIENVENIDO A METROTIFY\n Ingrese la opcion que desee:
                   \n1. Crear Usuario\n2. Log in\n3. Cerrar programa\n>>>''')
        while op != '1' and op!= '2' and op != '3':
            op = input('''<<<METROTIFY>>>
                   \n1. Crear Usuario\n2. Log in\n3. Cerrar programa\n>>>''')
        if op == '1':
            usuario_ = Usuario.crear_usuario(usuarios_json)
            actualizar_datos(usuario_ , arch_users)   
            
        elif op == '2':
            
            usuario_login = Usuario.login(usuarios_json)

            while True:
                if usuario_login['tipo'] == 'musician':
                    
                    opcionA = input('''<<<METROTIFY>>>
                          \n1. Gestion de perfil\n2. Buscador\n3. Crear album\n4. Bibioteca\n5. Estadisticas\n6. Salir\n>>>''')
                    while opcionA != "1" and opcionA != "2" and opcionA != "3" and opcionA != "4" and opcionA != "5" and opcionA!="6":
                        opcionA = input('''<<<METROTIFY>>>
                          \n1. Gestion de perfil\n2. Buscador\n3. Crear album\n4. Bibioteca\n5. Estadisticas\n6. Salir\n>>>''')
                    if opcionA == "1":
                        while True:
                            opcionB = input("<<<Gestion de perfil>>>\n1. Actualizar Usuario\n2. Eliminar Usuario\n3. Salir\n>>>")
                            while opcionB != "1" and opcionB != "2" and opcionB != "3" :
                                opcionB = input("<<<Gestion de perfil>>>\n1. Actualizar Usuario\n2. Eliminar Usuario\n3. Salir\n>>>")
                            if opcionB == "1":
                                updated_user = Usuario.update_info(usuario_login,usuarios_json)
                                actualizar_datos(updated_user, arch_users)
                            elif opcionB =="2":
                                deleted_user = Usuario.delete_user(usuario_login,usuarios_json)
                                actualizar_datos(deleted_user,arch_users)
                            elif opcionB =="3":
                                break
                            
                    elif opcionA == "2":
                        print("Buscador")
                        while True:
                            opcionC = input("<<<Buscador>>>\n1. Buscar Usuario\n2. Buscar Playlist\n3. Buscar Album\n4. Buscar cancion y escuchar\n5.Buscar cancion y guardar\n6. Salir\n>>>")
                            while opcionC != "1" and opcionC != "2" and opcionC != "3" and opcionC != "4" and opcionC != "5" and opcionC != "6":
                                opcionC = input("<<<Buscador>>>\n1. Buscar Usuario\n2. Buscar Playlist\n3. Buscar Album\n4. Buscar cancion y escuchar\n5.Buscar cancion y guardar\n6. Salir\n>>>")
                            if opcionC == "1":
                                user_found = Usuario.buscar_nombre(usuarios_json)
                                
                                if user_found['tipo'] == 'listener':
                                    print(f"<<<{user_found['nombre']}>>>")
                                    eleccion = input("Ingrese la opcion que desea:\n1. Ver canciones guardadas\n2. Ver albums guardados\n3. Ver playlists guardadas\n4. Ver playlists creadas\n5. Salir\n>>>")
                                    while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
                                        eleccion = input("Ingrese la opcion que desea:\n1. Ver canciones guardadas\n2. Ver albums guardados\n3. Ver playlists guardadas\n4. Ver playlists creadas\n5. Salir\n>>>")
                                    if eleccion == "1":
                                        if 'liked_songs' not in user_found:
                                            print("El usuario no tiene canciones guardadas")
                                        else:
                                            print(f"Canciones guardadas: {user_found['liked_songs']}")
                                    elif eleccion == "2":
                                        if 'liked_albums' not in user_found:
                                            print("El usuario no tiene albums guardados")
                                        else:
                                            print(f"Albums guardados: {user_found['liked_albums']}")
                                    elif eleccion ==  "3":
                                        if 'liked_playlist' not in user_found:
                                            print("El usuario no tiene playlist guardadas")
                                        else:
                                            print(f"Playlists guardadas: {user_found['liked_playlists']}")
                                    elif eleccion == "4":
                                        Usuario.made_playlist(user_found,usuarios_json,playlist_json) 
                                    elif eleccion =="5":  
                                        break
                                else:
                                    print(f"<<<{user_found['nombre']}>>>")
                                    eleccion2 = input("Ingrese la opcion que desea:\n1. Ver albums de musica\n2. Top 10 canciones mas escuchadas\n3. Cantidad total de reproducciones\n4. Salir\n>>>")
                                    while eleccion2 != "1" and eleccion2 != "2" and eleccion2 != "3" and eleccion2!="4":
                                        eleccion2 = input("Ingrese la opcion que desea:\n1. Ver albums de musica\n2. Top 10 canciones mas escuchadas\n3. Cantidad total de reproducciones\n4. Salir\n>>>")
                                    if eleccion2 == "1":
                                        Usuario.show_artist_albums(user_found,albums_json)

                                        x = input("Ingrese la opcion que desea:\n1. Ver tracklist de album\n2. Dar like a un album\n3. Salir\n>>>")
                                        while x != "1" and x != "2" and x != "3":
                                           x = input("Ingrese la opcion que desea:\n1. Ver tracklist de album\n2. Dar like a un album\n3. Salir\n>>>")
                                        if x == "1":
                                            Usuario.show_artist_tracklist_album(user_found,albums_json)
                                            
                                            z = input("Ingrese la opcion que quiera:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                            while z!="1"and z!="2" and z!="3":
                                                z = input("Ingrese la opcion que quiera:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>") 
                                            if z =="1":
                                                listen_1 = Usuario.listen_song(albums_json)
                                                actualizar_datos(listen_1,arch_albums)
                                            elif z =="2":
                                                like_1 = Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                                actualizar_datos(like_1,arch_users) 
                                            elif z =="3":
                                                break
                                        elif x =="2":
                                            like_2=Usuario.like_album_in_artist(usuario_login,usuarios_json,albums_json)
                                            actualizar_datos(like_2,usuarios_json)
                                        elif x =="3":
                                            break
                                    elif eleccion2 =="2":
                                        pass
                                    elif eleccion2 =="3":
                                        pass
                                    elif eleccion2=="4":
                                        break
                            elif opcionC=="2":
                                playlist_found =Usuario.search_playlist(playlist_json)
                                if playlist_found == None:
                                    print("Playlist no se encontro")
                                    break
                                else:
                                    w = input("Ingrese la opcion que desea:\n1. Guardar playlist\n2. Ver tracklist\n3. Salir\n>>>")
                                    while w !="1" and w!= "2" and w!= "3":
                                        w = input("Ingrese la opcion que desea:\n1. Guardar playlist\n2. Ver tracklist\n3. Salir\n>>>")
                                    if w =="1":
                                        like_3 = Usuario.like_playlist(usuario_login,playlist_found,playlist_json,usuarios_json)
                                        actualizar_datos(like_3,arch_users)
                                    elif w =="2":
                                        Usuario.show_playlist_tracks(playlist_found,playlist_json,albums_json)
                                        n = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        while n!="1" and n!="2" and n!="3":
                                            n = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        if n =="1":
                                            listen_2 = Usuario.listen_song(albums_json)
                                            if listen_2 == None:
                                                print("Ocurrio un error")
                                            else:
                                                actualizar_datos(listen_2,arch_albums)
                                        elif n =="2":
                                            like_7= Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                            actualizar_datos(like_7, arch_users)
                                    elif w =="3":
                                        break      
                            elif opcionC=="3":
                                album_found = Usuario.search_album(albums_json)
                                if album_found == None:
                                    print("Album no se encontro")
                                    break
                                else:
                                    print(f"<<<{album_found['name']}")
                                    f = input("Que quiere hacer:\n1. Guardar album\n2. Ver tracklist\n3. Salir\n>>>")
                                    while f != "1" and f!= "2" and f != "3":
                                        f = input("Que quiere hacer:\n1. Guardar album\n2. Ver tracklist\n3. Salir\n>>>")
                                    if f =="1":
                                        like_4=Usuario.like_album(usuario_login,album_found,usuarios_json,albums_json)
                                        actualizar_datos(like_4,arch_users)
                                    elif f =="2":
                                        Usuario.show_tracklist_album(album_found,albums_json)
                                        zzz = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        while zzz!="1" and zzz!="2" and zzz!="3":
                                            zzz = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        if zzz == "1":
                                            pass
                                        elif zzz =="2":
                                            like_5=Usuario.like_song_in_album(usuario_login,album_found,usuarios_json,albums_json)
                                            actualizar_datos(like_5,arch_users)
                                        elif zzz =="3":
                                            break
                                    elif f =="3":
                                        break
                            elif opcionC=="4":
                                listen_3=Usuario.listen_song(albums_json)
                                actualizar_datos(listen_3,arch_albums)
                            elif opcionC=="5":
                                like_6=Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                actualizar_datos(like_6,arch_users)
                            elif opcionC=="6":
                                break
                    elif opcionA == "3":
                        new_album=Album.create_album(albums_json,usuario_login,usuarios_json)
                        actualizar_datos(new_album,arch_albums)
                    elif opcionA =="4":
                        opcionE = input("<<<Biblioteca>>>\n1. Crear Playlist\n2. Ver canciones guardadas\n3. Ver albums guardados\n4. Ver playlists guardadas\n5. Ver mis playlists\n6. Remover like\n7. Salir\n>>>")
                        while opcionE != "1" and opcionE != "2" and opcionE!= "3" and opcionE != "4" and opcionE != "5" and opcionE != "6" and opcionE != "7":
                            opcionE = input("<<<Biblioteca>>>\n1. Crear Playlist\n2. Ver canciones guardadas\n3. Ver albums guardados\n4. Ver playlists guardadas\n5. Ver mis playlists\n6. Remover like\n7. Salir\n>>>")
                        if opcionE == "1":
                            create_play= Usuario.create_playlist(playlist_json,albums_json,usuario_login)
                            actualizar_datos(create_play, arch_playlist)
                        elif opcionE == "2":
                            if 'liked_songs' not in usuario_login:
                                print("No tienes canciones guardadas")
                            else:
                                print(f"{usuario_login['liked_songs']}")
                        elif opcionE =="3":
                            if 'liked_albums' not in usuario_login:
                                print("No tienes albums guardados")
                            else:
                                print(f"{usuario_login['liked_albums']}")
                        elif opcionE =="4":
                            if 'liked_playlists' not in usuario_login:
                                print("No tienes playlists de otros usuarios guardadas")
                            else:
                                print(f"{usuario_login['liked_playlists']}")
                        elif opcionE =="5":
                            Usuario.made_playlist(usuario_login,usuarios_json,playlist_json)
                        elif opcionE =="6":
                            editar1=Usuario.remove_like(usuario_login,usuarios_json)
                            actualizar_datos(editar1,arch_users)
                        elif opcionE =="7":
                            break
                    elif opcionA == "5":
                        print("Top 5 artistas mas escuchados")
                        lista1= artist_most_streams(albums_json,usuarios_json)
                        print(f"{lista1}")
                        break
                    elif opcionA =="6":
                        break    
                    else:
                        print("Ingrese una opcion valida")
                elif usuario_login['tipo'] == 'listener':
                    opcionF = input('''<<<METROTIFY>>>
                          \n1. Gestion de perfil\n2. Buscador\n3. Bibioteca\n4. Estadisticas\n5. Salir\n>>>''')
                    while opcionF != "1" and opcionF != "2" and opcionF != "3" and opcionF != "4" and opcionF!= "5":
                        opcionF = input('''<<<METROTIFY>>>
                          \n1. Gestion de perfil\n2. Buscador\n3. Bibioteca\n4. Estadisticas\n5. Salir\n>>>''')
                    if opcionF =="1":
                        while True:

                            opcionG = input("<<<Gestion de perfil>>>\n1. Actualizar Usuario\n2. Eliminar Usuario\n3. Salir\n>>>")
                            while opcionG != "1" and opcionG != "2" and opcionG != "3" :
                                opcionG = input("<<<Gestion de perfil>>>\n1. Actualizar Usuario\n2. Eliminar Usuario\n3. Salir\n>>>")
                            if opcionB == "1":
                                updated_user = Usuario.update_info(usuario_login,usuarios_json)
                                actualizar_datos(updated_user, arch_users)
                            elif opcionG =="2":
                                deleted_user = Usuario.delete_user(usuario_login,usuarios_json)
                                actualizar_datos(deleted_user,arch_users)
                            elif opcionG =="3":
                                break
                    elif opcionF =="2":
                        print("Buscador")
                        while True:
                            opcionH = input("<<<Buscador>>>\n1. Buscar Usuario\n2. Buscar Playlist\n3. Buscar Album\n4. Buscar cancion y escuchar\n5.Buscar cancion y guardar\n6. Salir\n>>>")
                            while opcionH != "1" and opcionH != "2" and opcionH != "3" and opcionH != "4" and opcionH != "5" and opcionH != "6":
                                opcionH = input("<<<Buscador>>>\n1. Buscar Usuario\n2. Buscar Playlist\n3. Buscar Album\n4. Buscar cancion y escuchar\n5.Buscar cancion y guardar\n6. Salir\n>>>")
                            if opcionH == "1":
                                user_found = Usuario.buscar_nombre(usuarios_json) 
                                if user_found['tipo'] == 'listener':
                                    print(f"<<<{user_found['nombre']}>>>")
                                    eleccion3 = input("Ingrese la opcion que desea:\n1. Ver canciones guardadas\n2. Ver albums guardados\n3. Ver playlists guardadas\n4. Ver playlists creadas\n5. Salir\n>>>")
                                    while eleccion3 != "1" and eleccion3 != "2" and eleccion3 != "3" and eleccion3 != "4":
                                        eleccion = input("Ingrese la opcion que desea:\n1. Ver canciones guardadas\n2. Ver albums guardados\n3. Ver playlists guardadas\n4. Ver playlists creadas\n5. Salir\n>>>")
                                    if eleccion3 == "1":
                                        if 'liked_songs' not in user_found:
                                            print("El usuario no tiene canciones guardadas")
                                        else:
                                            print(f"Canciones guardadas: {user_found['liked_songs']}")
                                    elif eleccion3 == "2":
                                        if 'liked_albums' not in user_found:
                                            print("El usuario no tiene albums guardados")
                                        else:
                                            print(f"Albums guardados: {user_found['liked_albums']}")
                                    elif eleccion3 ==  "3":
                                        if 'liked_playlist' not in user_found:
                                            print("El usuario no tiene playlist guardadas")
                                        else:
                                            print(f"Playlists guardadas: {user_found['liked_playlists']}")
                                    elif eleccion3 =="4":
                                        Usuario.made_playlist(user_found,usuarios_json,playlist_json) 
                                    elif eleccion =="5":  
                                        break
                                else:
                                    print(f"<<<{user_found['nombre']}>>>")
                                    eleccion4 = input("Ingrese la opcion que desea:\n1. Ver albums de musica\n2. Top 10 canciones mas escuchadas\n3. Cantidad total de reproducciones\n4. Salir\n>>>")
                                    while eleccion4 != "1" and eleccion4 != "2" and eleccion4 != "3" and eleccion4!="4":
                                        eleccion4 = input("Ingrese la opcion que desea:\n1. Ver albums de musica\n2. Top 10 canciones mas escuchadas\n3. Cantidad total de reproducciones\n4. Salir\n>>>")
                                    if eleccion4 == "1":
                                        Usuario.show_artist_albums(user_found,albums_json)

                                        ww = input("Ingrese la opcion que desea:\n1. Ver tracklist de album\n2. Dar like a un album\n3. Salir\n>>>")
                                        while ww != "1" and ww != "2" and ww != "3":
                                           ww = input("Ingrese la opcion que desea:\n1. Ver tracklist de album\n2. Dar like a un album\n3. Salir\n>>>")
                                        if ww == "1":
                                            Usuario.show_artist_tracklist_album(user_found,albums_json)
                                            
                                            cc= input("Ingrese la opcion que quiera:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                            while cc!="1"and cc!="2" and cc!="3":
                                                cc = input("Ingrese la opcion que quiera:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>") 
                                            if cc =="1":
                                                listen_1 = Usuario.listen_song(albums_json)
                                                actualizar_datos(listen_1,arch_albums)
                                            elif cc =="2":
                                                like_1 = Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                                actualizar_datos(like_1,arch_users) 
                                            elif cc =="3":
                                                return
                                        elif ww =="2":
                                            like_2=Usuario.like_album_in_artist(usuario_login,usuarios_json,albums_json)
                                            actualizar_datos(like_2,usuarios_json)
                                        elif ww =="3":
                                            break
                                    elif eleccion4 =="3":
                                        pass
                                    elif eleccion4=="2":
                                        pass
                                    elif eleccion4=="4":
                                        break
                            elif opcionH=="2":
                                playlist_found =Usuario.search_playlist(playlist_json)
                                if playlist_found == None:
                                    print("Playlist no se encontro")
                                    break
                                else:
                                    wc = input("Ingrese la opcion que desea:\n1. Guardar playlist\n2. Ver tracklist\n3. Salir\n>>>")
                                    while wc !="1" and wc!= "2" and wc!= "3":
                                        wc = input("Ingrese la opcion que desea:\n1. Guardar playlist\n2. Ver tracklist\n3. Salir\n>>>")
                                    if wc =="1":
                                        like_8 = Usuario.like_playlist(usuario_login,playlist_found,playlist_json,usuarios_json)
                                        actualizar_datos(like_8,arch_users)
                                    elif wc =="2":
                                        Usuario.show_playlist_tracks(playlist_found,playlist_json,albums_json)
                                        no = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        while no!="1" and no!="2" and no!="3":
                                            no = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        if no =="1":
                                            listen_4 = Usuario.listen_song(albums_json)
                                            if listen_4 == None:
                                                print("Ocurrio un error")
                                            else:
                                                actualizar_datos(listen_4,arch_albums)
                                        elif no =="2":
                                            like_9= Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                            actualizar_datos(like_9, arch_users)
                                    elif wc =="3":
                                        break  
                            elif opcionH=="3":
                                album_found = Usuario.search_album(albums_json)
                                if album_found == None:
                                    print("Album no se encontro")
                                    break
                                else:
                                    print(f"<<<{album_found['name']}")
                                    fa = input("Que quiere hacer:\n1. Guardar album\n2. Ver tracklist\n3. Salir\n>>>")
                                    while fa != "1" and fa!= "2" and fa != "3":
                                        fa = input("Que quiere hacer:\n1. Guardar album\n2. Ver tracklist\n3. Salir\n>>>")
                                    if fa =="1":
                                        like_10=Usuario.like_album(usuario_login,album_found,usuarios_json,albums_json)
                                        actualizar_datos(like_10,arch_users)
                                    elif fa =="2":
                                        Usuario.show_tracklist_album(album_found,albums_json)
                                        zzzz = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        while zzzz!="1" and zzzz!="2" and zzzz!="3":
                                            zzzz = input("Desea:\n1. Escuchar cancion\n2. Guardar cancion\n3. Salir\n>>>")
                                        if zzzz == "1":
                                            listen_6=Usuario.listen_song(albums_json)
                                            actualizar_datos(listen_6,arch_albums)
                                        elif zzzz =="2":
                                            like_11=Usuario.like_song_in_album(usuario_login,album_found,usuarios_json,albums_json)
                                            actualizar_datos(like_11,arch_users)
                                        elif zzzz =="3":
                                            break
                                    elif fa =="3":
                                        break
                            elif opcionH=="4":
                                listen_5=Usuario.listen_song(albums_json)
                                actualizar_datos(listen_5,arch_albums)
                            elif opcionH=="5":
                                like_12=Usuario.like_song(usuario_login,usuarios_json,albums_json)
                                actualizar_datos(like_12,arch_users)
                            elif opcionH=="6":
                                break   
                    elif opcionF =="3":
                        opcionI = input("<<<Biblioteca>>>\n1. Crear Playlist\n2. Ver canciones guardadas\n3. Ver albums guardados\n4. Ver playlists guardadas\n5. Ver mis playlists\n6. Remover like\n7. Salir\n>>>")
                        while opcionI != "1" and opcionI != "2" and opcionI!= "3" and opcionI != "4" and opcionI != "5" and opcionI != "6" and opcionI != "7":
                            opcionI = input("<<<Biblioteca>>>\n1. Crear Playlist\n2. Ver canciones guardadas\n3. Ver albums guardados\n4. Ver playlists guardadas\n5. Ver mis playlists\n6. Remover like\n7. Salir\n>>>")
                        if opcionI == "1":
                            create_play= Usuario.create_playlist(playlist_json,albums_json,usuario_login)
                            actualizar_datos(create_play, arch_playlist)
                        elif opcionI == "2":
                            if 'liked_songs' not in usuario_login:
                                print("No tienes canciones guardadas")
                            else:
                                print(f"{usuario_login['liked_songs']}")
                        elif opcionI =="3":
                            if 'liked_albums' not in usuario_login:
                                print("No tienes albums guardados")
                            else:
                                print(f"{usuario_login['liked_albums']}")
                        elif opcionI =="4":
                            if 'liked_playlists' not in usuario_login:
                                print("No tienes playlists de otros usuarios guardadas")
                            else:
                                print(f"{usuario_login['liked_playlists']}")
                        elif opcionI =="5":
                            Usuario.made_playlist(usuario_login,usuarios_json,playlist_json)
                        elif opcionI =="6":
                            editar=Usuario.remove_like(usuario_login,usuarios_json)
                            actualizar_datos(editar,arch_users)
                        elif opcionI =="7":
                            break
                    elif opcionF == "4":
                        print("Top 5 artistas mas escuchados")
                        lista1= artist_most_streams(albums_json,usuarios_json)
                        print(f"{lista1}")
                        break
                    elif opcionF =="5":
                        break
                elif usuario_login== None:
                
                    break
        elif op == '3':
            break 
        else:
            print("Opcion ingresada no es valida")



menu()

           
               
