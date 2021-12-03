from application import app, db
from application.models import Myth, Location
from flask import render_template, request, redirect, url_for, jsonify 
  
@app.route('/create/location/<int:id>', methods=['POST'])
def create_location():
        json = request.json
        new_location = Location(name = json["name"])
        db.session.add(new_location)
        db.session.commit()  
        return f"Location '{new_location.name}' added to database"

@app.route('/create/myth/<int:id>', methods=['POST'])
def create_myth():
        package = request.json()
        new_myth = Myth(name = package["name"], character = package["character"], story = package["story"], location_id=location_id)
        db.session.add(new_myth)
        db.session.commit()
        return f"Myth '{new_myth.name}' added to database"

@app.route('/get/allLocations', methods=["GET"])
def get_all_locations():
    all_locations = Location.query.all()
    json = {"locations": []}
    for location in all_locations:
        myths = []
        for myth in location.myths:
            myths.append({"id": myth.id,"name": myth.name, "character": myth.character, "story": myth.story, "location_id": myth.location_id})
        json["locations"].append({ "id": location.id, "name": location.name, "myths": myths})
    
    return jsonify(json)


@app.route('/read/allMyths', methods=["GET"])
def read_allmyths():
    all_myths = Myths.query.all()
    json = {"myths": []}
    for myth in all_myths:
        json["myth"].append({"id": myth.id, "name": myth.name,  "character": myth.character, "story": myth.character})
    return jsonify(json)

# @app.route('/read/location/<int:id>/myths', methods=["GET"])
# def read_myths(id):
#     myths = Location.query.get(id).myths
#     json = {"myths": []}
#     for myth in myths:
#         json["myths"].append({"id": myth.id,"name": myth.name,
#         "location_id": myth.location_id,"character": myth.character,
#         "story": myth.story})
#     return jsonify(json)   

@app.route('/read/myth/<int:id>', methods=["GET"])
def read_myth(id):
    myth = Myths.query.get(id)
    json = ["myths"].append({"id": myth.id,"name": myth.name,
        "location_id": myth.location_id,"character": myth.character,
        "story": myth.story})
    return jsonify(json)   


        
@app.route('/update/location/<int:id>',  methods=['GET','POST'])
def update_location(id):
    package = request.json
    location = Location.query.get(id)
    location.name = package["name"]
    db.session.commit()
    return f"updated a location:{location.name}"
    

# @app.route('/update/myth/<int:id>', methods=["POST"])
# def update_myth(id):
#     package = reaquest.json
#     myth = Myth.query.get(id)
#     myth.name = form.name.data
#     myth.character = form.character.data
#     myth.story = form.story.data
#     db.session.commit()
#     return f"updated a myth:{myth.name}"
    

@app.route('/delete/location/<int:id>')
def delete_location(id):
    location = Location.query.get(id)
    db.session.delete(location)
    return f"Deleted a location:{location.name}"

# @app.route('/delete/myth/<int:id>')
# def delete_myth(id):
#     myth = Myth.query.get(id)
#     db.session.delete('myth')
#     return f"Deleted a myth:{myth.name}"