from controller import db
from datetime import datetime


class Incubator(db.Model):
    __tablename__ = 'incubators'
    id = db.Column(db.Integer, primary_key = True)
    # tray_id= db.relationship('Tray', backref='incubator')
    name = db.Column(db.String(30), unique=False, index=True, default='Incubator')
    rows = db.Column(db.Integer, nullable=False)
    columns = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    balot = db.Column(db.Integer, default = 0)
    freska = db.Column(db.Integer, default = 0)
    matra = db.Column(db.Integer, default = 0)
    echo = db.Column(db.Integer, default = 0)
    penoy = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return '<Role %r>' %self.name

class Tray(db.Model):
    __tablename__ = 'trays'
    id = db.Column(db.Integer, primary_key=True)
    incubator_id = db.Column(db.Integer, db.ForeignKey('incubators.id'), nullable=False)
    incubator = db.relationship('Incubator', backref=db.backref('trays'))
    date_incubated = db.Column(db.DateTime, nullable=True)
    eggs_contained = db.Column(db.Integer, nullable=False, default=0)
    # incubator_id = db.Column(db.Integer, db.ForeignKey('incubators.id'))

    def __repr__(self):
        return '<Role %r>' %self.id

class Daily_Harvest(db.Model):
    __tablename__ = 'harvests'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    balot = db.Column(db.Integer, default = 0)
    freska = db.Column(db.Integer, default = 0)
    matra = db.Column(db.Integer, default = 0)
    echo = db.Column(db.Integer, default = 0)
    penoy = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return '<Role %r>' %self.name

def AddIncubator(form):
    try:
        new_incubator = Incubator(name=form.name.data, rows=form.rows.data, columns=form.columns.data)
        for x in range(form.rows.data*form.columns.data):
            tray = Tray()
            new_incubator.trays.append(tray)
        db.session.add(new_incubator)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def GetIncubators():
    my_incubators = Incubator.query.all()
    return(my_incubators)

def FetchIncubator(id):
    my_incubator = Incubator.query.filter_by(id).first()
    return my_incubator


db.create_all()

# FetchIncubator()
