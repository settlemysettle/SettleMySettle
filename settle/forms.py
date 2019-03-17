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
    # Give help text to the username
    username = forms.CharField(
        max_length=20, help_text="Choose a unique username upto 20 characters long.", required=True)
    # Make the passowrd field use password input
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput(), required=True,
        help_text="The password msut be at least 8 characters in length, contain an upper and lowercase letter and contain at least one digit")
    # Make sure the put in the same password
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # Provides additional info on the form
    class Meta:
        model = User
        # Onlyshow the following fileds from the inherited model
        fields = ['email', 'username', 'password']

    def clean(self):
        # Get the data put into the form
        cleaned_data = super(SignupForm, self).clean()
        # Get the password and confirmed password
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        # Check they match, else add a new error
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")

        return cleaned_data


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
