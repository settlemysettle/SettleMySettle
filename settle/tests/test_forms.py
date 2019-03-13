from django.test import TestCase
# from settle.forms import ...
from settle.models import Tag, User, Post, Comment
from django.utils import timezone


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
        # Should raise issue when trying to login with a incorrect username
        with self.assertRaises(KeyError):
            LoginForm(
                user={'username': "wrongUsername", 'password': "testPassword123!"})


class Signup(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Duke", password="testPassword123!")

    def test_init(self):
        # Check it accepts a new user?
        SignupForm(user={'username': "newUsername",
                         'password': "testPassword123!"})

    def test_sign_up_without_text(self):
        # Shouldn't take this as a valid form?
        form = SignupForm()
        self.assertFalse(form.is_valid())

    def test_signup_exsisting_user(self):
        # should give an exception when trying to make an account with a username already taken
        with self.assertRaises(KeyError):
            SignupForm(self.user)

    def test_password_length_short(self):
        # Should give exception with very short password
        with self.assertRaises(KeyError):
            SignupForm(user={'username': "test", 'password': "abc"})

    def test_long_password_length(self):
        # Should raise exception with a very long password
        with self.assertRaises(KeyError):
            SignupForm(user={
                       'username': "test", 'password': "ThisPasswordIsFarToolongItsQuiteSillyActually"})

    def test_long_username_length(self):
        # Should raise exception with a very long password
        with self.assertRaises(KeyError):
            SignupForm(user={
                       'username': "thisisaverylongusername", 'password': "password"})


class UploadTestCase(TestCase):
    def setUp(self):
        self.author = User.objects(
            username="Duke", password="GoodBoy"
        )
        self.picture = "static/images/logoWAD.png"
        self.tag = Tag.objects.create(
            text="test", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        self.post = Post.objects.create(author=self.author, picture=self.picture,
                                        game_tag=self.tag, date_submitted=timezone.now(), description="description")

    def test_init(self):
        # Check it accepts a new post
        UploadForm(post=self.post)

    def test_empty(self):
        # Check it won't accept empty imput
        with self.assertRaises(KeyError):
            UploadForm()

    def check_it_must_have_game_tag(self):
        # Check it won't accept a post without a game_tag selected
        with self.assertRaises(KeyError):
            UploadForm(post={'author': self.author, 'picture': self.picture,
                             'date_submitted': timezone.now(), 'description': "description"})

    def check_it_must_have_a_picture_seleted(self):
        # Check it won't accept a post that doesn't contain an image
        with self.assertRaises(KeyError):
            UploadForm(post={'author': self.author, 'date_submitted': timezone.now(
            ), 'description': "description"})


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
