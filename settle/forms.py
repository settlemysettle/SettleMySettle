from django import forms
from settle.models import Tag, User, Post, Comment


class CommentForm(forms.ModelForm):
    """The form for posting a new comment."""

    # Will inherit the fields from the comment model
    text = forms.CharField(max_length=300, widget=forms.Textarea)

    class Meta:
        # Choose the Comment model
        model = Comment
        fields = ['text']


class SignupForm(forms.ModelForm):
    """ Form used to registor a new user."""

    username = forms.CharField(
        max_length=20, help_text="Choose a username upto 20 characters long.", required=True)
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(), required=True)

    # Provides additional info on the form
    class Meta:
        model = User
        # Don't show fav games filled as this will be updated in another form
        fields = ['username', 'password']


class UploadForm(forms.ModelForm):
    """The form used to post a picture."""

    # Give the description a box to write in
    description = forms.CharField(
        max_length=300, required=False, widget=forms.Textarea)
    picture = forms.ImageField(required=True)

    class Meta:
        # Make it inherit fields from Post model
        model = Post
        # These values will be generated automatically
        exclude = ['author', 'date_submitted']


class UploadTag(forms.ModelForm):
    """A form used to upload a tag suggestion."""

    # Will inherit the fields from the model
    class Meta:
        model = Tag
        # Don't show is_pending field
        exclude = ['is_pending']
