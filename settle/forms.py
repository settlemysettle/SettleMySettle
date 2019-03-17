from django import forms
from settle.models import Tag, User, Post, Comment


class LoginForm(forms.ModelForm):
    # Using a ModelForm as it will inhert the fields from the model

    # Give a widget to hide password when entering
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    class Meta:
        # Choose the model it will inherent the fileds from
        model = User
        exclude = ['favourite_games']


class CommentForm(forms.ModelForm):
    # Will inherit the fields from the comment model
    text = forms.CharField(max_length=300, widget=forms.Textarea)

    class Meta:
        # Choose the Comment model
        model = Comment
        fields = ['text']


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20, help_text="Choose a username upto 20 characters long.", required=True)
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(), required=True)

    # Provides additional info on the form
    class Meta:
        model = User
        # Don't show fav games filled as this will be updated in another form
        fields = ['email', 'username', 'password']


class UploadForm(forms.ModelForm):
    # Give the description a box to write in
    description = forms.CharField(
        max_length=300, required=False, widget=forms.Textarea)

    class Meta:
        # Make it inherit fields from Post model
        model = Post
        exclude = ['author', 'date_submitted']


class UploadTag(forms.ModelForm):
    # Will inherit the fields from the model
    class Meta:
        model = Tag
        # Don't show is_pending field
        exclude = ['is_pending']
