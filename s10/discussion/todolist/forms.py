from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)

class AddTaskForm(forms.Form):
    task_name = forms.CharField(label='Task Name', max_length=50)
    description = forms.CharField(label='Description', max_length=200)

class UpdateTaskForm(forms.Form):
    task_name = forms.CharField(label='Task Name', max_length=50)
    description = forms.CharField(label='Description', max_length=200)
    status = forms.CharField(label='Status', max_length=50)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    first_name = forms.CharField(label='First Name', max_length=150)
    last_name = forms.CharField(label='Last Name', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

