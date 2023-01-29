from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# initializing app
app = Flask(__name__)
basedirectory = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedirectory, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize database
db = SQLAlchemy(app)

# initialize marshmallow
ma = Marshmallow(app)


class vendingMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machineName = db.Column(db.String(50), unique=True)
    machineLocation = db.Column(db.String(100))

    def __init__(self, machineName, machineLocation):
        self.machineName = machineName
        self.machineLocation = machineLocation


class vendingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'machineName', 'machineLocation')

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})


if __name__ == '__main__':
    app.run()
