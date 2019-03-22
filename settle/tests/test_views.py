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
            username="test", password="testPassword1", email="testemail@email.com")
        self.user.save()
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
        # Login with the made user
        self.client.force_login(self.user)
        # Get the response when you are logged in as a specfic user
        response = self.client.get(reverse('feed'))
        # Get the post objects from the context dictionary
        posts = response.context['posts']

        # Check every post contains the Civ 6 tag
        for post in posts:
            self.assertTrue(post.game_tag == self.tag)

    def test_empty_fav_games(self):
        user = User.objects.create(
            username="newUser", password="newPassword", email="test@email.com")
        user.save()
        # Login
        self.client.force_login(user)
        # Get the response with the new user
        response = self.client.get(reverse('feed'), {'user': user})
        # Post list sould be empty as we have no fav games
        posts = response.context[-1]['posts']
        self.assertEqual(len(posts), 0)


class sugTagViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Get data that we will send as a post request
        self.text = "TestTag"
        self.colour = "#FFFFFF"
        self.is_game_tag = True
        self.steamAppId = 222

    def test_new_post(self):
        user = User.objects.create(
            username="newUser", password="newPassword", email="test@email.com")
        user.save()
        self.client.force_login(user)
        # Send the data as a post request
        response = self.client.post(reverse('tags'),
                                    {'text': self.text, 'colour': self.colour, 'is_game_tag': self.is_game_tag,
                                     'steamAppId': self.steamAppId, 'type': 'suggest', 'user': user.username})
        # CHeck the data we sent is valid
        form = response.context['suggest_form']
        self.assertTrue(form.is_valid())


class loginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Make a user that we can sign in with
        user = User.objects.create(
            username="newUser", password="newPassword", email="test@email.com")

    def signin_Test(self):
        # Should redirect if logged in corretly
        response = self.client.post(
            reverse('login'), {'username': "newUser", 'password': "newPassword"})
        self.assertEqual(response.status_code, 302)

    def sign_InInvalid_Test(self):
        response = self.client.post(
            reverse('login'), {'username': 'wrong', 'password': "notRight1"})
        self.assertFalse(response.context['valid'])


class SignupView(TestCase):
    def setUp(self):
        # Get the client we will use
        self.client = Client()
        # Use we will try to signup
        self.newUser = {'email': "testemail@test.com",
                        'username': "Duke", 'password': "testPassword123!",
                        'confirm_password': "testPassword123!"}

    def test_new_user(self):
        response = self.client.post(reverse('register'), self.newUser)
        # Should redirect to home if valid
        self.assertEqual(response.status_code, 302)

    def test_lowercase_password(self):
        response = self.client.post(reverse('register'), {'email': "testemail@test.com",
                                                          'username': "Duke", 'password': "password",
                                                          'confirm_password': "password"})
        # Should be returned with form errors
        form = response.context['signup_form']
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        response = self.client.post(reverse('register'), {'email': "testemail@test.com",
                                                          'username': "Duke", 'password': "pw1",
                                                          'confirm_password': "pw1"})
        # Should be returned with form errors
        form = response.context['signup_form']
        self.assertFalse(form.is_valid())

    def test_justUpper_password(self):
        response = self.client.post(reverse('register'), {'email': "testemail@test.com",
                                                          'username': "Duke", 'password': "PASSWORD",
                                                          'confirm_password': "PASSWORD"})
        # Should be returned with form errors
        form = response.context['signup_form']
        self.assertFalse(form.is_valid())

    def test_noDigits_password(self):
        response = self.client.post(reverse('register'), {'email': "testemail@test.com",
                                                          'username': "Duke", 'password': "Password",
                                                          'confirm_password': "Password"})
        # Should be returned with form errors
        form = response.context['signup_form']
        self.assertFalse(form.is_valid())
