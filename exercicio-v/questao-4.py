"""
Aplicação Web que carrega uma expressão Python
e retorna seu resultado
"""
import cherrypy


class Web(object):
    @cherrypy.expose()
    def index(self):
        html = '<html>' \
               '<body>' \
               '<form method="post" action="/result">' \
               '  <input type="text" name="expressao" /><br>' \
               '  <input type="submit" />' \
               '</form>' \
               '</body>' \
               '</html>'

        return html

    @cherrypy.expose()
    def result(self, **args):
        expressao = str(args['expressao'])
        resultado = str(eval(expressao))

        return 'A expressão {0} retornou o seguinte resultado => {1}'.format(expressao, resultado)


cherrypy.config.update({'server.socket_port': 1256})
cherrypy.engine.restart()
cherrypy.quickstart(Web())
