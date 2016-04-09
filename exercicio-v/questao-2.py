"""
Função que formata uma lista de tuplas em tabela HTML
"""
import cherrypy


def tuplas_para_html(tuplas):
    cabecalho = tuplas[0]

    html = '<html>' \
           '<body>' \
           '  <table>' \
           '    <tr>' \
           '      <py-for="item in cabecalho">' \
           '        <th><py-eval="item"></th>' \
           '      </py-for>' \
           '    </tr>' \
           '    <py-for="linha in tuplas[1:]">' \
           '      <tr>' \
           '        <py-for="coluna in linha">' \
           '          <td><py-eval="coluna"></td>' \
           '        </py-for>' \
           '      </tr>' \
           '  </table>' \
           '</body>' \
           '</html>'
