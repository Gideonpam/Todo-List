from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

todoData =[]

@app.route('/')
def index():
    return render_template("index.html", todos=todoData)

@app.route('/create_todo', methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo")
    todoData.append(new_todo)
    return redirect(url_for("index"))

@app.route("/delete-todo/<todo_item>")
def delete(todo_item):
    todoData.remove(todo_item)

    return redirect(url_for("index"))

#for update
index_to_update=''
@app.route('/update_item-todo/<todo_item>', methods = ['GET', 'POST'])
def update(todo_item):
    index = todoData.index(todo_item)

    global index_to_update
    index_to_update = index
    return render_template('update.html', todo_item= todo_item)

@app.route('/update_item', methods = ['POST'])
def update_item():
    if request.method == 'POST':
        new_item = request.form.get('new_item')
        todoData[index_to_update] = new_item

        return redirect(url_for('index'))

if __name__== "__main__":
    app.run(debug=True)