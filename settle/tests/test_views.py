from django.test import TestCase
# from settle.views import ...


class IndexViewTestCase(TestCase):
    # Check it has pictures (context dict)
    #
    print("todo")


class feedViewTestCase(TestCase):
    print("todo")


class uploadViewTestCase(TestCase):
    print("todo")


class sugTagViewTestCase(TestCase):
    print("todo")
<<<<<<< HEAD


class postViewTestCase(TestCase):
    print("todo")
=======
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
>>>>>>> 76fb66243011c658ee15964554d8bbddaafb410c
