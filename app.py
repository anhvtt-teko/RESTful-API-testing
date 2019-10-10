from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        data = todos.get(todo_id, "")
        if data == "":
            return {"response": "not exist"}, 201
        else:
            return {"response": "success",
                    "key": todo_id,
                    "value": todos[todo_id]}, 200

    def put(self, todo_id):
        data = todos.get(todo_id, "")
        if data != "":
            return {"response": "already exist"}, 201
        todos[todo_id] = request.form['data']
        return {"response": "added successfully"}, 200


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)