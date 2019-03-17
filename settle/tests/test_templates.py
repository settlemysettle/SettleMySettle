from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class BaseTemTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_and_base_templates_used(self):
        response = self.client.get(reverse('index'))
        # Check it got a response back
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'settle/index.html')
        # Should also use the base/html
        self.assertTemplateUsed(response, 'settle/base.html')

    def test_if_name_on_nav_bar(self):
        response = self.client.get(reverse('index'))
        # Check that index page was accessed
        self.assertEqual(response.status_code, 200)

        # Check that the name of the website appears on the template
        self.assertContains(response, 'Settle My Settle')

    def test_logo_on_nav_bar(self):
        response = self.client.get(reverse('index'))

        # Make sure index page was accessed
        self.assertEqual(response.status_code, 200)
        # Make sure logo is present
        self.assertContains(response, "images/favicon.ico")

    def test_home_link_is_visible_on_nav_bar(self):
        response = self.client.get(reverse('index'))

        # check that the index page was found
        self.assertEqual(response.status_code, 200)

        # Check that the home page is visible
        self.assertContains(response, 'Home')

    def test_myFeed_link_is_visible_on_nav_bar(self):
        response = self.client.get(reverse('index'))

        # check that the index page was found
        self.assertEqual(response.status_code, 200)

        # Check that the feed page is visible
        self.assertContains(response, 'My Feed')

    def test_upload_link_is_visible_on_nav_bar(self):
        response = self.client.get(reverse('index'))

        # check that the index page was found
        self.assertEqual(response.status_code, 200)

        # Check that the upload page is visible
        self.assertContains(response, 'Upload')

    def test_suggestTag_link_is_visible_on_nav_bar(self):
        response = self.client.get(reverse('index'))

        # check that the index page was found
        self.assertEqual(response.status_code, 200)

        # Check that the suggest tag page is visible
        self.assertContains(response, 'Suggest Tag')


class loginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('login'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the login template
        self.assertTemplateUsed(response, 'settle/login.html')

    def access_login_page(self):
        response = self.client.get(reverse('login'))
        # Check that login page was accessed
        self.assertEqual(response.status_code, 200)

        # Check it contains a link to login
        self.assertContains(response, 'Sign in')

    def contains_username_and_password_fileds(self):
        response = self.client.get(reverse('login'))
        # Check that the page was accessed
        self.assertEqual(response.status_code, 200)
        # Check it contains the correct fields
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')


class logoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('logout'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the logout template
        self.assertTemplateUsed(response, 'logout.html')

    def access_logout_page(self):
        response = self.client.get(reverse('registration/logout'))
        # Check that logout page was accessed
        self.assertEqual(response.status_code, 200)

        # Check it contains a message saying we've logged out
        self.assertContains(response, 'You are now logged out.')


class feedTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('feed'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the feed template
        self.assertTemplateUsed(response, 'settle/feed.html')

    def access_feed_page(self):
        response = self.client.get(reverse('feed'))
        # Check that feed page was accessed
        self.assertEqual(response.status_code, 200)


class indexTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('index'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the index template
        self.assertTemplateUsed(response, 'settle/index.html')

    def access_index_page(self):
        response = self.client.get(reverse('index'))
        # Check that index page was accessed
        self.assertEqual(response.status_code, 200)


class suggestTagTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('suggest-tag'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the suggest-tag template
        self.assertTemplateUsed(response, 'settle/suggest-tag.html')

    def access_suggest_tag_page(self):
        response = self.client.get(reverse('suggest-tag'))
        # Check that suggest-tag page was accessed
        self.assertEqual(response.status_code, 200)

        # Check it contains a message saying we can make a tag
        self.assertContains(response, 'Create a Tag')

    def contains_tag_options(self):
        response = self.client.get(reverse('suggest-tag'))
        # Check that suggest-tag page was accessed
        self.assertEqual(response.status_code, 200)

        # Check it contains a tag type option
        self.assertContains(response, 'Tag Type')

        # Check it Contains a colour type
        self.assertContains(response, 'Colour')

        # Check it contains a tag field
        self.assertContains(response, 'Tag Text')

        # Check it contains a Steam AppID and url
        self.assertContains(response, 'Steam AppID')
        self.assertContains(response, 'Test Steam URL')

    def contains_preview_and_submit(self):
        response = self.client.get(reverse('suggest-tag'))
        # Check that suggest-tag page was accessed
        self.assertEqual(response.status_code, 200)

        # Check it contains a preview
        self.assertContains(response, 'Preview')
        # Check it contains a submit button
        self.assertContains(response, 'Submit')


class uploadTempTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def check_it_uses_template(self):
        response = self.client.get(reverse('upload'))
        # Check it uses the base template
        self.assertTemplateUsed(response, 'settle/base.html')
        # Check it uses the upload template
        self.assertTemplateUsed(response, 'settle/upload.html')

    def check_it_contains_upload_options(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)
        # Check it contains an image field with the ability to upload
        # an image
        self.assertContains(response, 'Image')
        self.assertContains(response, 'Choose Photo')

    def check_it_contains_tag_options(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)
        # Check it contains a game and info tag box
        self.assertContains(response, 'Select Game Tag')
        self.assertContains(response, 'Select Info Tags (max 5)')

    def test_it_has_description_box(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)
        # Check it contains description box
        self.assertContains(response, 'Description')
