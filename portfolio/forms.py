from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog
from portfolio.models import Author


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ('username', 'email')


class LogInForm(AuthenticationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ('username', 'email')


class CreateBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'tag', 'image','body')

class AuthorProfileForm(ModelForm):
    class Meta:
        model = Author
        fields = ('Name', 'image', 'Bio','Location', 'Work')