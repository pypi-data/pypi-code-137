# Libraries
import feedparser
import requests
import os
import time

from qbittorrent import Client



def download(search: str, jacket_host: str, jacket_apiKey: str, qbtorrent_host: str, qbtorrent_user: str, qbtorrent_pass: str, download_path: str, max_size = 2000, low_discard = True):
    """
    Descarga los torrents de las peliculas con ayuda de este módulo.

    Params
    ====
    search: str | Nombre de la serie o película a buscar!

    jackett_host: str | El host dond está corriendo tu servidor de Jackett.

    jackett_apiKey: str | La API KEY de tu Jackett! La puedes encontrar arriba derecha de tú Jackett.

    qbtorrent_host: str | El host donde esta corriento tu qBitTorrent WEB.

    qbtorrent_user: str | Usuario admin en tu qBitTorrrent!

    qbtorrent_pass: str | Contraseña de tu usuario en tu qBitTorrent!

    max_size: int | Peso máximo (en MB) que podrán tener los archivos.

    low_discard: bool | Si desea que se descarte el contenido en 720p, active esto!

    download_path: str | Ruta donde se descargarán los archivos virgenes, sin haberlos procesado y renombrado, por tanto, no des la ruta defenitiva. RUTA ABSOLUTA!!!!
    """



    # Configuración inicial del string debúsqueda.
    busqueda = search.replace(' ', '+')
    
    # Configuraciones básicas. Es importante que, para empezar, se tiene que tener los trackers ya puestos en jackett.


    # A continuación extraigo la información de la serie (temporada y episodio) guiandome del formato SXXEXX que ya conociamos.
    serie_number_info = search.split(' ')[-1].upper()  # -1 porque,la temporada y episodio de la serie queda a lo último.


    parameters: str

    if 'S' in serie_number_info[0] and 'E' in serie_number_info[1:]:  # Desde acá, descartamos directamente el indice 0, ya que ya se validó y no lo necesitamos.

        # Extraemos el numero de temporada y episodio.
        season_number = serie_number_info[1:serie_number_info.find('E')]
        episode_number = serie_number_info[serie_number_info.find('E') + 1:]


        parameters = f'api/v2.0/indexers/all/results/torznab/api?apikey={jacket_apiKey}&cat=5000,5030,5040,5070,2000,2030,2040,2045,2070&t=search&q={busqueda[:busqueda.find(serie_number_info)]}&season={season_number}&ep={episode_number}'

        

    else:
        parameters = f'api/v2.0/indexers/all/results/torznab/api?apikey={jacket_apiKey}&t=search&q={busqueda}'
        
        

    # Validación de sí la url pasada contiene la típica "/" al fínal. Sí es así, se la eliminamos.
    if jacket_host[-1] == '/':
        url_consult = f'{jacket_host[:-1]}/{parameters}'  # ¡Url lista para consulta!

    else:
        url_consult = f'{jacket_host}/{parameters}'  # ¡Url lista para consulta!


    print(f'Haciendo la busqueda de {search}.')



    # Accediendo!
    feed = feedparser.parse(url_consult)  # Se lee el RSS. ¡Devuelve una lista de diccionarios con los resultados!
    # Rastreo el estado 404 por si se ingresa mal el host del jackett!
    if feed['status'] == 404:
        raise Exception('(JackettHostError, error 02) Hay un erorr con la url del Jackett. Revisala. Puede que se deba a que esté mal redactada, que no esté corriendo el servidor o que esté en otro puerto.')



    torrents = []  # Diccionario para guardar los torrents


    for torrent in feed['entries']:
        torrents.append([torrent['size'], torrent['link'], torrent['title']])

        

    max_size_bytes = max_size * 1000000


    torrents_definitive_list = []
    

    # TODO: si se prefiere que los torrents que contengan 720, comentar las siguientes lineas de código.
    for torrents_info_count, torrents_info in enumerate(torrents):
        # Sí el nombre del torrent no contiene "720" y, sí el peso del torrent no supera el ya pasado a la función como parametro:
        if low_discard == True:
            if '720' not in torrents_info[-1] and int(torrents_info[0]) <= max_size_bytes:
                torrents_definitive_list.append(torrents[torrents_info_count])

        else:
            if int(torrents_info[0]) <= max_size_bytes:
                torrents_definitive_list.append(torrents[torrents_info_count])


    if len(torrents_definitive_list) == 0:
        print('(NoContentError, error 01) No se ha podido obtener  ninguna pelicula/serie para tu búsqueda, puede que se deba a error en la busqueda, que sea demasiado nuevo el contenido o que la filtración por los parametros causó que no quedara nada.')


    # Ahora sí, descarga de los torrents en sí.

    try:
        f_torrent = torrents_definitive_list[0] # Tomamos el primero de la lista. Esto aún se puede barajar, y ver si lo totamos otro torrent por diferente razón. Recordar que por lo menos, el RSS del jackett no devuelve los seeders ni peers para obtener más metadata, por tanto, nos vemos por este lado restringidos.

        # Config torrents var's.
        torrent_link = f_torrent[1]
        torrent_size = f_torrent[0]
        torrent_name = f_torrent[2]
        


        try:
            # Conexión al servidor de qBitTorrent!
            global qb
            qb = Client(qbtorrent_host)



        # Excepción si la url pasa está mal.
        except requests.exceptions.ConnectionError:
            print('(qBitTorrentHostError, error 03) El link del host de qBitTorrent es erroneo. Puede que tu servidor esté corriendo sobre otro puerto, esté apagado o hayas escrito mal la URL. Revisalo!')
            exit()
        
        # Iniciamos sesión en qBitTorrent para empezar a usarlo.
        qbtorrent_login = qb.login(qbtorrent_user, qbtorrent_pass)
        # print(qbtorrent_login)
        


        # Manejo de contraseña/usuario incorrecto.
        if qbtorrent_login == 'Fails.':
            raise ValueError('(qBTorrentCredentialsError, error 04) Al parecer, las credenciales de tu qBitTorrent (usuario o contraseña) están mal. Como recordatorio: la contraseña por defecto del qBitTorrent es "adminadmin", y por otro lado, el usuario es "admin".')
        



        # TODO: Extraer información del torrent antes de descargarlo.

        # Descarga final del torrent!
        t_d = qb.download_from_link(torrent_link, savepath = download_path)  # Si la ruta está mal, directamente se descarga en descargas.
        print(f'\nLa descarga de {torrent_name} comenzó.')
        time.sleep(3)

        active_torrents = qb.torrents(sort = 'added_on')  # Devielve TODOS los torrents activos ordenados por orden de añadido!
        re_active = []  # Lista para rehacer la lista de los torrents activos.


        for at in active_torrents:
            re_active.append({'added_on': at['added_on'], 'hash': at['hash'], 'name': at['name']})
        

        active_torrents_sort = re_active[::-1]
        
        actual_torrent = active_torrents_sort[0]
        torrent_name = actual_torrent['name']

        

        return torrent_name




    except IndexError:
        pass

