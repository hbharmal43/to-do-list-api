from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import random
app = Flask(__name__)
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)

app.config['SECRET_KEY'] = '_QkO3BwHfth7N1hz'
#Declare a todo item class. The class should have its properties and methods as required.
class Todo:
    def __init__(self,id:int, title: str,description: str,priority: int,status: bool) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    
    def in_dict(self):
        return{
            "id":self.id,
            "title": self.title,
            "description" :self.description,
            "priority" : self.priority,
            "status" : self.status
        }

# Create a todo hashmap with key as the todoId and value as the toDo class
todo_list = {
    0: Todo(0, "Wash Clothes", "Wash the laundry", 3, False),
    1: Todo(1, "Buy Groceries", "Purchase groceries for the week", 4, False),
    2: Todo(2, "Study for Exam", "Prepare for the upcoming math exam", 5, False),
    3: Todo(3, "Walk the Dog", "Take the dog for a walk in the park", 2, False)
}
keys_list = list(todo_list.keys())
# Create a GET /todos endpoint to retrieve all todos
@app.route("/todos",methods = ["GET"])
@limiter.limit("10 per minute")
def get_data():
    completed_list = []
    pending_list = []
    for todos in todo_list.values():
            if todos.status == False:
                pending_list.append(todos.in_dict())
            else:
                completed_list.append(todos.in_dict())
                
    return jsonify({
        "Incomplete todos" : pending_list, 
        "complete To-Dos" : completed_list
    })

# Create a GET /todos/<id> endpoint to retrieve a todo with specific id
@app.route("/todos/<id>",methods = ["GET"])
@limiter.limit("10 per minute")
def get_data_id(id):
    if id != keys_list:
        return("id does not exist Error: 404"), 404
    id = int(id)
    return jsonify([todo_list[id].in_dict()]) 

# Create a POST /todo endpoint to create new a todo
@app.route("/todo", methods = ["POST"])
@limiter.limit("10 per minute")
def input_data():
    data = request.get_json()
    random_int = random.randint(4,100)
    todo_list[random_int]= Todo(random_int,data["title"],data["description"],data["priority"],False)
    return jsonify(todo_list[random_int].in_dict())

    # return jsonify(str(len(todo_list)))
# Create a PUT /todo/<id> endpoint to update a todo for a specific id
@app.route("/todo/<id>",methods = ["PUT"])
@limiter.limit("10 per minute")
def update_todo(id):
    if id != keys_list:
        return("id does not exist Error: 404"), 404    
    id = int(id)
    data = request.get_json()
    todo_list[id] = Todo(id,data["title"],data["description"],data["priority"],data["status"])
    return jsonify([todo_list[id].in_dict()])


# Create a DELETE /todo/<id> endpoint to delete a todo item with specific endpoint
@app.route("/todo/<id>",methods = ["DELETE"])
@limiter.limit("10 per minute")
def delete_todo(id):
    if id != keys_list:
        return("id does not exist Error: 404"), 404
    id = int(id)
    del todo_list[id]
    return jsonify(str(id) +" is deleted")
    

# Create a PUT /todo/<id>/complete to set a todo item to complete with a specific id
@app.route("/todo/<id>/complete",methods = ["PUT"])
@limiter.limit("10 per minute")
def complete_todo(id):
    if id != keys_list:
        return("id does not exist Error: 404"), 404
    id = int(id)
    data = request.get_json()
    todo_list[id] = Todo(id,data["title"],data["description"],data["priority"],True)
    return jsonify("Todo with "+str(id)+" is completed")






# todos = [
#     {
#         "id": 1,
#         "title": "Complete Assignment",
#         "description": "Finish the math assignment before the deadline.",
#         "priority": "high",
#         "marked": False
#     },
#     {
#         "id": 2,
#         "title": "Grocery Shopping",
#         "description": "Buy milk, eggs, bread, and vegetables.",
#         "priority": "medium",
#         "marked": False
#     },
#     {
#         "id": 3,
#         "title": "Workout",
#         "description": "Do a 30-minute cardio session and strength training.",
#         "priority": "low",
#         "marked": False
#     },
#     {
#         "id": 4,
#         "title": "Read a Book",
#         "description": "Read two chapters of 'Atomic Habits'.",
#         "priority": "medium",
#         "marked": False
#     },
#     {
#         "id": 5,
#         "title": "Plan Weekend Trip",
#         "description": "Decide on a destination and book tickets for the weekend trip.",
#         "priority": "high",
#         "marked": False
#     }
# ]


# app = Flask(__name__)
# limiter = Limiter(key_func=get_remote_address)
# limiter.init_app(app)


# @app.route("/todos", methods=["POST"])
# @limiter.limit("10 per minute")
# def create_data():
#     data = request.get_json()

#     todos.append(
#         {
#             "id": len(todos),
#             "title": data["title"],
#             "description": data["description"],
#             "marked": False,
#             "priority": data["priority"],
#         }
#     )
#     return jsonify(todos)


# @app.route("/todos", methods=["GET"])
# @limiter.limit("10 per minute")
# def get_data():
#     return jsonify(todos)


# @app.route("/todos/<int:id>", methods=["GET", "PUT", "DELETE"])
# @limiter.limit("10 per minute")
# def update_todos(id):

#     if request.method == "GET":
#         for i in todos:
#             i["id"] == id
#             return jsonify(i)

#     if request.method == "PUT":
#         data = request.get_json()
        
#         if data["title"]:
#             todos[id]["title"] = data["title"]
#         if
#             continue
#         todos[id]["description"]: data["description"]
#         todos[id]["marked"]: data["marked"]
#         todos[id]["priority"]: data["priority"]

#     # if request.method == "DELETE":

# # 
# @app.route("/")
# def hello_world():
#     return "Hello World!"

# #generate a secret key / register

# #verify the key / login


if __name__ == "__main__":
    app.run(debug=True)
