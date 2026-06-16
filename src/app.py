from flask import Flask, render_template, request , redirect
from pymongo import MongoClient
import os
app=Flask(__name__, template_folder='../templates')
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client=MongoClient(mongo_url)
db=client['tododb']
todos=db['todos']

@app.route('/')
def index():
    all_todos = list(todos.find())
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_text = request.form.get('todo')
    if todo_text:
        todos.insert_one({'text': todo_text})
    return redirect('/')

@app.route('/delete/<todo_id>')
def delete_todo(todo_id):
    from bson.objectid import ObjectId
    todos.delete_one({'_id': ObjectId(todo_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

