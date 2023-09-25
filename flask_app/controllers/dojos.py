from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    dojos = Dojo.get_all()
    # print(dojos)
    return render_template('create_dojo.html', dojos=dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojos():
    data = {
        "name": request.form['dojo_name']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/create_ninja')
def add_ninja():
    return render_template('index.html', all_dojos = Dojo.get_all_dojos())


@app.route('/dojos/<int:dojo_id>')
def show_details(dojo_id):
    data = {
        "id": dojo_id
    }
    
    return render_template('show.html')