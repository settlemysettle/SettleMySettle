from django.test import TestCase
from django.test import Client


class BaseTemTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_and_base_templates_used(self):
        res = self.client.get('/')
        # Check it got a response back
        self.assertEqual(res.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(res, 'index.html')
        # Should also use the base/html
        self.assertTemplateUsed(res, 'base.html')

    def test_if_name_on_nav_bar(self):
        res = self.client.get('/')
        # Check that index page was accessed
        self.assertEqual(res.status_code, 200)

        # Check that the name of the website appears on the template
        self.assertContains(res, 'Settle My Settle')

    def test_logo_on_nav_bar(self):
        res = self.client.get('/')

        # Make sure index page was accessed
        self.assertEqual(res.status_code, 200)
        # Make sure logo is present
        self.assrtContains(res, "images/favicon.ico")

    def test_home_link_is_visible_on_nav_bar(self):
        res = self.client.get('/')

        # check that the index page was found
        self.assertEqual(res.status_code, 200)

        # Check that the home page is visible
        self.assertContains(res, 'Home')

    def test_myFeed_link_is_visible_on_nav_bar(self):
        res = self.client.get('/')

        # check that the index page was found
        self.assertEqual(res.status_code, 200)

        # Check that the feed page is visible
        self.assertContains(res, 'My Feed')

    def test_upload_link_is_visible_on_nav_bar(self):
        res = self.client.get('/')

        # check that the index page was found
        self.assertEqual(res.status_code, 200)

        # Check that the upload page is visible
        self.assertContains(res, 'Upload')

    def test_suggestTag_link_is_visible_on_nav_bar(self):
        res = self.client.get('/')

        # check that the index page was found
        self.assertEqual(res.status_code, 200)

        # Check that the suggest tag page is visible
        self.assertContains(res, 'Suggest Tag')


class loginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def access_login_page(self):
        res = self.client.get('/login')
        # Check that login page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a link to login
        self.assertContains(res, 'Sign in')

    def contains_username_and_password_fileds(self):
        res = self.client.get('/login')
        # Check that the page was accessed
        self.assertEqual(res.status_code, 200)
        # Check it contains the correct fields
        self.assertContains(res, 'Username')
        self.assertContains(res, 'Password')


class logoutTestCase(TestCase):
    print("todo")


class passChangeTestCase(TestCase):
    print("todo")


class regFormTestCase(TestCase):
    print("todo")


class feedTempTestCase(TestCase):
    print("todo")


class indexTempTestCase(TestCase):
    print("todo")


class suggestTagTempTestCase(TestCase):
    print("todo")


class uploadTempTestCase(TestCase):
    print("todo")
