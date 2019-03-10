from django.test import TestCase
# Import the models
from settle.models import Tag, User, Post, Comment
from settle.fields import ColourField


class TagTestCase(TestCase):
    def create_tag(self, t, c, gt, isP, sa):
        # Use this to mnake Tag objects
        return Tag.objects.create(text=t, colour=c, is_game_tag=gt,
                                  is_pending=isP, steamAppId=sa)

    def try_making_tag(self):
        # Make Tag with method
        tagTest = self.create_tag("test tag", "#FFFFFF", True, False, "")
        # Assert tagTest is a Tag object
        self.assertTrue(isinstance(tagTest, Tag))

    def test_tag_toString(self):
        # Make Tag with method
        tagTest = self.create_tag("test tag", "#FFFFFF", True, False, "")
        # Assert the toString method returns the title
        self.assertEqual(tagTest.__str__, tagTest.title)

    def test_max_length(self):
        # Make a tag with a large name
        # Should raise an error
        self.assertRaises(Exception, Tag, text="this is a long test string")

    def test_colour_field(self):
        # Try to set the colour using an invalid code
        self.asserRaises(
            Exception, Tag, colour="this isn't a valid colour code")


class UserTestCase(TestCase):
    print("Todo")


class PostTestCase(TestCase):
    print("Todo")


class CommentTestCase(TestCase):
    print("Todo")
