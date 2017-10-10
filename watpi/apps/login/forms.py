from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", max_length=45)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/login/'
    helper.add_input(Submit('submit', 'Login'))
    def clean(self):
        form_data = self.cleaned_data
        print form_data['username'], form_data['password']
        user = authenticate(username=form_data['username'], password=form_data['password'])
        self.cleaned_data['user'] = user
        if user is None:
            msg = 'Login and password do not match'
            self.add_error('username', msg)
            self.add_error('password', msg)
        return form_data

class ChangePassForm(forms.Form):
    username = forms.CharField(label="Username:", max_length=45, min_length=2)
    oldpass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}),label="Password:", max_length=258, min_length=8)
    newpass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Confirm pw:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/login'
    helper.add_input(Submit('submit', 'Change Password'))
    def clean(self):
        form_data = self.cleaned_data
        if len(User.objects.filter(alias=form_data.get('alias'))) > 0:
            msg = 'User already registered'
            self.add_error('alias', msg)
        if form_data.get('password') != form_data.get('confirm'):
            msg = 'Passwords do not match!'
            self.add_error('password', msg)
        return form_data
