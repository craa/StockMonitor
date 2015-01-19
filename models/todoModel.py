import web;

db = web.database(dbn='mysql', host='192.168.1.111', user='root', pw='', db='test')

def findAll():
    todos = db.select('todo', where='id=2')
    return todos
