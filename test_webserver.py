
import cherrypy,os

cherrypy.config.update({'server.socket_host': '192.168.1.109',
                        'server.socket_port': 8080,
                       })


PATH = os.path.abspath(os.path.dirname(__file__))
class Root(object): pass

cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
            },
    })

cherrypy.quickstart()
