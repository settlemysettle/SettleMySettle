from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from settle.models import User, Tag, Post
from django.utils import timezone


class IndexViewTestCase(TestCase):
    def setUp(self):
        # Make a client
        self.client = Client()
        # Make a user that will upload the posts to find
        self.user = User.objects.create(
            username="test", password="testPassword")
        # Tag for the post
        self.tag = Tag.objects.create(
            text="Civ 6", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        # Make a save three new posts
        for i in range(3):
            self.post = Post.objects.create(author=self.user, picture='static/images/logoWAD.png', game_tag=self.tag,
                                            date_submitted=timezone.now(), description="test")
            # Save the post
            self.post.save()

    def test_context_dict(self):
        response = self.client.get(reverse('index'))
        # The context_dict should contain a list of images it will display to the page
        posts = response.context[-1]['posts']
        # Should return 3 images as it does inifite scroll
        self.assertEqual(len(posts), 3)


class feedViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Make a tag object that we will add to the fav games of our new user
        self.tag = Tag.objects.create(
            text="Civ 6", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        self.tag2 = Tag.objects.create(
            text="Civ 5", colour="#FF8FFF", is_game_tag=True, is_pending=False, steamAppId=222)
        # Make a new user
        self.user = User.objects.create(
            username="test", password="testPassword")
        # self.user.save()
        # Add a new tag to it's fav games
        self.user.favourite_games.add(self.tag)
        self.userTest = User.objects.create(
            username="testUser", password="password")

        self.post = Post.objects.create(
            author=self.userTest, picture='static/images/logoWAD.png', game_tag=self.tag, date_submitted=timezone.now(),
            description="test")
        self.post.save()
        # Make a different post with a different tag
        self.post2 = Post.objects.create(
            author=self.userTest, picture='static/images/logoWAD.png', game_tag=self.tag2, date_submitted=timezone.now(),
            description="test")
        self.post2.save()

    def test_context_dict(self):
        # Get the response when you are logged in as a specfic user
        response = self.client.get(reverse('feed'), {'user': self.user})
        # Get the post objects from the context dictionary
        posts = response.context[-1]['posts']

        # Check every post contains the Civ 6 tag
        for post in posts:
            self.assertTrue(post.game_tag == self.tag)

    def test_empty_fav_games(self):
        user = User.objects.create(username="newUser", password="newPassword")
        user.save()
        # Get the response with the new user
        response = self.client.get(reverse('feed'), {'user': user})
        # Post list sould be empty as we have no fav games
        posts = response.context[-1]['posts']
        self.assertEqual(len(posts), 0)


class uploadViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Picture we will try to upload
        self.picture = "logoWAD.png"
        # Make a new user
        self.user = User.objects.create(
            username="test", password="testPassword")
        self.user.save()
        # Get a tag object that will be the gametag of the upload
        self.tag = Tag.objects.create(
            text="Civ 6", colour="#FFFFFF", is_game_tag=True, is_pending=False, steamAppId=222)
        self.description = "test description"

    def test_upload_response(self):
        # Post a new image using a HTTP post
        response = self.client.post(
            reverse('upload'), {'author': self.user, 'picture': self.picture,
                                'game_tag': self.tag, 'description': self.description, 'info_tags': []})
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
        response = self.client.post(reverse('tags'),
                                    {'text': self.text, 'colour': self.colour, 'is_game_tag': self.is_game_tag,
                                     'steamAppId': self.steamAppId})
        # CHeck the data we sent is valid
        form = response.context[-1]['form']
        self.assertTrue(form.is_valid())
