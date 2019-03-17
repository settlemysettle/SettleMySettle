from django.test import TestCase
from settle.forms import SignupForm, CommentForm, UploadForm, SuggestTag
from settle.models import Tag, User, Post, Comment
from django.utils import timezone


class Signup(TestCase):
    def setUp(self):
        # Make a user that has already signed up
        u = User.objects.create(username="test", password="testPassword")
        u.save()
        # A user we will try to create
        self.user = {'email': "testemail@test.com",
                     'username': "Duke", 'password': "testPassword123!",
                     'confirm_password': "testPassword123!"}

    def test_init(self):
        # Check it accepts a new user
        form = SignupForm(self.user)
        self.assertTrue(form.is_valid())

    def test_sign_up_without_text(self):
        # Shouldn't take this as a valid form
        form = SignupForm({})
        self.assertFalse(form.is_valid())

    def test_signup_existing_user(self):
        # Shouldn't allow an existing user to signup
        form = SignupForm({'username': "test", 'password': "testPassword"})
        self.assertFalse(form.is_valid())

    def test_incorrect_email(self):
        # Shouldn't accept an incorrect email
        form = SignupForm({'email': "wrongEmail", 'username': "Duke", 'password': "testPassword123!",
                           'confirm_password': "testPassword123!"})
        self.assertFalse(form.is_valid())

    def test_different_passwords(self):
        # Shoudn't accept the data if the passwords are different
        form = SignupForm({'email': "testemail@test.com", 'username': "Duke", 'password': "testPassword123!",
                           'confirm_password': "wrongPassword"})
        self.assertFalse(form.is_valid())


class NewtagTestCase(TestCase):
    def setUp(self):
        # The tag we will try to upload
        self.tag = {'text': "test", 'colour': "#FFFFFF",
                    'is_game_tag': True, 'is_pending': False, 'steamAppId': 222}
        # Make a tag object that we won't be apply to suggest again
        t = Tag.objects.create(text="Civ 6", colour="#FFFFFF",
                               is_game_tag=True, is_pending=False, steamAppId=222)
        t.save()

    def test_init(self):
        # Test it will accept a tag
        form = SuggestTag(self.tag)
        self.assertTrue(form.is_valid())

    def test_empty_tag(self):
        # An empty form won't be accepted
        form = SuggestTag({})
        self.assertFalse(form.is_valid())

    def test_suggest_existing_tag(self):
        # Try to suggest a tag that already exists
        form = SuggestTag({'text': "Civ 6", 'colour': "#FFFFFF",
                           'is_game_tag': True, 'is_pending': False, 'steamAppId': 222})


class CommentFormTestCase(TestCase):
    def setUp(self):
        # Need a user, tag and post in order to comment
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)

        postTest = Post.objects.create(author=userTest, picture='static/images/logoWAS.png', game_tag=tagTest,
                                       date_submitted=timezone.now(), description="test")
        postTest.save()
        postTest.info_tags.add(tagTest)
        # The request we will send to try and make a comment
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
