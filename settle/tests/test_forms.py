from django.test import TestCase
from settle.forms import LoginForm, SignupForm, CommentForm, UploadForm, UploadTag
from settle.models import Tag, User, Post, Comment
from django.utils import timezone


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = {'username': "Duke", 'password': "testPassword123!"}

    def test_init(self):
        # LoginForm doesn't exist yet
        # Want to check it accepts a user
        form = LoginForm(self.user)
        self.assertTrue(form.is_valid())

    def test_login_without_user(self):
        # Shouldn't accept empty details
        form = LoginForm({})
        self.assertFalse(form.is_valid())


class Signup(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="testPassword")
        self.user = {'username': "Duke", 'password': "testPassword123!"}

    def test_init(self):
        # Check it accepts a new user
        form = SignupForm(self.user)
        self.assertTrue(form.is_valid())

    def test_sign_up_without_text(self):
        # Shouldn't take this as a valid form?
        form = SignupForm({})
        self.assertFalse(form.is_valid())


class UploadTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create(
            username="Duke", password="GoodBoy"
        )
        self.picture = "static/images/logoWAD.png"
        self.tag = Tag.objects.create(
            text="test", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        self.post = {'author': self.author, 'picture': self.picture,
                     'game_tag': self.tag, 'description': "description"}

    def test_init(self):
        # Check it accepts a new post
        form = UploadForm(self.post)
        self.assertTrue(form.is_valid())

    def test_empty(self):
        # Check it won't accept empty imput
        form = UploadForm({})
        self.assertFalse(form.is_valid())


class NewtagTestCase(TestCase):
    def setUp(self):
        self.tag = {'text': "test", 'colour': "#FFFFFF",
                    'is_game_tag': True, 'is_pending': False, 'steamAppId': 222}

    def test_init(self):
        # Test it will accept a tag
        form = UploadTag(self.tag)
        self.assertTrue(form.is_valid())

    def test_empty_tag(self):
        # An empty form won't be accepted
        form = UploadTag({})
        self.assertFalse(form.is_valid())


class CommentFormTestCase(TestCase):
    def setUp(self):
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)

        postTest = Post.objects.create(author=userTest, picture='static/images/logoWAS.png', game_tag=tagTest,
                                       date_submitted=timezone.now(), description="test")
        postTest.save()
        postTest.info_tags.add(tagTest)
        # Try to make a comment object
        self.comment = {'author': userTest, 'text': "This is a comment",
                        'linking_users': userTest, 'parent_post': postTest}

    def test_init(self):
        # Test it will accept a comment
        form = CommentForm(self.comment)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        # An empty form shouldn't be valid
        form = CommentForm({})
        self.assertFalse(form.is_valid())
