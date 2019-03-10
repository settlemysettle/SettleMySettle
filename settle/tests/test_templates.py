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

    def check_it_uses_template(self):
        res = self.client.get('/login')
        # Check it uses the base template
        self.assertTemplateUsed(res, 'base.html')
        # Check it uses the login template
        self.assertTemplateUsed(res, 'login.html')

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
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        res = self.client.get('/logout')
        # Check it uses the base template
        self.assertTemplateUsed(res, 'base.html')
        # Check it uses the logout template
        self.assertTemplateUsed(res, 'logout.html')

    def access_logout_page(self):
        res = self.client.get('/logout')
        # Check that logout page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a message saying we've logged out
        self.assertContains(res, 'You are now logged out.')


class feedTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        res = self.client.get('/feed')
        # Check it uses the base template
        self.assertTemplateUsed(res, 'base.html')
        # Check it uses the feed template
        self.assertTemplateUsed(res, 'feed.html')

    def access_feed_page(self):
        res = self.client.get('/feed')
        # Check that feed page was accessed
        self.assertEqual(res.status_code, 200)


class indexTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        res = self.client.get('/')
        # Check it uses the base template
        self.assertTemplateUsed(res, 'base.html')
        # Check it uses the index template
        self.assertTemplateUsed(res, 'index.html')

    def access_index_page(self):
        res = self.client.get('/')
        # Check that index page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a message saying we've logged out
        self.assertContains(res, 'You are now logged out.')


class suggestTagTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        res = self.client.get('/suggest-tag')
        # Check it uses the base template
        self.assertTemplateUsed(res, 'base.html')
        # Check it uses the suggest-tag template
        self.assertTemplateUsed(res, 'suggest-tag.html')

    def access_suggest_tag_page(self):
        res = self.client.get('/suggest-tag')
        # Check that suggest-tag page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a message saying we can make a tag
        self.assertContains(res, 'Create a Tag')

    def contains_tag_options(self):
        res = self.client.get('/suggest-tag')
        # Check that suggest-tag page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a tag type option
        self.assertContains(res, 'Tag Type')

        # Check it Contains a colour type
        self.assertContains(res, 'Colour')

        # Check it contains a tag field
        self.assertContains(res, 'Tag Text')

        # Check it contains a Steam AppID and url
        self.assertContains(res, 'Steam AppID')
        self.assertContains(res, 'Test Steam URL')

    def contains_preview_and_submit(self):
        res = self.client.get('/suggest-tag')
        # Check that suggest-tag page was accessed
        self.assertEqual(res.status_code, 200)

        # Check it contains a preview
        self.assertContains(res, 'Preview')
        # Check it contains a submit button
        self.assertContains(res, 'Submit')


class uploadTempTestCase(TestCase):
    print("todo")
