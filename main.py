from flask import Flask, request, jsonify


from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import sqlite3

app = Flask(__name__)
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)


def db_connection():
    conn = sqlite3.connect('todo.sqlite')
    return conn



@app.route('/view', methods=["GET","POST"])
@limiter.limit("10 per minute")
def get_data():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM todo")

        todos = [
            dict(id=row[0], title=row[1], description=row[2], done=row[3], priority=row[4])
            for row in cursor.fetchall()
        ]
        if todos is not None:
            return jsonify(todos)
        else:
            return "No todos found"
    
    if request.method == "POST":
        new_title = request.form["title"]
        new_description = request.form["description"]
        new_done = request.form["done"]
        new_priority = request.form["priority"]

        sql = """INSERT INTO todo (title,description,done,priority) VALUES (?,?,?,?)"""

        cursor = conn.execute(sql, (new_title, new_description, new_done, new_priority))
        conn.commit()
        return f"Todo with the id: {cursor.lastrowid} created successfully", 201

@app.route('/edit/<int:id>', methods=["GET","PUT","DELETE"])
@limiter.limit("10 per minute")
def update_todo(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM todo WHERE id=?", (id,))
        row = cursor.fetchall()
        for r in row:
            todos = r

        if todos is not None:
            return jsonify(todos), 200
        else:
            return "No todos found",404
        
    if request.method == "PUT":
        
        update_title = request.form["title"]
        update_description = request.form["description"]
        update_done = request.form["done"] 
        update_priority = request.form["priority"]

        if update_done == "True":
            sql = """DELETE FROM todo WHERE id=?"""
            conn.execute(sql, (id,))
            conn.commit()
            return "The todo with id: {} has been done so it was deleted.".format(id), 200
        else:
            sql = """UPDATE todo 
            SET title = ?,
            description = ?,
            done = ?,
            priority = ?
            WHERE id = ?"""


            update_todo = {
                "id":id,
                "title": update_title,
                "description": update_description,
                "done": update_done,
            }


            conn.execute(sql, (update_title, update_description, update_done, update_priority, id))
            conn.commit()
            return jsonify(update_todo)
    
    if request.method == "DELETE":
        sql = """DELETE FROM todo WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "The todo with id: {} has been deleted.".format(id), 200



@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)