from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:TaRa#31tasraj#1013@localhost:3306/contact_form'
db = SQLAlchemy(app)

# Define the database model
class ContactUsSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        comment = request.form['comment']

        # Create a new submission and add it to the database
        submission = ContactUsSubmission(email=email, subject=subject, comment=comment)
        db.session.add(submission)
        db.session.commit()

        return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create database tables
    app.run(debug=True)
