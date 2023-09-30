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


@app.route('/ninja/edit/<int:ninja_id>')
def edit_details(ninja_id):
    data = {
        "id": ninja_id
    }

    friend_details = Ninja.get_one(data)
    return render_template('edit.html', details=friend_details)

@app.route('/ninja/update', methods=['POST'])
def update_details():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.update(data)
    return redirect('/')

@app.route('/ninja/remove/<int:ninja_id>')
def delete(ninja_id):
    data = {
        'id': ninja_id
    }
    Ninja.remove(data)
    return redirect('/')

