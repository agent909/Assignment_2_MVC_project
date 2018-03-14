from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/dbase'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

import model

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/incubators')
# def incubators():
#     return render_template('incubators.html')


if __name__=='__main__':
    app.run(debug=True)
