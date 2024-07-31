from django import forms
from django.contrib.auth.models import User
from .models import Post



class UserDetailsForm(forms.Form):
    fname = forms.CharField(max_length=30, required=True)
    lname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

class UsernamePasswordForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    pass1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    pass2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')
        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
