from flask import Flask, render_template, request,redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
app = Flask(__name__)
app.secret_key="secret key"

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgresql@127.0.0.1/flaskcrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)

app.app_context().push()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    position=db.Column(db.String(100),nullable = False)
    office=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    __table_args__ = (
            CheckConstraint('age >= 1 AND age <= 99', name='check_age'),
        )
    startdate=db.Column(db.Date,nullable=False, server_default=db.func.current_date())
    salary=db.Column(db.Integer,nullable=False)

    def __init__(self,name,position,office,age,startdate,salary):
        self.name=name
        self.position=position
        self.office=office
        self.age=age
        self.startdate=startdate
        self.salary=salary





@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name = request.form['recipient-name']
        position = request.form['recipient-position']
        office = request.form['recipient-office']
        age = request.form['recipient-age']
        startdate = request.form['recipient-startdate']
        salary = request.form['recipient-salary']
        new_employee = Employee(name=name,position=position,office=office,age=age,startdate=startdate,salary=salary)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'GET':
        allemployees=Employee.query.all()
        return render_template('index.html',employees=allemployees)
    return redirect(url_for('index'))

@app.route('/edit/<int:id>',methods=['POST','DELETE'])
def edit(id):
    employee_edit=Employee.query.get(id)
    if request.method=='POST':
        employee_edit.name=request.form['name']
        employee_edit.position=request.form['position']
        employee_edit.office=request.form['office']
        employee_edit.age=request.form['age']
        employee_edit.startdate=request.form['startdate']
        employee_edit.salary=request.form['salary']
        db.session.commit()
        return redirect(url_for('index'))
    if request.method=='DELETE':
        print("delete request received")
        db.session.delete(employee_edit)
        db.session.commit()
        return jsonify({'status':200})
    return redirect(url_for(index))


if __name__=='__main__':
    # db.create_all()
    app.run(debug=True)
    
    

    



            






