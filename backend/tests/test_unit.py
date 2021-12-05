from flask import url_for
from flask_testing import TestCase
#from application.routes import backend
from flask import url_for

test_myth = {
                "id" : 1,
                "name" : "name",
                "character" : "character",
                "story" : "story"
            }

test_get_all_myths = {
                "id" : 2,
                "name" : "name",
                "character" : "character",
                "story" : "story"
            }




class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
        
    def setUp(self):
        db.create_all()
        db.session.add(Myths(id = 1, name="name", character="character", story="story", location_id=1))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):

    def test_read_all_locations(self):
        response = self.client.get(url_for('test_location', id=1)
        alllocations = { "location": [test_read_all_locations]}
        self.assertEquals(all_locations,response.json)
    
    def test_read_location(self):
        response = self.client.get(url_for('read_location', id=1))
        self.assertEquals(test_location, response.json)

    def test_read_all_myths(self):
        response = self.client.get(url_for('test_myths'))
        allmyths = {"myts":[test_read_all_myths]}                  
        self.assertEquals(all_myths, response.json)
    
    def test_read_myth(self):
        response = self.client.get(url_for('read_myth', id=1))
        self.assertEquals(test_myth, response.json)
    

# class TestCreate(TestBase):

#     def test_create_location(self):
#         response = self.client.post(url_for('create_location'), json={"name": "Testing create funtionality"}, follow_redirects=True)
#         self.assertEquals(b"Location '{new_location.name}' added to database:Testing create funtionality", response.data)
#         self.assertEquals(Location.query.get(2).description, "Testing create fuctionality")
   
#     def test_create_myth(self):
#         response = self.client.post(url_for('create_myth'), json={"name": "Testing create funtionality", "character": "Testing create funtionality", "story": "Testing create funtionality"}, follow_redirects=True)
#         self.assertEquals(b"Myth '{new_myth.name}' added to database:Testing create funtionality", response.data)
#         self.assertEquals(Myth.query.get(2).description, "Testing create fuctionality")
   

# class Testupdate(TestBase):  
#     def test_update_location(self):
#         response = self.client.post(
#             url_for('update_location', id=1),
#             json={"name": "Testing update funtionality"}, follow_redirects=True)
#             self.assertEquals(b"updated a location:{location.name}: Testing update funtionality", response.data)

# def test_update_myth(self):
#         response = self.client.post(url_for('update_myth', id=1),
#         json={"name": "Testing create funtionality",
#          "character": "Testing create funtionality",
#          "story": "Testing create funtionality"}
#         self.assertEquals(b" updated a myth:{myth.name}: Testing update funtionality", response.data)


# class TestDelete(TestBase):

#     def test_delete_location(self):
#         response = self.client.get(url_for('delete_location', id=1),
#         self.assertEquals(b"Deleted a location:{location.name}", response.data)
#         self.assertNotIn(Location.query.get(1))
        
#     def test_delete_myth(self):
#         response = self.client.get(url_for('delete_myth', id=1)
#         self.assertEquals(b"Deleted a myth:{location.name}", response.data)
#         self.assertNotIn(Myth.query.get(1))
    
