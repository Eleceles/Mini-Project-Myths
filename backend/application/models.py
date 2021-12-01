from application import db

class Myth(db.Model):
    __tablaname__ = 'myths'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    character = db.Column(db.String(80))
    story = db.Column(db.String(250))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    # def __init__(self, name, character, story):
    #     self.name = name
    #     self.character = character
    #     self.story = story


class Location(db.Model):
    __tablaname__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    myths = db.relationship("Myth")
