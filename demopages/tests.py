from django.test import TestCase, Client


# Create your tests here.
class IndexTestCase(TestCase):
    def setUP(self):
        self.client = Client()

    def test_get_index_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hi, world")
