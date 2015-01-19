import web
from models import *

#route rules
urls = (
    '/', 'index'
)

#view renderer
render = web.template.render('templates/')

#main function
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

#utils , better pack into a module later
def getRender(obj):
    templatePath = 'templates/' + obj.__class__.__name__
    return web.template.render(templatePath)

#base controller
class Controller(object):
    def __init__(self):
	self.render = web.template.render('templates/' + self.__class__.__name__)

#web controller instance
class index(Controller):
    def GET(self):
	todos = todoModel.findAll()
	str = ''
	for todo in todos:
	    str = str + todo.title
#	str = getRender(self)
        return self.render.index(str)


