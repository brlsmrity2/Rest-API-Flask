from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


app = Flask(__name__)
api = Api(app)

fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):
        return fakeDatabase
    
    def post(self):
        data = request.json
        itemId = len(fakeDatabase.keys())+1
        fakeDatabase[itemId]={"name": data["name"]}
        return fakeDatabase

class Item(Resource):
    def get(self, pk):
        return fakeDatabase[pk]   


    def put(self, pk):
        data = request.json
        fakeDatabase[pk]['name'] = data['name']
        return fakeDatabase
    
    def delete(self, pk):
        del fakeDatabase[pk]
        return fakeDatabase

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

if __name__ == "__main__":
    app.run(debug = True)