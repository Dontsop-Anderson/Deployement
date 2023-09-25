from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja  import Ninja

@app.route('/create_ninja',methods=['POST'])
def create():
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojos_id']
    }
    Ninja.save(data)
    return redirect('/')


