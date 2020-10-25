from bottle import route, run, view, static_file, redirect, request
from db import TodoItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
s = Session()


@route("/static/<filename:path>")
def send_static(filename):
	return static_file(filename, root="static")


@route("/")
@view("index")
def index():
	tasks = s.query(TodoItem).order_by(TodoItem.uid)
	total_tasks = s.query(TodoItem).count()
	incomplete = s.query(TodoItem).filter(TodoItem.is_completed == False).count()
	complete = total_tasks - incomplete
	# s.commit()
	return {"tasks": tasks,
	"total_tasks": total_tasks,
	"incomplete": incomplete,
	"complete" : complete}

@route("/api/delete/<uid:int>")
def api_delete(uid):
	s.query(TodoItem).filter(TodoItem.uid == uid).delete()
	s.commit()
	return redirect("/")

@route("/api/complete/<uid:int>")
def api_complete(uid):
	t = s.query(TodoItem).filter(TodoItem.uid == uid).first()
	s.commit()
	t.is_completed = True
	return "OK"

@route("/add-task", method="POST")
def add_task():
	desc = request.POST.description.strip()
	if len(desc) > 0:
		t = TodoItem(desc)
		s.add(t)
		s.commit()
	return redirect("/")


###
run(host="localhost", port=8080, autoreload=True)