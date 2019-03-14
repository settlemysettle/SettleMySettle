from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from settle.models import User, Tag


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_context_dict(self):
        response = self.client.get(reverse('index'))
        # The context_dict should contain a list of images it will display to the page
        posts = response.context[-1]['pictures']
        # Should return 6 images
        self.assertTrue(len(posts) == 6)


class feedViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Get a tag object that we will add to the fav games of our new user
        self.tag = Tag.objects.get(text="Civ 6")
        # Make a new user
        self.user = User.objects.create(
            username="test", password="testPassword")
        self.user.save()
        # Add a new tag to it's fav games
        self.user.favourite_games.add(self.tag)

    def test_context_dict(self):
        # Get the response when you are logged in as a specfic user
        response = self.client.get(reverse('feed'), {'user': self.user})
        # Get the post objects from the context dictionary
        posts = response.context[-1]['post_list']

        # Check every post contains the Civ 6 tag
        for post in posts:
            self.assertTrue(post.game_tag == self.tag)

    def test_empty_fav_games(TestCase):
        user = User.objects.create(username="newUser", password="newPassword")
        user.save()
        # Get the response with the new user
        response = self.client.get(reverse('feed'), {'user': user})
        # Post list sould be empty as we have no fav games
        posts = response.context[-1]['post_list']
        self.assertTrue(len(posts) == 0)


class uploadViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Picture we will try to upload
        self.picture = "logoWAD.png"
        # Make a new user
        self.user = User.objects.create(
            username="test", password="testPassword")
        self.user.save()
        # Get a tag object that we will add to the fav games of our new user
        self.tag = Tag.objects.get(text="Civ 6")
        self.tag.save()
        self.description = "test description"

    def test_upload_response(self):
        # Post a new image using a HTTP post
        response = self.client.post(
            reverse('upload'), {'author': self.user, 'picture': self.picture,
                                'game_tag': self.tag, 'description': self.description})
        # Check the request form is valid
        form = response.context[-1]['form']
        self.assertTrue(form.is_valid())


class sugTagViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Get data that we will send as a post request
        self.text = "TestTag"
        self.colour = "#FFFFFF"
        self.is_game_tag = True
        self.steamAppId = 222

    def test_new_post(self):
        # Send the data as a post request
        response = self.client.post(reverse(
            'suggest-tag'), {'text': self.text, 'colour': self.colour, 'is_game_tag': self.is_game_tag, 'steamAppId': self.steamAppId})
        # CHeck the data we sent is valid
        form = response.context[-1]['form']
        self.assertTrue(form.is_valid())


class postViewTestCase(TestCase):
    print("todo")
    # Login
    # def test_wrong_password(self):
    #     # Shouldn't accept the wrong password
    #     form = LoginForm(
    #         {'username': "Duke", 'password': "wrongPassword"})
    #     self.assertFalse(form.is_valid())

    # def test_wrong_username(self):
    #     # Shouldn't accept wrong username
    #     form = LoginForm(
    #         {'username': "wrongUsername", 'password': "testPassword123!"})
    #     self.assertFalse(form.is_valid())
    # Singup
    # def test_signup_exsisting_user(self):
    #     # should give an exception when trying to make an account with a username already taken
    #     form = SignupForm(
    #         user={'username': "test", 'password': "testPassword"})
    #     self.asserFalse(form.is_valid())

    # def test_password_length_short(self):
    #     # Shouldn't accept a very short password
    #     form = SignupForm(user={'username': "test", 'password': "abc"})
    #     self.assertFalse(form.is_valid())

    # def test_long_password_length(self):
    #     # Shouldn't  accept a form with a very long password
    #     form = SignupForm(user={
    #         'username': "test", 'password': "ThisPasswordIsFarToolongItsQuiteSillyActually"})
    #     self.assertFlase(form.is_valid())

    # def test_long_username_length(self):
    #     # Shouldn't accept a very long password
    #     form = SignupForm(
    #         user={'username': "thisisaverylongusername", 'password': "password"})
    #     self.assertFalse(form.is_valid())
#
    # Upload picture
    # def check_it_must_have_game_tag(self):
    #     # Check it won't accept a post without a game_tag selected
    #     form = UploadForm(post={'author': self.author, 'picture': self.picture,
    #                             'date_submitted': timezone.now(), 'description': "description"})
    #     self.assertFalse(form.is_valid())

    # def check_it_must_have_a_picture_seleted(self):
    #     # Check it won't accept a post that doesn't contain an image
    #     form = UploadForm(post={'author': self.author, 'date_submitted': timezone.now(
    #     ), 'description': "description"})
    #     self.assertFalse(form.is_valid())
    #
    # upload tag
    # def test_existing_tag(self):
    #         # Shouldn't allow you to upload a tag that already exists
    #     form = UploadForm(tag=self.existingTag)

    # def test_tag_without_game_name(self):
    #     # Shouldn't accept a tag without a game name
    #     form = UploadForm(form={
    #                       'colour': "#FFFFFF", 'is_game_tag': True, 'is_pending': False, 'steamAppId': 222})
    #     self.assertFalse(form.is_valid())
