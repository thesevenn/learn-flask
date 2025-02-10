import unittest
from main import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True  # Enable testing mode
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"name":"George"}', response.data)

    def test_notfound(self):
        response = self.client.get("/random-url")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
