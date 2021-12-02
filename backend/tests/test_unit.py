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
        app.config.update(DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Myth(name="Run unit tests", character="Run unit tests", story="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):

    def test_read_all_myths(self):
        response = self.client.get(url_for('read_myths'))
        all_myths = {"myts":[test_myth]}                  
        self.assertEquals(all_myths, response.json)
    
    def test_read_myth(self):
        response = self.client.get(url_for('read_myth'))
        self.assertIn(b"Run unit tests", response.data)

    def test_read_home_location(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_read_location_dictionary(self):
        response = self.client.get(url_for('read_myth'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):
    def test_create_myth(self):
        response = self.client.post(url_for('create_myth'), data={"name": "Testing create funtionality", "character": "Testing create funtionality", "story": "Testing create funtionality"}, follow_redirects=True)
        self.assertIn(b"Testing create funtionality", response.data)
    
    def test_create_location(self):
        response = self.client.post(url_for('create_location'), data={"name": "Testing create funtionality"}, follow_redirects=True)
        self.assertIn(b"Testing create funtionality", response.data)

class Testupdate(TestBase):
    def test_update_myth(self):
        response = self.client.post(url_for('update_myth', id=1), data={"name": "Testing create funtionality", "character": "Testing create funtionality", "story": "Testing create funtionality"}, follow_redirects=True)
        self.assertIn(b"Testing update funtionality", response.data)
    
    def test_update_location(self):
        response = self.client.post(url_for('update_location', id=1), data={"name": "Testing create funtionality"}, follow_redirects=True)
        self.assertIn(b"Testing update funtionality", response.data)

class TestDelete(TestBase):
    def test_delete_myth(self):
        response = self.client.get(url_for('delete_myth', id=1), follow_redirects=True)
        self.assertNotIn(b"Run unit tests", response.data)
    
    def test_delete_location(self):
        response = self.client.get(url_for('delete_location', id=1), follow_redirects=True)
        self.assertNotIn(b"Run unit tests", response.data)

    
