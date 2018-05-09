from django import forms
from models import Posting, Profile, Massage, forum_topic, forum_post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class postingForm(forms.ModelForm):
    catergo = (('Free', "Free"), ('For Sale', "For Sale"), ('Currency Exchange', "Currency Exchange"), ("Wanted", "Wanted"),)
    catergo = forms.ChoiceField(choices=catergo, widget=forms.RadioSelect())
    class Meta():
        model = Posting
        fields = ('header','catergo','body', 'airport')
class message(forms.ModelForm):
    class Meta():
        model = Massage
        fields = ('text',)

class topicForm(forms.ModelForm):
    class Meta():
        model = forum_topic
        fields = ('title', 'catregory')
class forumPostForm(forms.ModelForm):
    class Meta():
        model = forum_post
        fields = ('text',)

class apcSearch(forms.Form):
    apc = forms.CharField(max_length = 3)
