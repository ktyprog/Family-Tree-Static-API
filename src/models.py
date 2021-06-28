from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    parent = db.relationship('Person')


    def __repr__(self):
        return '<Person %s' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last name": self.last_name,
            "age": self.age,
            "parent_id": self.parent_id,
            # do not serialize the password, its a security breach
        }

# class Abuelo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(120))
#     apellido = db.Column(db.String(80))
#     edad = db.Column(db.Integer)

#     def __repr__(self):
#         return '<Abuelo %r>' % self.id
        
#     def serialize(self):
#         return {
#             "id": self.id,
#             "nombre": self.nombre,
#             "apellido": self.apellido,
#             "edad": self.edad,
            
#             # do not serialize the password, its a security breach
#         }

    
# class Padre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(120))
#     apellido = db.Column(db.String(80))
#     edad = db.Column(db.Integer)
#     abuelo_id = db.Column(db.Integer, db.ForeignKey('abuelo.id'))
#     abuelo = db.relationship('Abuelo')


#     def __repr__(self):
#         return '<Padre %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "nombre": self.nombre,
#             "apellido": self.apellido,
#             "edad": self.edad,
#             "abuelo_id": self.abuelo_id,
#             # do not serialize the password, its a security breach
#         }

# class Generacion_actual(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(120), unique=False, nullable=False)
#     apellido = db.Column(db.String(80), unique=False, nullable=False)
#     edad = db.Column(db.Integer)
#     padre_id = db.Column(db.Integer, db.ForeignKey('padre.id'))
#     padre = db.relationship('Padre')
#     def __repr__(self):
#         return '<Generacion_actual %r>' % self.nombre

#     def serialize(self):
#         return {
#             "id": self.id,
#             "nombre": self.nombre,
#             "apellido": self.apellido,
#             "edad": self.edad,
#             "padre_id": self.padre_id
#             # do not serialize the password, its a security breach
#         }