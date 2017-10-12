from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", max_length=45)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label="Password:", 
                               max_length=255, min_length=8)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/login/'
    helper.add_input(Submit('submit', 'GO!'))

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
    old_login = forms.CharField(label="Old username:",
                                max_length=45, min_length=2)
    old_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old password'}),
                               label="old Password:",
                               max_length=258, min_length=8)
    new_login = forms.CharField(label="New username:",
                                max_length=45, min_length=2)
    new_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'new password'}),
                               label="Password:", 
                               max_length=258, min_length=8)
    confirm_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm'}),
                                   label="Confirm Password:", max_length=255, min_length=8)
                                   
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Current Info',
            'old_login',
            'old_pass',
        ),
        Fieldset(
            'Update Info',
            'new_login',
            'new_pass',
            'confirm_pass',
        ),
        ButtonHolder(
            Submit('submit', 'GO!'),
        )
    )
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/login/'

    def clean(self):
        form_data = self.cleaned_data
        user = authenticate(username=form_data['old_login'],
                            password=form_data['old_pass'])
        if user is None:
            msg = 'Login and password do not match'
            self.add_error('old_login', msg)
            self.add_error('old_pass', msg)
        else:
            self.cleaned_data['user'] = user
        if form_data.get('new_pass') != form_data.get('confirm_pass'):
            msg = 'Passwords do not match!'
            self.add_error('new_pass', msg)
            self.add_error('confirm_pass', msg)
        return form_data
