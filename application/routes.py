from application import app, db
from application.forms import LocationForm, MythForm
from application.models import Myth, Location
from flask import render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap


@app.route('/')
@app.route('/home')
def home(): 
    all_location = Location.query.all()
    return render_template('index.html', title="Home", all_location=all_location)
    
@app.route('/create/myth', methods=['GET','POST'])
def create_myth():
    form = MythForm()
    locations = Location.query.all()
    for location in locations:
        form.location.choices.append((location.id,location.name))  
    if request.method=="POST":
        name=request.form['name']
        character=request.form['character']
        story=request.form['story']
        location_id=request.form['location']
        new_myth = Myth(name=name, character=character, story=story, location_id=location_id)
        db.session.add(new_myth)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_myth.html', title="Add a myth",  form=form)

@app.route('/read/myth')
def read_myth():
    all_myths = Myth.query.all()
    myths_dict = {"myths": []}
    for myth in all_myths:
        myths_dict["myths"].append({ "name": myth.name, "character": myth.character, "story": myth.story})
    return myths_dict
    return "read all myths"

@app.route('/update/myth')
def update_myth():
    form = MythForm()
    myth = Myth.query.get(id)
    if request.method == "POST": 
       myth.name = form.name.data
       myth.character = form.character.data
       myth.story = form.story.data
       db.session.commit()
       return redirect(url_for('home'))
    return render_template('update_myth.html', myth=myth, form=form)
 
@app.route('/delete/myth/<int:id>')
def delete_myth(id):
    myth = Myth.query.get(id)
    #db.session.delete('myth')
    db.session.commit()
    return redirect(url_for('home'))
    return render_template('update_myth.html', myth=myth, form=form)
    

@app.route('/create/location', methods=['GET', 'POST'])
def create_location():
    form = LocationForm()
    if request.method=="POST":
        name=request.form['name']
        new_location = Location(name=name)
        db.session.add(new_location)
        db.session.commit()  
        return redirect(url_for('home'))
    return render_template('create_location.html',title="Add a location", form=form)
        
    
@app.route('/read/location')
def read_location():
    all_locations = Location.query.all()
    locations_dict = {"locations": []}
    for location in all_locations:
        locations_dict["locations"].append({ "name": location.name,})
    return locations_dict
    return "read all location"


@app.route('/update/location',  methods=['GET','POST'])
def update_location():
    form = LocationForm()
    if request.method=="POST": 
       name = request.form["name"]
       db.session.commit()
       return redirect(url_for('home'))
    return render_template('update_location.html', form=form)


@app.route('/delete/location/<int:id>')
def delete_location(id):
    location = Location.query.get(id)
    #db.session.delete(location)
    db.session.commit()
    return redirect(url_for('home'))
    return render_template('update_location.html', form=form)