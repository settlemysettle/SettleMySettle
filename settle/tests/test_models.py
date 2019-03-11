from django.test import TestCase
# Import the models
from settle.models import Tag, User, Post, Comment
from settle.fields import ColourField
from django.utils import timezone


class TagTestCase(TestCase):
    def create_tag(self, t, c, gt, isP, sa):
        # Use this to make Tag objects
        return Tag.objects.create(text=t, colour=c, is_game_tag=gt,
                                  is_pending=isP, steamAppId=sa)

    def try_making_tag(self):
        # Make Tag with method
        tagTest = self.create_tag("test tag", "#FFFFFF", True, False, 222)
        # Assert tagTest is a Tag object
        self.assertTrue(isinstance(tagTest, Tag))

    def test_tag_toString(self):
        # Make Tag with method
        tagTest = self.create_tag("test tag", "#FFFFFF", True, False, 222)
        # Assert the toString method returns the title
        self.assertEqual(str(tagTest), tagTest.text)


class UserTestCase(TestCase):
    def create_user(self, un, pa):
        # Make using the user model
        return User.objects.create(username=un, password=pa)

    def test_making_user(self):
        # Make a user using our method
        userTest = self.create_user("test", "password")
        # Check it is an instance of the User class
        self.assertTrue(isinstance(userTest, User))

    def test_user_toString(self):
        # Make a user using our method
        userTest = self.create_user("test", "password")
        # CHeck the string method works
        self.assertEqual(userTest.username, str(userTest))


class PostTestCase(TestCase):
    def create_post(self, a, p, gt, it, ds, pi, de):
        # Make a user object
        return Post.objects.create(author=a, picture=p, game_tag=gt, info_tags=it, date_submitted=ds,
                                   post_id=pi, description=de)

    def test_making_post(self):
        # Need a user and a tag object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)
        # Try to make a new post
        postTest = self.create_post(
            userTest, 'static/images/logoWAS.png', tagTest, tagTest, timezone.now(), 2222, "description")

    def test_to_string(self):
        # Need a user and a tag object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)
        # Try to make a new post
        postTest = self.create_post(
            userTest, 'static/images/logoWAS.png', tagTest, tagTest, timezone.now(), 2222, "description")

        self.assertEqual(str(postTest), postTest.text +
                         " by " + str(postTest.author))


class CommentTestCase(TestCase):
    def create_comment(self, a, t, lu, pp):
        # Make a comment object
        return Comment.objects.create(author=a, text=t, liking_users=lu, parent_post=pp)

    def test_making_comment_and_to_string(self):
        # Need a user and post object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)

        postTest = Post.objects.create(author=userTest, picture='static/images/logoWAS.png', game_tag=tagTest,
                                       info_tags=tagTest, date_submitted=timezone.now(),
                                       post_id=222, description="test")
        # Try to make a comment object
        commentTest = self.create_comment(
            userTest, "This is a comment", userTest, postTest)

        # Test the toString of comment object
        self.assertEqual(str(commentTest), commentTest.text +
                         " by " + str(commentTest.author))
