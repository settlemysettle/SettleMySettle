from django.test import TestCase
# from settle.forms import ...
from settle.models import Tag, User, Post, Comment
from django.utils import timezone


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = {'username': "Duke", 'password': "testPassword123!"}

    def test_init(self):
        # LoginForm doesn't exist yet
        # Want to check it accepts a user
        form = LoginForm(user=self.user)
        assertTrue(form.is_valid())

    def test_login_without_user(self):
        # Shouldn't accept empty details
        form = LoginForm()
        self.assertFlase(form.is_valid())

    def test_wrong_password(self):
        # Shouldn't accept the wrong password
        form = LoginForm(
            user={'username': "Duke", 'password': "wrongPassword"})
        self.assertFalse(form.is_valid())

    def test_wrong_username(self):
        # Shouldn't accept wrong username
        form = LoginForm(
            user={'username': "wrongUsername", 'password': "testPassword123!"})
        self.assertFlase(form.is_valid())


class Signup(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="testPassword")
        self.user = {'username': "Duke", 'password': "testPassword123!"}

    def test_init(self):
        # Check it accepts a new user?
        form = SignupForm(
            user={'username': "newUsername", 'password': "testPassword123!"})
        self.assertTrue(form.is_valid())

    def test_sign_up_without_text(self):
        # Shouldn't take this as a valid form?
        form = SignupForm()
        self.assertFalse(form.is_valid())

    def test_signup_exsisting_user(self):
        # should give an exception when trying to make an account with a username already taken
        form = SignupForm(
            user={'username': "test", 'password': "testPassword"})
        self.asserFalse(form.is_valid())

    def test_password_length_short(self):
        # Shouldn't accept a very short password
        form = SignupForm(user={'username': "test", 'password': "abc"})
        self.assertFlase(form.is_valid())

    def test_long_password_length(self):
        # Shouldn't  accept a form with a very long password
        form = SignupForm(user={
            'username': "test", 'password': "ThisPasswordIsFarToolongItsQuiteSillyActually"})
        self.assertFlase(form.is_valid())

    def test_long_username_length(self):
        # Shouldn't accept a very long password
        form = SignupForm(
            user={'username': "thisisaverylongusername", 'password': "password"})
        self.assertFalse(form.is_valid())


class UploadTestCase(TestCase):
    def setUp(self):
        self.author = User.objects(
            username="Duke", password="GoodBoy"
        )
        self.picture = "static/images/logoWAD.png"
        self.tag = Tag.objects.create(
            text="test", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        self.post = {'author': self.author, 'picture': self.picture,
                     'game_tag': self.tag, 'date_submitted': timezone.now(), 'description': "description"}

    def test_init(self):
        # Check it accepts a new post
        form = UploadForm(post=self.post)
        assertTrue(form.is_valid())

    def test_empty(self):
        # Check it won't accept empty imput
        form = UploadForm()
        self.assertFalse(form.is_valid())

    def check_it_must_have_game_tag(self):
        # Check it won't accept a post without a game_tag selected
        form = UploadForm(post={'author': self.author, 'picture': self.picture,
                                'date_submitted': timezone.now(), 'description': "description"})
        self.assertFalse(form.is_valid())

    def check_it_must_have_a_picture_seleted(self):
        # Check it won't accept a post that doesn't contain an image
        form = UploadForm(post={'author': self.author, 'date_submitted': timezone.now(
        ), 'description': "description"})
        self.assertFalse(form.is_valid())


class NewtagTestCase(TestCase):
    def set_up(self):
        self.tag = {'text': "test", 'colour': "#FFFFFF",
                    'is_game_tag': True, 'is_pending': False, 'steamAppId': 222}
        # Make a tag
        self.existingTag = Tag.ojects.create(text="tagTest", colour="#FF2FFF",
                                             is_game_tag=True, is_pending=False, steamAppId=2221)

    def test_init(self):
        # Test it will accept a tag
        form = UploadTag(tag=self.tag)
        assertTrue(form.is_valid())

    def test_empty_tag(self):
        # An empty form won't be accepted
        form = UploadTag()
        self.assertFalse(form.is_valid())

    def test_existing_tag(self):
        # Shouldn't allow you to upload a tag that already exists
        form = UploadForm(tag=self.existingTag)

    def test_tag_without_game_name(self):
        # Shouldn't accept a tag without a game name
        form = UploadForm(form={
                          'colour': "#FFFFFF", 'is_game_tag': True, 'is_pending': False, 'steamAppId': 222})
        self.assertFalse(form.is_valid())
