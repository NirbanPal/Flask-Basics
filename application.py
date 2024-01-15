from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
app = Flask(__name__)
app.secret_key="secret key"

app.config['SQLALCHEMY_DATABASE_URI']="postgresurl"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    position=db.Column(db.String(100),nullable = False)
    office=db.Column(db.String(100),nullable=False)
    age=db.column(db.Integer,nullable=False)
    __table_args__ = (
            CheckConstraint('age >= 1 AND age <= 99', name='check_age'),
        )
    startdate=db.column(db.Date,nullable=False, server_default=db.func.current_date())
    salary=db.column(db.Integer,nullable=False)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        
        return redirect(url_for(index))
    if request.method == 'GET':
        allemployees=db.Query.all()
        return render_template('index.html',employees=allemployees)
    return redirect(url_for(index))

@app.route('/edit',methods=['POST'])
def edit(id):
    if request.method=='POST':
        pass
    
    

    



            






