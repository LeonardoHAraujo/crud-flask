# IMPORT DEPENDENCIES
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# INIT FLASK
app = Flask(__name__, static_folder = 'assets')

# CONFIG DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CLASS MODEL
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, unique=True, nullable=False)
    lastName = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

# ROUTES
@app.route('/')
def Index():
    persons = Person.query.all()
    return render_template('index.html', persons = persons)

@app.route('/create', methods = ['GET', 'POST'])
def Create():
    if request.method == 'POST':
        if request.form['first'] != '' and request.form['last'] != '':
            person = Person(request.form['first'], request.form['last'])
            db.session.add(person)
            db.session.commit()

            return redirect(url_for('Index'))
        else:
            return render_template('create.html', message = 'Preencha os dados!')

    return render_template('create.html')

@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def Edit(id):
    person = Person.query.get(id)

    if request.method == 'POST':
        if request.form['first'] != '' and request.form['last'] != '':
            person.firstName = request.form['first']
            person.lastName = request.form['last']

            db.session.commit()

            return redirect(url_for('Index'))
        else:
            return render_template('edit.html', person = person)

    return render_template('edit.html', person = person)

@app.route('/delete/<int:id>')
def Delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()

    return redirect(url_for('Index'))

# RUN APP
if __name__ == '__main__':
    db.create_all()
    app.run()
