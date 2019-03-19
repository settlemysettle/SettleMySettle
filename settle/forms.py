from django import forms
from settle.models import Tag, User, Post, Comment
from django.forms.widgets import TextInput


class CommentForm(forms.ModelForm):
    """The form for posting a new comment."""

    # Will inherit the fields from the comment model
    text = forms.CharField(
        max_length=300, widget=forms.Textarea, required=True)

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
        help_text="The password must be at least 8 characters in length, contain an upper and lowercase letter and contain at least one digit")
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
    """The form used to post a picture."""

    # Give the description a box to write in
    description = forms.CharField(
        max_length=300, required=False, widget=forms.Textarea)
    picture = forms.ImageField(required=True)
    game_tag = forms.ModelChoiceField(queryset=Tag.objects.filter(
        is_game_tag=True).filter(is_pending=False).order_by("text"))

    info_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(is_game_tag=False).filter(
        is_pending=False).order_by("text"), widget=forms.CheckboxSelectMultiple(attrs={'class': 'info-tag-list'}))

    class Meta:
        # Make it inherit fields from Post model
        model = Post
        # These values will be generated automatically
        exclude = ['author', 'date_submitted']


class AddFavGame(forms.Form):
    # Select the game tags as a multiple choice field
    game_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(
        is_game_tag=True).filter(is_pending=False).order_by("text"), widget=forms.CheckboxSelectMultiple(attrs={'class': 'game-tag-list'}))

    class Meta:
        fields = ['game_tags']


class SuggestTag(forms.ModelForm):
    """A form used to upload a tag suggestion."""

    text = forms.CharField(max_length=20, required=True)

    colour = forms.CharField(max_length=7, required=True, widget=TextInput(attrs={"type": "color"}))

    is_game_tag = forms.BooleanField(required=False)

    steamAppId = forms.IntegerField(min_value=0, required=False)

    # Will inherit the fields from the model

    class Meta:
        model = Tag
        # Don't show is_pending field
        exclude = ['is_pending']
