from application import app
from flask import url_for
from flask_testing import TestCase
from application.routs import backend_host
import requst_mock

test_data={"id": 1,
    "name": "Test Location 1"
    "myths": [
        {
            "id": 1,
            "name": "Test Location 1",
            "character": god,
            "story": "kdjfdjd",
            "location_id": 1
        }
    ]
}



class TestBase(TestCase):

     def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

class TestViews(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend}/get/allLocations", json={'locations': []})
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_create_location(self):
        response = self.client.get(url_for('create_location'))
        self.assert200(response)

class TestRead(TestBase):

    def test_home_read_locations(self):
        with requests_mock.Mocker() as m:
                m.get(f"http://{backend}/get/allLocations", json={'locations': [test_data]})
                response = self.client.get(url_for('home'))
                self.assertIn("Test Location 1", response.data.decode("utf-8"))
    
    def test_home_read_myths(self):
        with requests_mock.Mocker() as m:
                m.get(f"http://{backend}/get/allMyths", json={'myths': [test_data]})
                response = self.client.get(url_for('home'))
                self.assertIn("Test Myth 1", response.data.decode("utf-8"))

class TestCreate(TestBase):
    def test_create_location_form_post(self):
        with requests_mock.Mocker() as m:
                m.post(f"http://{backend}/create/location", text="Test response")
                m.get(f"http://{backend}/get/allLocations", json={'location': [test_data]})
                response = self.client.post(url_for('create_location'), follow_redirects=True)
                self.assertIn("Test Location 1", response.data.decode("utf-8"))

    def test_create_myth_form_post(self):
        with requests_mock.Mocker() as m:
                m.post(f"http://{backend}/create/myth", text="Test response")
                m.get(f"http://{backend}/get/allMyths", json={'myth': [test_data]})
                response = self.client.post(url_for('create_myth'), follow_redirects=True)
                self.assertIn("Test Myth 1", response.data.decode("utf-8"))


class Testupdate(TestBase):
    def test_update_location(self):
            with requests_mock.Mocker() as m:
                    m.post(f"http://{backend}/update/location", text="Test response")
                    m.get(f"http://{backend}/get/allLocations", json={'location': [test_data]})
                    response = self.client.post(url_for('update_location'), follow_redirects=True)
                    self.assertIn("Test Location 1", response.data.decode("utf-8"))
   
   
   
   
    def test_update_myth(self):
        with requests_mock.Mocker() as m:
                m.post(f"http://{backend}/update/myth", text="Test response")
                m.get(f"http://{backend}/get/allMyths", json={'myth': [test_data]})
                response = self.client.post(url_for('update_myth'), follow_redirects=True)
                self.assertIn("Test Myth 1", response.data.decode("utf-8"))



class TestDelete(TestBase):
    def test_update_myth(self):
        with requests_mock.Mocker() as m:
                m.post(f"http://{backend}/delete/myth", text="Test response")
                m.get(f"http://{backend}/get/allMyths", json={'myth': [test_data]})
                response = self.client.post(url_for('update_myth'), follow_redirects=True)
                self.assertIn("Test Myth 1", response.data.decode("utf-8"))

    
    def test_delete_location(self):
        with requests_mock.Mocker() as m:
                m.post(f"http://{backend}/delete/location", text="Test response")
                m.get(f"http://{backend}/get/allMyths", json={'myth': [test_data]})
                response = self.client.post(url_for('update_myth'), follow_redirects=True)
                self.assertIn("Test Myth 1", response.data.decode("utf-8"))
            
