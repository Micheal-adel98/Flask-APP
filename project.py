from flask import Flask,request,render_template,redirect,url_for
project = Flask(__name__)

todos = []
def get_id():
    id=1
    if len(todos)>0:
        id=todos[-1]['id'] + 1
    return id

@project.route('/')
def index():
    return render_template("index.html",todos=todos)

@project.route('/todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        todos.append({
            "id": get_id(),
            "title" : request.form.get('title'),
            "description" : request.form.get('description')
        })
        return redirect(url_for('index'))
    return render_template('todo_form.html')
@project.route("/todo/<int:id>",methods=["GET","POST"])
def get_todo(id):
    todo = list(filter(lambda todo: todo['id']==id,todos))
    if not todo:
        return "Not Found"
    return render_template("todo.html", todo=todo[0])

@project.route("/todo/<int:id>/edit",methods=["GET","POST"])
def edit_todo(id):
    todo = list(filter(lambda todo: todo['id']==id,todos))
    if not todo:
        return "Not Found"
    if request.method == "POST":
        todo[0]['title']=request.form.get('title')
        todo[0]['description']=request.form.get('description')
        return redirect(url_for('get_todo',id=id))
    return render_template("todo_form.html", todo=todo[0])
@project.route("/delete/<int:id>",methods=["GET"])
def delete_todo(id):
    todo = list(filter(lambda todo: todo['id']==id,todos))
    if not todo:
        return "Not Found"
    else:
        todos.pop(todo[0]['id']-1)
        return redirect(url_for('index'))
  
        

if __name__ == '__main__':
    project.run('127.0.0.1',"5800",debug=True)