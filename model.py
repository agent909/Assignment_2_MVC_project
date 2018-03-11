from index import db
from datetime import datetime


class Tray(db.Model):
    __tablename__ = 'trays'
    id = db.Column(db.Integer, primary_key=True)
    date_incubated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    eggs_contained = db.Column(db.Integer)

    def __repr__(self):
        return '<Role %r>' %self.id

db.create_all()
