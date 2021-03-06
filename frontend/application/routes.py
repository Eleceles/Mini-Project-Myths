from application import app, db
from application.forms import LocationForm, MythForm
from flask import render_template, request, redirect, url_for, jsonify
import requests


backend_host = "mini-app_backend:5000"

@app.route('/', methods=["GET"])
def home(): 
    locations = requests.get(f"http://{backend_host}/get/allLocations").json()["locations"]
    app.logger.info(f"Locations: {locations}")
    return render_template("index.html", title="Home", locations=locations)


@app.route('/create/location', methods=['GET', 'POST'])
def create_location():
    form = LocationForm()
    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/location",
            json={"name": form.name.data})
        app.logger.info(f"Response: {response.text}")   
        return redirect(url_for('home'))
    return render_template('create_location.html', title="Add location", form=form)


@app.route('/create/myth', methods=['GET','POST'])
def create_myth():
    form = MythForm()

    json = requests.get(f"http://{backend_host}/get/allLocations").json()
    for location in json["locations"]:
        form.location.choices.append((location["id"], location["name"]))  

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/myth/{form.location.data}",
            json={
                "name": form.name.data, 
                "character": form.character.data, 
                "story": form.story.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))
    return render_template('create_myth.html', title="Add  Myth",  form=form)


# @app.route('/update/location/<int:id>',  methods=['GET','POST'])
# def update_location(id):
#     form = LocationForm()
#     location = requests.put(f"http://{backend_host}/read/location/{id}").json()
#     app.logger.info(f"Location: {location}")
#     if request.method=="POST": 
#        response = requests.post(f"http://{backend_host}/update/location/{id}",
#             json={"name": form.name.data})
#        return redirect(url_for('home'))
#     return render_template('update_location.html', location=location, form=form)

@app.route('/update/myth/<int:id>', methods=['GET','POST'])
def update_myth(id):
    form = MythForm()
    myth = requests.put(f"http://{backend_host}/read/myth/{id}").json()
    app.logger.info(f"Myth: {myth}")
    if request.method == "POST": 
       response = requests.put(f"http://{backend_host}/update/myth/{id}",
            json={"name": form.name.data, "character": form.character.data,"story": form.story.data})
       return redirect(url_for('home'))
    return render_template('update_myth.html', myth=myth, form=form)


# @app.route('/delete/location/<int:id>')
# def delete_location(id):
#     response = requests.delete(f"http://{backend_host}/delete/location/{id}")
#     app.logger.info(f"Response: {response.text}")
#     return redirect(url_for('home'))
    


@app.route('/delete/myth/<int:id>')
def delete_myth(id):
    response = requests.delete(f"http://{backend_host}/delete/myth/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))
    
           
