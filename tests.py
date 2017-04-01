import os
import unittest
import tempfile
from flask.ext.testing import TestCase
from project import app, db


class BaseTestCase(TestCase):

	def create_app(self):
    		app.config.from_object('config.TestConfig')
    		return app
	
	def setUp(self):
		db.create_all()
		db.session.add(BlogPost("Test post", "This is just a test."))
		db.session.add(User("admin", "adm@in.com", "admin"))
		db.session.commit()

class FlaskTestCase(unittest.TestCase):
#Ensure Flask was setup correctly
    def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()