from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/dbase'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

import model

@app.route('/')
def index():
    return '<h1>My Home Page</h1>', 404


if __name__=='__main__':
    app.run(debug=True)
