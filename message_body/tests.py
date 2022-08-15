from django.test import TestCase

# Create your tests here.
from .models import MessagePost

class MessageModelTest(TestCase):
    def setUp(self):
        MessagePost.objects.create(text='just a text')


    def test_text_content(self):
        post = MessagePost.objects.get(id=1)
        expected_object_name = post.text
        self.assertEqual(expected_object_name, 'just a text')

class HomepageTest(TestCase):
    def setup(self):
        MessagePost.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reversed('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reversed('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')