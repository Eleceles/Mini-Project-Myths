from application import db

class Myth(db.Model):
    # __tablename__ = 'myths'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    character = db.Column(db.String(80), nullable=False)
    story = db.Column(db.String(250), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)


class Location(db.Model):
    # __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    myths = db.relationship('Myth', backref='location')
    
