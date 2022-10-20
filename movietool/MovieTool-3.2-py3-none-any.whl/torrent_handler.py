from feedparser import exceptions
from qbittorrent import Client
import time
import os
import shutil


# Exeptions:
class CategoryContentError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))

class SeasonEpisodeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))






def torrent_handler(torrent_name: str, original_name: str, route_moviesdb: str, torrent_type: str, qbtorrent_host: str, qbtorrent_user='admin', qbtorrent_pass='adminadmin', handler_time = 10, season = 'SXX', episode = 'EXX'):
    """
    ¡Usa ese módulo para estar pendiente de sí tus torrents ya descargaron! Recomendamos ejectuar esto en un nuevo hilo.
    
    
    Params
    =======
    torrent_name: str | Nombre del torrent a visualizar.

    original_name: str | El nombre oficial de la serie/pelicula. Esto lo usamos para renombrar archivos, crear carpetas etc.

    route_moviesdb: str | Ruta definitiva para el contenido. Esta ruta es la que tomará plex para ver el contenido. Lo ideal sería que una vez  establecida no fuera cambiada, por tanto, ten en cuenta esto.

    torrent_type: str | El tipo de contenido que está intentando rastrear. Ese parametro soporta SOLO dos valores: 'tv' o 'movie'

    qbtorrent_host: str | El host donde esta corriento tu qBittorrent WEB.

    qbtorrent_user: str | Usuario admin en tu qBitTorrrent!

    qbtorrent_pass: str | Contraseña del usuario admin de tu QBitTorrent.

    handler_time: float | Tiempo de espera sobre el cual se harán las peticiones al estado de la descarga, en segundos. Recomiendo no dejar un numero tan alto (como 60), ni tan bajo (como 3).

    season: str | Si el parametro de "torrent_type" es "tv", es necesario especificar la temporada con el formato SXX, donde "X" es el número de temporada. Ej: S01.

    episode: str | Si el parametro de "torrent_type" es "tv", es necesario especificar el episodio con el formato EXX, donde "X" es el número de episodio. Ej: E02.


    """
    
    torrent_category = ['tv', 'movie']

    if torrent_type not in torrent_category:
        raise CategoryContentError('(error 01) Tu "torrent_type" no es valido. Recuerda que, este parametro solo soporta dos valores: "tv" o "movie".')
        exit()
        
    if torrent_type == 'tv' and season == 'SXX' or torrent_type == 'tv' and episode == 'EXX':
        raise SeasonEpisodeError('(error 02) Por favor configure los parametros de "season", "episode".')



    # Torrent Name!
    name = torrent_name

    # Login qBitTorrent
    qb = Client(qbtorrent_host)  # Nos conectamos al qBittorrent.
    qb.login(qbtorrent_user, qbtorrent_pass)  # Login.

    # Con el handler en sí, cada 10 s haremos una petición a qBitTorrent server para ver y manejar la descarga. De aquí solo sacaremos el hash de la descarga (por si la necesitamos), el estado actual y el path, que es donde se está descargando.

    # Esta sub función la usamos para obtener el estado del torrent. Esto lo sacamos en una función aparte, ya que, es lo que por separado, toca ejectutar constantemente para obtener SIEMRPE el estado del torrent.
    def get_state():
        my_hash = 'idk'
        state = 'idk'
        path = 'idk'
        name_torrent = 'idk'


        torrents_list = qb.torrents()

        # Vemos si el nombre proporcionado coincide con alguno de la lista actual del qBitTorrent.
        if len(torrents_list) == 0:
            print('No hay ningún torrent con ese nombre')
            exit()

        for download in torrents_list:

            # ¡Viendo un poco los torrents de diferentes descargas, algunas traen dobles espacios, ni puta idea de por qué, pero para solucionar eso básicmante eliminamos uno de esos espacios para que puedan coincidir perfectamente!
            if download['name'].replace('  ', ' ') != name:
                my_hash = download['hash']  # Extraemos el hash.
                state = download['state']  # Extraemos el estado actual.
                path = download['save_path']  # Extraemos la ruta de descarga.
                name_torrent = download['name']  # Extraemos el nombre del torrent.
                continue



            elif download['name'] != name:
                my_hash = download['hash']
                state = download['state']
                path = download['save_path']
                name_torrent = download['name']


            else:
                my_hash = download['hash']
                state = download['state']
                path = download['save_path']
                name_torrent = download['name']

            break

        return [state, path, my_hash, name_torrent]


    # Handler en sí.
    while True:
        handler_state = get_state()
        print(f'====================================\n Siguiendo: {handler_state[2]}')
        print(f' {handler_state[0]} \n====================================\n\n\n')
        
        base_route = handler_state[1]

        if base_route[-1] == '/' or base_route[-1] == '\\':
            base_route = base_route[:-1]



        # Acá es donde empezamos a manejar los archivos. ¡Con esto, ya verificamos que descargó y simplemente tenemos que idear una buena forma de detectar si es una serie o es una pelicula! (probablemente OMBI ayude)
        if handler_state[0] == 'stalledUP' or handler_state[0] is None or handler_state[0] == 'uploading':  # Esto quiere decir que está seedeando, terminó de descargar o está "subiendo".
            
            delete_torrent = qb.delete(handler_state[2])
            print(delete_torrent)


            # download_route = handler_state[1]  # ¡Ruta donde se descargó el torrent!
            folder_download = os.listdir(f'{base_route}/{handler_state[3]}')  # Lista de archivos de donde se descargó el torrent.
            
            
            


            delete_files = []

            for filec, fileff in enumerate(folder_download):  # Saco todos los archivos".html", solo saco esto porque estoy seguro de que aquí no hay nada más. No va a haber ningún otro archivo. Estos dos, serán acompañados por la carpeta donde estarán los archivos de video, en el caso de que se haya encontrado algo para descargar.
                if '.html' in fileff or '.txt' in fileff or '.url' in fileff:
                    delete_files.append(fileff)  # Sacamos eso de la lista. ¿Por qué? Luego lo usamos para mover los archivos, y no queremos que se muevan archivos basura.
                    # folder_download.pop(filec)

            # Con esto, eliminamos los archivos basura que no necesitamos.
            for file_to_delete in delete_files:
                os.remove(f'{base_route}/{handler_state[3]}/{file_to_delete}')


            # Creo una lista con SOLO los archivos "mkv"
            video_files = []
            new_folder_download = os.listdir(f'{base_route}/{handler_state[3]}')
            
            for video_file in folder_download:
                if '.mkv' in video_file or '.MKV' in video_file:
                    video_files.append(video_file)


            # Renombrando archivos!
            if len(video_files) == 1:
                if torrent_type == 'tv':
                    tv_name = f'{base_route}/{handler_state[3]}/{video_files[0]}'

                    new_tv_name_route = f'{route_moviesdb}/tv/{original_name}'
                    new_tv_name = f'{route_moviesdb}/tv/{original_name}/{season}{episode}.mkv'
                    
                    try:
                        os.mkdir(new_tv_name_route)

                    except:
                        pass


                    os.rename(tv_name, f'{base_route}/{handler_state[3]}/{season}{episode}.mkv')


                else:
                    movie_name = f'{base_route}/{handler_state[3]}/{video_files[0]}'
                    new_movie_name = f'{base_route}/movies/{original_name}.mkv'


                    os.rename(movie_name, f'{base_route}/{handler_state[3]}/{original_name}.mkv')




            # Creando carpetas necesarias!
            if route_moviesdb[-1] == '/' or route_moviesdb[-1] == '/':
                route_moviesdb = route_moviesdb[:-1]

                #f'{route_moviesdb}/{original_name} {season}{episode}'

            try:
                os.mkdir(f'{route_moviesdb}/tv')
                os.mkdir(f'{route_moviesdb}/movies')
            
            except:
                pass


            if torrent_type == 'tv':
                shutil.move(f'{base_route}/{handler_state[3]}/{season}{episode}.mkv', new_tv_name)

            else:
                shutil.move(f'{base_route}/movies/{original_name}.mkv', new_movie_name)

            

            print(f'Se ha hecho la descarga de {original_name}')
            break

            

        # ¡Para estar pendiente de los torrents, pero que no esté ejecutandoce siempre, lo ponemos a esperar un tiempo, para que luego vuelva a ver el estado!
        time.sleep(handler_time)
