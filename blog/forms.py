from django import forms
from .models import Post, RePost

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

class NewForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    email = forms.CharField(label='电子邮箱', max_length=300)

class RePostForm(forms.ModelForm):

    class Meta:
        model = RePost
        fields = ('text',)