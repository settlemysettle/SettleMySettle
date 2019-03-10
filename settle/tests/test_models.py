from django.test import TestCase
# Import the models
from settle.models import Tag, User, Post, Comment
from settle.fields import ColourField
from django.utils import timezone


class TagTestCase(TestCase):
    def create_tag(self, t, c, gt, isP, sa):
        # Use this to make Tag objects
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

    def test_unique_tag(self):
        testTag = self.create_tag("DukeIsAGoodBoy", "#FFFFFF", True, False, "")
        # This should raise an error when we try to make a new one
        self.assertRaises(Exception, Tag, text="DukeIsAGoodBoy")


class UserTestCase(TestCase):
    def create_user(self, un, pa):
        # Make using the user model
        return User.objects.create(username=un, password=pa)

    def test_making_user(self):
        # Make a user using our method
        userTest = self.create_user("test", "password")
        # Check it is an instance of the User class
        self.asserTue(isinstance(userTest, User))

    def test_max_length_username(self):
        # make a test user with a username too long
        self.assertRaises(
            Exception, User, username="This is a very long username")

    def test_max_length_password(self):
        # Try to make a user with a very long password
        self.assertRaises(
            Exception, User, password="This password is far too long, you will never remember it")

    def test_unique_username(self):
        userTest = self.create_user("testUser", "password")
        # Should raise an issue as this is already a user
        self.assertRaises(Exception, User, username="testUser",
                          password="password")


class PostTestCase(TestCase):
    def create_post(self, a, p, gt, it, ds, pi, de):
        # Make a user object
        return Post.objects.create(author=a, picture=p, game_tag=gt, info_tags=it, date_submitted=ds, post_id=pi, description=de)

    def test_making_post(self):
        # Try to make a post object
        userTest = User.objects.create("test", "password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pendging=True, steamAppId="")
        # Try to make a new post
        postTest = self.create_post(
            userTest, 'static/images/logoWAS.png', tagTest, tagTest, timezone.now(), 2222, "description")


class CommentTestCase(TestCase):
    print("Todo")
