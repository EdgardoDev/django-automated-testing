from django.test import TestCase
from . models import Post

# We start by building some small tests

class ModelTest(TestCase):

    def setUp(self):
        self.djangoblog = Post.objects.create(title="Django Automated Testing", author="Edgardo", slug="django-automated-testing")
    
    def test_post_model(self):
        djangoblogtest = self.djangoblog
        self.assertTrue(isinstance(djangoblogtest, Post)) # If data goes into the db assert True.
        self.assertEqual(str(djangoblogtest), "Django Automated Testing")

