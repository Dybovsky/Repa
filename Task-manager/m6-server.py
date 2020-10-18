## server.py
from bottle import route, run, static_file, view, redirect


class TodoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()


tasks_db = {
    1: TodoItem("прочитать книгу", 1),
    2: TodoItem("учиться жонглировать 30 минут", 2),
    3: TodoItem("помыть посуду", 3),
    4: TodoItem("поесть", 4),
}

###
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


@route("/")
@view("index")
def index():
    tasks = tasks_db.values()
    return {"tasks": tasks}


@route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return redirect("/")


@route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "Ok"


###
run(host="localhost", port=8080)