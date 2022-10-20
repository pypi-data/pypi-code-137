from typing import Callable

import cherrypy
import ujson

from telebox.telegram_bot.types.types.update import Update
from telebox.telegram_bot.serializer import Serializer


class ServerRoot:

    def __init__(self, update_processor: Callable[[Update], None]):
        self._serializer = Serializer()
        self._update_processor = update_processor

    @cherrypy.expose
    def index(self) -> str:
        content_length = cherrypy.request.headers.get("Content-Length")

        if content_length is None:
            raise cherrypy.HTTPError(403)

        data = ujson.loads(cherrypy.request.body.read(int(content_length)))
        update = self._serializer.get_object(data=data, class_=Update)
        self._update_processor(update)

        return str()
