"""
Aplicação Web que retorna saudação dependendo do horário
"""
import cherrypy
import datetime


class Web(object):
    @cherrypy.expose()
    def index(self):
        tempo = datetime.datetime.now().time()

        if 5 <= int(tempo.hour) <= 12:
            saudacao = "Bom dia, "
        elif 12 < int(tempo.hour) < 18:
            saudacao = "Boa tarde, "
        else:
            saudacao = "Boa noite, "

        return str(saudacao + 'são {0}:{1}.'.format('%02d' % tempo.hour, '%02d' % tempo.minute))


cherrypy.config.update({'server.socket_port': 1256})
cherrypy.engine.restart()
cherrypy.quickstart(Web())
