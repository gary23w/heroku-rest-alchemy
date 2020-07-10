from db import db

class StuffModel(db.Model):
    __tablename__ = 'stuff'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    stuff = db.Column(db.String(80))

    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff

    def json(self):
        return {'name': self.name, 'stuff': self.stuff}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
