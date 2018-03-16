from controller import db
from datetime import datetime


class Incubator(db.Model):
    __tablename__ = 'incubators'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, index=True, default='Incubator')
    rows = db.Column(db.Integer, nullable=False)
    columns = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    balot = db.Column(db.Integer, default=0)
    freska = db.Column(db.Integer, default=0)
    matra = db.Column(db.Integer, default=0)
    echo = db.Column(db.Integer, default=0)
    penoy = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Role %r>' % self.name


class Tray(db.Model):
    __tablename__ = 'trays'
    id = db.Column(db.Integer, primary_key=True)
    incubator_id = db.Column(db.Integer, db.ForeignKey('incubators.id'), nullable=False)
    incubator = db.relationship('Incubator', backref=db.backref('trays'))
    date_incubated = db.Column(db.DateTime, nullable=True)
    eggs_contained = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Role %r>' % self.id


class DailyHarvest(db.Model):
    __tablename__ = 'harvests'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    balot = db.Column(db.Integer, default=0)
    freska = db.Column(db.Integer, default=0)
    matra = db.Column(db.Integer, default=0)
    echo = db.Column(db.Integer, default=0)
    penoy = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Role %r>' % self.name


def add_incubator(form):
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


def get_incubators():
    my_incubators = Incubator.query.all()
    return my_incubators


def fetch_incubator(incubator_id):
    my_incubator = Incubator.query.filter_by(id=incubator_id).first()
    return my_incubator


def contain_eggs(tray_id, eggs):
    tray = Tray.query.filter_by(id=tray_id).first()
    tray.eggs_contained = eggs
    db.session.add(tray)
    db.session.commit()


def get_incubator_eggs(incubator_id):
    trays = Tray.query.filter_by(incubator_id=incubator_id).all()
    total_eggs = 0
    for x in trays:
        total_eggs += x.eggs_contained
    return total_eggs


db.create_all()
