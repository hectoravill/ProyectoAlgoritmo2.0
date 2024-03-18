import matplotlib.pyplot as plt
#Funcion para saber el top 5 artistas con mas streams
def artist_most_streams(albums,users):
    streams_artists = {}
    for album in albums:
        artista_id = album.get('artist')
        nombre_artista = None
        for artista in users:
            if artista.get('id') == artista_id:
                nombre_artista = artista.get('nombre')
                break
        total_streams = 0
        for track in album.get('tracklist',[]):
            total_streams += track.get('streams',0)
        if nombre_artista in streams_artists:
            streams_artists[nombre_artista] += total_streams
        else:
            streams_artists[nombre_artista] = total_streams
    artistas_soted = sorted(streams_artists.items(),key= lambda x: x[1],reverse=True)
    #Esta parte de la funcion ordena de mayor a menor los streams de los artistas, se usa .item para separar el nombre de la cantidad de streams, lambda se usa para funciones mas cortas, la x: = a los artistas, el [1] es para fijarse en el segundo argumento,es decir,los streams; reverse es para devolver de mayor a menor
    top_cinco = artistas_soted[:5]
    #Aqui se recibe el top 5 de artistas
    return top_cinco
def artist_most_streamed_songs(usuario,albums):
    most_streamed_songs = {}
    artist_id = usuario['id']
    for album in albums:
       if album['artist'] == artist_id:
           song_name = None
           
               


def graficar_top(data,titulo,x_label,y_label):
#data = top, titulo = el titulo, x_label es a lo que equivale x en el grafico y y_label el grafico en y
    nombres = [item[0] for item in data]
    valores = [item[1]for item in data]
    plt.figure(figsize=(10,6))
    plt.bar(nombres,valores,color='blue')
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45, ha='right')
    #Esto se refiere a la posicion
    plt.show()