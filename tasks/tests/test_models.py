from django.test import TestCase
from tasks.models import Tag


class ModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test_name")
        self.assertEqual(str(tag), tag.name)

