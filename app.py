from flask import Flask, render_template, request, redirect
from models import db, Donor
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        donor = Donor(
            name=request.form['name'],
            blood_group=request.form['blood_group'],
            phone=request.form['phone'],
            location=request.form['location']
        )
        db.session.add(donor)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    donors = []
    if request.method == 'POST':
        bg = request.form['blood_group']
        donors = Donor.query.filter_by(blood_group=bg).all()
    return render_template('search.html', donors=donors)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)