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
    def create_post(self, a, p, gt, it, ds, de):
        # Make a user object
        ret = Post.objects.create(
            author=a, picture=p, game_tag=gt, date_submitted=ds, description=de)
        ret.save()

        ret.info_tags.add(it)
        return ret

    def test_making_post(self):
        # Need a user and a tag object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)
        # Try to make a new post
        postTest = self.create_post(
            userTest, 'static/images/logoWAS.png', tagTest, tagTest, timezone.now(), "description")

    def test_to_string(self):
        # Need a user and a tag object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)
        # Try to make a new post
        postTest = self.create_post(
            userTest, 'static/images/logoWAS.png', tagTest, tagTest, timezone.now(), "description")

        self.assertEqual(str(postTest), str(postTest.date_submitted) +
                         ": by " + str(postTest.author))


class CommentTestCase(TestCase):
    def create_comment(self, a, t, lu, pp):
        # Make a comment object
        ret = Comment.objects.create(author=a, text=t, parent_post=pp)
        ret.save()
        ret.liking_users.add(lu)

        return ret

    def test_making_comment_and_to_string(self):
        # Need a user and post object
        userTest = User.objects.create(username="test", password="password")
        tagTest = Tag.objects.create(
            text="test", colour="#FFFFF", is_game_tag=True, is_pending=True, steamAppId=222)

        postTest = Post.objects.create(author=userTest, picture='static/images/logoWAS.png', game_tag=tagTest,
                                       date_submitted=timezone.now(), description="test")
        postTest.save()
        postTest.info_tags.add(tagTest)
        # Try to make a comment object
        commentTest = self.create_comment(
            userTest, "This is a comment", userTest, postTest)

        # Test the toString of comment object
        self.assertEqual(str(commentTest), commentTest.text +
                         " by " + str(commentTest.author))
