from bottle import route, run, view, static_file, redirect, request

class TodoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()

tasks_db = {
	1: TodoItem("read a book", 1),
	2: TodoItem("flairing", 2),
	3: TodoItem("wash dishes", 3),
	4: TodoItem("dinner", 4),
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

@route("/add-task", method="POST")
def add_task():
	desc = request.POST.description.strip()
	if len(desc) > 0:
		new_uid = max(tasks_db.keys()) + 1
		t = TodoItem(desc, new_uid)
		tasks_db[new_uid] = t
	return redirect("/")
###
run(host="localhost", port=8080, autoreload=True)