
from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

# Model for Contact. creamos tabla contacto con sus columnas
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def serialize(self):  # para convertir objeto Contact en diccionario
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }
    
with app.app_context():
    db.create_all()  # crea las tablas en la base de datos

#crear rutas para la API RESTful
@app.route('/contacts', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if contact:
        return jsonify(contact.serialize()), 200
    else:
        return jsonify({'message': 'Contact not found'}), 404
contacts = []