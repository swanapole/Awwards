from django.test import TestCase
from .models import categories,technologies,colors,countries
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class categoriesTestClass(TestCase):
    def setUp(self):
        self.Art = categories(categories='Art')

    def test_instance(self):
        self.assertTrue(isinstance(self.Art,categories))

    def tearDown(self):
        categories.objects.all().delete()
     def test_save_method(self):
        self.Art.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Art.delete_category('Art')
        category = categories.objects.all()
        self.assertTrue(len(category)==0)
