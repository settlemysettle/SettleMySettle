from django.test import TestCase
# from settle.forms import ...
from settle.models import Tag, User, Post, Comment


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Duke", password="testPassword123!")

    def test_init(self):
        # LoginForm doesn't exist yet
        # Want to check it accepts a user
        LoginForm(user=self.user)

    def test_login_without_user(self):
        # Should raise exception by trying to login without details
        with self.assertRaises(KeyError):
            LoginForm()

    def test_wrong_password(self):
        # Should raise exception when wrong password is given?
        with self.assertRaises(KeyError):
            LoginForm(user={'username': "Duke", 'password': "wrongPassword"})

    def test_wrong_username(self):
        # Should raise issue when trying to login with a very large username
        with self.asserRaises(KeyError):
            LoginForm(
                user={'username': "wrongUsername", 'password': "testPassword123!"})


class Signup(TestCase):
    print("Todo")


class UploadTestCase(TestCase):
    print("todo")


class NewtagTestCase(TestCase):
    print("Todo")

# Tag
    # def test_max_length(self):
    #     # Make a tag with a large name
    #     # Should raise an error
    #     self.assertRaises(Exception, Tag, text="this is a long test string")

    # def test_colour_field(self):
    #     # Try to set the colour using an invalid code
    #     self.assertRaises(
    #         Exception, Tag, colour="this isn't a valid colour code")

    # def test_unique_tag(self):
    #     testTag = self.create_tag(
    #         "DukeIsAGoodBoy", "#FFFFFF", True, False, 222)
    #     # This should raise an error when we try to make a new one
    #     self.assertRaises(Exception, Tag, text="DukeIsAGoodBoy")
# User
    # def test_max_length_username(self):
    #     # make a test user with a username too long
    #     self.assertRaises(
    #         Exception, User, username="This is a very long username")

    # def test_max_length_password(self):
    #     # Try to make a user with a very long password
    #     self.assertRaises(
    #         Exception, User, password="This password is far too long, you will never remember it")

    # def test_unique_username(self):
    #     userTest = self.create_user("testUser", "password")
    #     # Should raise an issue as this is already a user
    #     self.assertRaises(Exception, User, username="testUser",
    #                       password="password")
