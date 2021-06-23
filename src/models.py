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

class GrandParents(db.Model):
    __tablename__ = 'grandparents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # parents_id = db.Column(db.Integer, db.ForeignKey('Parents_Relation.id'))
    childrens = db.relationship('Parents_Relation', backref='grandparents', lazy=True)
    

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "childrens": list(map(lambda x: x.serialize(), self.childrens))
            # do not serialize the password, its a security breach
        }

class Parents_Relation(db.Model):

    __tablename__ = 'parents_relation'
    id = db.Column(db.Integer, primary_key=True)
    parents_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    grand_parents_id = db.Column(db.Integer, db.ForeignKey('grandparents.id'))
    current_generation_id = db.Column(db.Integer, db.ForeignKey('current_generation.id'))


class Parents(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grand_parents = db.relationship('Parents_Relation', backref='parents', lazy=True)
    # current_generation = db.relationship('Parents_Relation', backref='parents', lazy=True)
    

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "grand_parents": list(map(lambda x: x.serialize(), self.grand_parents))
            # do not serialize the password, its a security breach
        }




class Current_Generation(db.Model):
    __tablename__ = 'current_generation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parents = db.relationship('Parents_Relation', backref='current_generation', lazy=True)

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "parents": list(map(lambda x: x.serialize(), self.parents))
            # do not serialize the password, its a security breach
        }