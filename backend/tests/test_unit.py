from flask import url_for
from flask_testing import TestCase
#from application.routes import backend
from flask import url_for


test_data={"id": 1,"name": "Test Location 1","myths": [
        {
            "id": 1,
            "name": "Heracles",
            "character": "Test character 1" ,
            "story": "spanishmmcvndfjvnf",
            "location_id": 1,
            "completed": False
        }
    ]
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
        db.session.add(Myth(name="Run unit tests", character="Run unit tests", story="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):

    def test_read_all_location(self):
        response = self.client.get(url_for('test_location', id=1)
        all_locations = { "location": [test_location]}
        self.assertEquals(all_location,response.json)
    
    def test_read_location(self):
        response = self.client.get(url_for('read_location', id=1))
        self.assertEquals(test_location, response.json)

    def test_read_all_myths(self):
        response = self.client.get(url_for('test_myths', id=1))
        all_myths = {"myts":[test_myth]}                  
        self.assertEquals(all_myths, response.json)
    
    def test_read_myth(self):
        response = self.client.get(url_for('read_myth', id=1))
        self.assertEquals(test_myth, response.json)
    

class TestCreate(TestBase):

    def test_create_location(self):
        response = self.client.post(url_for('create_location'), json={"name": "Testing create funtionality"}, follow_redirects=True)
        self.assertEquals(b"Location '{new_location.name}' added to database:Testing create funtionality", response.data)
        self.assertEquals(Location.query.get(2).description, "Testing create fuctionality")
   
    def test_create_myth(self):
        response = self.client.post(url_for('create_myth'), json={"name": "Testing create funtionality", "character": "Testing create funtionality", "story": "Testing create funtionality"}, follow_redirects=True)
        self.assertEquals(b"Myth '{new_myth.name}' added to database:Testing create funtionality", response.data)
        self.assertEquals(Myth.query.get(2).description, "Testing create fuctionality")
   

class Testupdate(TestBase):  
    def test_update_location(self):
        response = self.client.post(
            url_for('update_location', id=1),
            json={"name": "Testing update funtionality"}, follow_redirects=True)
            self.assertEquals(b"updated a location:{location.name}: Testing update funtionality", response.data)

def test_update_myth(self):
        response = self.client.post(url_for('update_myth', id=1),
        json={"name": "Testing create funtionality",
         "character": "Testing create funtionality",
         "story": "Testing create funtionality"}
        self.assertEquals(b" updated a myth:{myth.name}: Testing update funtionality", response.data)


class TestDelete(TestBase):

    def test_delete_location(self):
        response = self.client.get(url_for('delete_location', id=1),
        self.assertEquals(b"Deleted a location:{location.name}", response.data)
        self.assertNotIn(Location.query.get(1))
        
    def test_delete_myth(self):
        response = self.client.get(url_for('delete_myth', id=1)
        self.assertEquals(b"Deleted a myth:{location.name}", response.data)
        self.assertNotIn(Myth.query.get(1))
    
