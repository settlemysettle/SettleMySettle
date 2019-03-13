from django import forms
from settle.models import Tag, User, Post, Comment


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        help_text="Please enter your username.", required=True)
    # Means the password is hidden when logging in
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    # So we can save the form and the data it contains
    def save(self):
        loginf = super().save(commit=False)
        loginf.save()
        return loginf

    # Provides additional info on the form
    class Meta:
        model = User
        fields = ('username', 'password')

# class CommentForm(forms.ModelForm):


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20, help_text="Choose a username upto 20 characters long.", required=True)
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(), required=True)
    # favourite_games = forms.CharField
    # DOn't know if I need this

    # Provides additional info on the form
    class Meta:
        model = User
        fields = ('username', 'password')
